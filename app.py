from flask import Flask, request, redirect, url_for, jsonify, render_template_string


app = Flask(__name__)


tasks = []
next_id = 1


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Task Manager</title>
</head>
<body>
    <h1>DevOps Task Manager</h1>
    <form action="/tasks" method="POST">
        <input name="title" placeholder="Enter a task" required>
        <button type="submit">Add Task</button>
    </form>
    <ul>
    {% for task in tasks %}
        <li>
            {{ task.title }} - {{ "Completed" if task.completed else "Pending" }}
            {% if not task.completed %}
            <form action="/tasks/{{ task.id }}/complete" method="POST">
                <button type="submit">Complete</button>
            </form>
            {% endif %}
        </li>
    {% endfor %}
    </ul>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML, tasks=tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    global next_id
    title = request.form.get("title") or (request.json or {}).get("title")
    if not title:
        return jsonify({"error": "Task title is required"}), 400
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    next_id += 1
    if request.is_json:
        return jsonify(task), 201
    return redirect(url_for("home"))


@app.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    task["completed"] = True
    return redirect(url_for("home"))


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
