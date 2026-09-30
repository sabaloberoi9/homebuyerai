import boto3
import json
from google import genai

# Configure your API key here for testing
GEMINI_API_KEY = "AIzaSyCxjgMowg_qGakIRpJaz5W-FVp5shcOmts"
client = genai.Client(api_key=GEMINI_API_KEY)

def run_ai_security_scan():
    print("Step 1: Fetching security groups from AWS...")
    ec2 = boto3.client('ec2', region_name='us-east-2')
    response = ec2.describe_security_groups()
    raw_aws_json = json.dumps(response['SecurityGroups'][0], indent=2)
    
    print("Step 2: Feeding AWS configuration into the modern Gemini client...")
    
    prompt = f"""
    You are a Senior Cloud Security Auditor. Analyze this raw AWS Security Group JSON:
    {raw_aws_json}
    
    Identify any security flaws, misconfigurations, or risks. 
    Provide your assessment in clear bullet points:
    1. Overall Risk Level (Low/Medium/High)
    2. Vulnerability Description
    3. Exact Remediation Steps (How to fix it)
    """
    
    try:
        # Using the upgraded, modern SDK method
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        print("\n=== UPGRADED GEMINI SECURITY AUDIT REPORT ===")
        print(response.text)
        print("=============================================")
    except Exception as e:
        print(f"AI Scan failed: {e}")

if __name__ == "__main__":
    run_ai_security_scan()