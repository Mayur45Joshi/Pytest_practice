import json
from analysis import analyze_results
from report_generator import generate_report

if __name__ == "__main__":
    with open("sample_results.json") as f:
        data = json.load(f)

    summary, ai_summary = analyze_results(data)
    generate_report(summary, ai_summary)
    print("HTML Report generated in reports/report.html")
