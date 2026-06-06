
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_report(summary):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Analyze this automation test summary and give professional QA report:\n{summary}"
    response = model.generate_content(prompt)
    return response.text
