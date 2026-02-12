from flask import Flask, render_template, request
from ai_engine import analyze_log_with_ai
from log_parser import parse_log_file

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    ai_response = None
    log_summary = None

    if request.method == "POST":
        file = request.files["logfile"]

        if file:
            log_content, log_summary = parse_log_file(file)
            ai_response = analyze_log_with_ai(log_content)

    return render_template(
        "index.html",
        ai_response=ai_response,
        log_summary=log_summary
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

