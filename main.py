import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_email(company, role, contact_name=""):
    """Generate a cold email for job application"""
    
    contact_greeting = f"Dear {contact_name}," if contact_name else f"Dear {company} Team,"
    
    prompt = f"""Write a professional cold email for a job application.

Company: {company}
Role: {role}
Contact: {contact_greeting}

Make it personal, engaging, and around 3-4 sentences. Include a subject line."""
    
    # Use Gemini Pro model
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    return response.text

# Test it out
if __name__ == "__main__":
    # Try reading from leads CSV
    try:
        import pandas as pd
        leads = pd.read_csv('profiles/leads.csv')
        
        print("Found leads:")
        for _, lead in leads.iterrows():
            print(f"- {lead['company']}: {lead['role']} ({lead['contact_name']})")
        
        # Generate email for first lead
        first_lead = leads.iloc[0]
        result = generate_email(
            first_lead['company'], 
            first_lead['role'], 
            first_lead['contact_name']
        )
        
        print(f"\nGenerated Email for {first_lead['company']}:")
        print("-" * 50)
        print(result)
        
    except FileNotFoundError:
        # Fallback to manual example
        result = generate_email("Google", "Software Engineer")
        print("Generated Email:")
        print("-" * 40)
        print(result)
