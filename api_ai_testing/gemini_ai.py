from google import genai

client = genai.Client(api_key="AIzaSyBvz46-7MNLz7aGjubzpbBxDtZFMTyxKss")

def analyze_report(test_results):

    prompt = f"""
You are an expert QA Automation Architect.

Analyze the following API test execution results.

Provide:
1. Root cause of failure
2. Fix recommendation
3. Test improvement suggestions
4. Risk analysis
5. Summary

Test Results:
{test_results}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# for model in client.models.list():
#     print(f"Model ID: {model.name}")