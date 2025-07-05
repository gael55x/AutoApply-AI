import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_email(company, role):
    """Generate a cold email for job application"""
    
    prompt = f"""Write a short, professional cold email for a job application.

Company: {company}
Role: {role}

Make it personal and engaging, around 3-4 sentences."""
    
    # Use Gemini Pro model
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    return response.text

# Test it out
if __name__ == "__main__":
    # Generate an email
    result = generate_email("Google", "Software Engineer")
    
    print("Generated Email:")
    print("-" * 40)
    print(result)
