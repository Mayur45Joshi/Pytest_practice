from jinja2 import Template
import os

def generate_report(summary, ai_summary):
    os.makedirs("reports", exist_ok=True)

    html = Template("""
    <html>
    <head>
    <title>AI Test Report Analysis</title>
    <style>
    body{font-family:Arial;padding:20px;}
    .box{padding:15px;border:1px solid #ccc;border-radius:8px;margin-bottom:15px;}
    </style>
    </head>
    <body>
    <h1>AI Test Report Analysis</h1>

    <div class="box">
    <b>Total:</b> {{total}} <br>
    <b>Passed:</b> {{passed}} ({{pass_percent}}%) <br>
    <b>Failed:</b> {{failed}} ({{fail_percent}}%) <br>
    </div>

    <div class="box">
    <h3>Failure Details</h3>
    {% for f in failures %}
    <p><b>{{f.test}}</b>: {{f.error}}</p>
    {% endfor %}
    </div>

    <div class="box">
    <h3>Gemini AI Analysis Summary</h3>
    <pre>{{ai_summary}}</pre>
    </div>

    </body>
    </html>
    """)

    content = html.render(**summary, ai_summary=ai_summary)

    with open("reports/report.html", "w", encoding="utf-8") as f:
        f.write(content)
