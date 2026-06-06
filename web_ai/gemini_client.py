from google import genai
import os

# Use environment variable or replace with your key
client = genai.Client(api_key="AIzaSyBvz46-7MNLz7aGjubzpbBxDtZFMTyxKss")

def get_ai_analysis(error_details):
    prompt = f"""You are an expert QA Automation Architect.

                Analyze the following API test execution results.
                
                Provide:
                1. Root cause of failure
                2. Fix recommendation
                3. Test improvement suggestions
                4. Risk analysis
                5. Summary:\n{error_details}"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Analysis failed: {str(e)}"