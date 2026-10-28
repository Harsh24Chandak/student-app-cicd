from datetime import datetime, timezone
from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)
STUDENTS = []                       # in-memory store (kept simple for the DevOps demo)
START = datetime.now(timezone.utc)
REQUESTS = {"count": 0}


@app.before_request
def count_requests():
    REQUESTS["count"] += 1


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        roll = request.form.get("roll", "").strip()
        if name and roll:
            STUDENTS.append({"name": name, "roll": roll})
        return redirect(url_for("index"))
    return render_template("index.html", students=STUDENTS)


@app.route("/api/students")
def api_students():
    return jsonify(STUDENTS)


@app.route("/health")
def health():
    uptime = int((datetime.now(timezone.utc) - START).total_seconds())
    return jsonify(status="UP", uptime_seconds=uptime)


@app.route("/metrics")
def metrics():
    return jsonify(total_requests=REQUESTS["count"], registered_students=len(STUDENTS))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
