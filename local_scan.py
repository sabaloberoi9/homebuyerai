import boto3
import json

def get_local_security_groups():
    print("Connecting to AWS to fetch Security Groups...")
    
    # Boto3 uses the credentials you just configured in your terminal automatically
    client = boto3.client('ec2', region_name='us-east-2')
    
    try:
        response = client.describe_security_groups()
        groups = response['SecurityGroups']
        
        print(f"Successfully fetched {len(groups)} Security Group(s)!\n")
        
        # Print out just the first group beautifully formatted so we can see it
        print(json.dumps(groups[0], indent=4))
        
    except Exception as e:
        print(f"Error connecting to AWS: {e}")

if __name__ == "__main__":
    get_local_security_groups()