from flask import Flask, render_template_string, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)
DB = "incidents.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            severity TEXT,
            status TEXT DEFAULT 'Open',
            dateCreated TEXT,
            assignee TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("""
            INSERT INTO incidents (title, description, severity, dateCreated, assignee)
            VALUES (?, ?, ?, ?, ?)
        """, (
            request.form["title"],
            request.form["description"],
            request.form["severity"],
            date.today().isoformat(),
            request.form["assignee"]
        ))
        conn.commit()
        conn.close()
        return redirect("/")

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM incidents ORDER BY id DESC")
    incidents = c.fetchall()
    conn.close()

    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Company Incident Tracker</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            margin-top: 40px;
        }
        .badge-severity-low { background-color: #6c757d; }
        .badge-severity-medium { background-color: #0d6efd; }
        .badge-severity-high { background-color: #ffc107; color: #212529; }
        .badge-severity-critical { background-color: #dc3545; }
        .badge-status-open { background-color: #198754; }
        .badge-status-inprogress { background-color: #0dcaf0; color: #212529; }
        .badge-status-closed { background-color: #6c757d; }

        /* Table row colors based on severity */
        .row-low { background-color: #f8f9fa; }           /* light gray */
        .row-medium { background-color: #e7f1ff; }        /* light blue */
        .row-high { background-color: #fff3cd; }          /* light yellow */
        .row-critical { background-color: #f8d7da; }      /* light red */
    </style>
</head>
<body>
<div class="container">
    <h2 class="mb-4 text-center">Company Incident Tracker</h2>

    <div class="card mb-4 shadow-sm">
        <div class="card-body">
            <form method="post">
                <div class="mb-3">
                    <input name="title" placeholder="Title" class="form-control" required>
                </div>
                <div class="mb-3">
                    <textarea name="description" placeholder="Description" class="form-control" rows="3"></textarea>
                </div>
                <div class="mb-3">
                    <select name="severity" class="form-select">
                        <option>Low</option>
                        <option>Medium</option>
                        <option>High</option>
                        <option>Critical</option>
                    </select>
                </div>
                <div class="mb-3">
                    <input name="assignee" placeholder="Assignee" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Add Incident</button>
            </form>
        </div>
    </div>

    <h3>Incidents</h3>
    <div class="table-responsive">
        <table class="table table-hover align-middle shadow-sm bg-white">
            <thead class="table-light">
                <tr>
                    <th>ID</th><th>Title</th><th>Severity</th>
                    <th>Status</th><th>Date</th><th>Assignee</th>
                </tr>
            </thead>
            <tbody>
                {% for i in incidents %}
                {% set row_class = '' %}
                {% if i[3] == 'Low' %} {% set row_class = 'row-low' %}
                {% elif i[3] == 'Medium' %} {% set row_class = 'row-medium' %}
                {% elif i[3] == 'High' %} {% set row_class = 'row-high' %}
                {% elif i[3] == 'Critical' %} {% set row_class = 'row-critical' %}
                {% endif %}
                <tr class="{{ row_class }}">
                    <td>{{ i[0] }}</td>
                    <td>{{ i[1] }}</td>
                    <td>
                        {% if i[3] == 'Low' %}
                            <span class="badge badge-severity-low">Low</span>
                        {% elif i[3] == 'Medium' %}
                            <span class="badge badge-severity-medium">Medium</span>
                        {% elif i[3] == 'High' %}
                            <span class="badge badge-severity-high">High</span>
                        {% elif i[3] == 'Critical' %}
                            <span class="badge badge-severity-critical">Critical</span>
                        {% endif %}
                    </td>
                    <td>
                        {% if i[4] == 'Open' %}
                            <span class="badge badge-status-open">Open</span>
                        {% elif i[4] == 'In Progress' %}
                            <span class="badge badge-status-inprogress">In Progress</span>
                        {% elif i[4] == 'Closed' %}
                            <span class="badge badge-status-closed">Closed</span>
                        {% else %}
                            <span class="badge bg-secondary">{{ i[4] }}</span>
                        {% endif %}
                    </td>
                    <td>{{ i[5] }}</td>
                    <td>{{ i[6] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
</body>
</html>
""", incidents=incidents)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=42069)