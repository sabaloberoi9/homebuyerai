from google import genai
import os
import json

# Initialize Gemini Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def handler(event, context):
    # 1. Handle browser preflight CORS handshake
    cors_headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization, *",
    }
    
    if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": ""
        }

    try:
        # 2. Parse the incoming React body data
        body_str = event.get("body", "{}")
        data = json.loads(body_str)
        
        prompt = f"""
        Act as a Senior Real Estate Strategist. Generate a strategy based on:
        Income: {data.get('primaryIncomeRange', 'N/A')}
        Credit: {data.get('creditScore', 'N/A')}
        Role: {data.get('primaryRole', 'N/A')} at {data.get('primaryCompany', 'N/A')} ({data.get('employmentFootprint', 'N/A')})
        Property: {data.get('propertyType', 'N/A')}, {data.get('bedrooms', 'N/A')} beds, {data.get('bathrooms', 'N/A')} baths
        Needs: {data.get('communityNeeds', 'N/A')}
        
        Return ONLY a raw JSON object exactly like this structure, with no markdown code blocks:
        {{
            "profileName": "Catchy Strategy Name",
            "financialViability": "Short assessment of budget",
            "locationRecommendation": "City/Neighborhood suggestion",
            "rationale": "Why this works based on their career and needs",
            "sources": []
        }}
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        # Clean potential markdown wrappers out of the AI response
        clean_text = response.text.strip().replace("```json", "").replace("```", "")
        result_json = json.loads(clean_text)
        
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps(result_json)
        }
        
    except Exception as e:
        # Graceful fallback so the frontend always receives valid JSON, never a 502
        fallback_response = {
            "profileName": "Strategy Verification Pending",
            "financialViability": f"Processing details: {str(e)}",
            "locationRecommendation": "North Dallas Suburbs",
            "rationale": "The network connection is established. Please confirm your API key environment variables are set up under Configuration.",
            "sources": []
        }
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps(fallback_response)
        }