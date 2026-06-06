import google.generativeai as genai
import os

def analyze_results(data):
    total = data['total']
    passed = data['passed']
    failed = data['failed']
    percent_pass = (passed/total)*100
    percent_fail = (failed/total)*100

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""Analyze test report:
    Total: {total}
    Passed: {passed}
    Failed: {failed}
    Failures: {data['failures']}

    Give QA summary, risk analysis, and improvement suggestions.
    """

    response = model.generate_content(prompt)

    summary = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_percent": round(percent_pass,2),
        "fail_percent": round(percent_fail,2),
        "failures": data['failures']
    }

    return summary, response.text
