import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum
import google.generativeai as genai

# Initialize FastAPI app
app = FastAPI(title="Homeowner Navigator API")

# Configure CORS (Crucial for allowing your S3 frontend to talk to your EC2 backend)
# Once deployed, replace "*" with your actual S3 bucket website URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini API securely via Environment Variables
# NEVER hardcode the API key in this file
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Define the expected data structure from the React frontend
class UserStrategyData(BaseModel):
    primaryIncomeRange: str
    creditScore: str
    employmentFootprint: str
    primaryCompany: str
    primaryRole: str
    secondaryIncomeRange: str = ""
    secondaryEmploymentFootprint: str = ""
    secondaryCompany: str = ""
    secondaryRole: str = ""
    propertyType: str
    bedrooms: str
    bathrooms: str
    lowTaxPriority: bool = False
    lowHoaPriority: bool = False
    lowUtilitiesPriority: bool = False
    communityNeeds: str

@app.post("/api/strategy")
async def generate_strategy(data: UserStrategyData):
    try:
        # 1. Construct the Mega Prompt using the validated data
        secondary_role_str = ""
        if data.secondaryIncomeRange:
            secondary_role_str = f"- Secondary: {data.secondaryRole} at {data.secondaryCompany} ({data.secondaryEmploymentFootprint})"

        mega_prompt = f"""
        ACT AS: Senior Real Estate Strategist & Data Analyst.
        TASK: Generate a "Strategic Profile" for a home buyer based on the inputs below.

        USER INPUTS:
        1. FINANCIAL:
           - Primary Income: {data.primaryIncomeRange}
           - Credit Score: {data.creditScore}
           - Tax Priority: {'Strict Low Tax Preference' if data.lowTaxPriority else 'Standard'}
           - HOA Priority: {'Strict Low HOA Preference' if data.lowHoaPriority else 'Standard'}
           - Utilities Priority: {'Low Utilities Preference' if data.lowUtilitiesPriority else 'Standard'}

        2. CAREER (CRITICAL):
           - Primary: {data.primaryRole} at {data.primaryCompany} ({data.employmentFootprint})
           {secondary_role_str}

        3. PROPERTY:
           - Type: {data.propertyType}
           - Min Beds: {data.bedrooms}
           - Min Baths: {data.bathrooms}

        4. COMMUNITY NEEDS (THE "WHY" - HIGH PRIORITY):
           "{data.communityNeeds}"

        SYSTEM INSTRUCTIONS:
        1. ANALYZE AFFORDABILITY: Cross-reference income ranges with current interest rates and median home prices in viable locations.
        2. ANALYZE CAREER VIABILITY: Prioritize locations with proximity to the stated Employer Office (if "Office-Based") or high industry density.
        3. ANALYZE LIFESTYLE: Find specific suburbs/cities that strictly match the "Community Needs" (e.g., school districts, specific cultural amenities).
        4. FAILSAFE (FHA): DO NOT mention race, religion, or demographics. Use objective proxies only (amenity counts, school scores).
        5. OUTPUT FORMAT (STRICT JSON):
           Return ONLY a raw JSON object (no markdown formatting). The JSON must have these exact keys:
           {{
             "profileName": "A catchy title for this strategy",
             "financialViability": "A detailed assessment of their budget vs market reality",
             "locationRecommendation": "Specific Cities/Suburbs",
             "rationale": "A comprehensive paragraph explaining WHY this location matches their Career, Money, and Lifestyle needs.",
             "sources": [{{"title": "Source Name", "uri": "URL"}}]
           }}
        """

        # 2. Call the LLM (using the specific model from your prototype)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Enforce JSON output format directly in the model configuration
        response = model.generate_content(
            mega_prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
            )
        )

        # 3. Parse the validated JSON string back into a Python dictionary and return it to the frontend
        strategy_json = json.loads(response.text)
        return strategy_json

    except Exception as e:
        # Return a clean 500 error to the frontend if something breaks
        raise HTTPException(status_code=500, detail=str(e))

# Run locally using: uvicorn main:app --reload
handler = Mangum(app)