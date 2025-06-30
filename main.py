import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub

# Load environment variables
load_dotenv()

# Initialize LangChain's Hugging Face LLM (free!)
llm = HuggingFaceHub(
    repo_id="microsoft/DialoGPT-medium",
    model_kwargs={"temperature": 0.7, "max_length": 200}
)

# Create a LangChain prompt template
prompt_template = PromptTemplate(
    input_variables=["company", "role"],
    template="""Write a short, professional cold email for a job application.

Company: {company}
Role: {role}

Make it personal and engaging, around 3-4 sentences."""
)

def generate_email(company, role):
    # Create the LangChain chain
    chain = prompt_template | llm
    
    # Invoke the chain
    response = chain.invoke({"company": company, "role": role})
    
    return response

# Test it out
if __name__ == "__main__":
    # Generate an email
    result = generate_email("Google", "Software Engineer")
    
    print("Generated Email:")
    print("-" * 40)
    print(result)
