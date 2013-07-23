"""
tipsy.py -- This is a Flask-based to-do list
"""
from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", user_name="Angie")

@app.route("/tasks")
def list_tasks():
    return render_template("list_tasks.html")

@app.route("/add-task")
def add_task():
    return render_template("add_task.html", user_id="user_id")

@app.route("/add-task-create")
def add_task_create():
    model.connect_to_db()
    title = request.args.get("title")
    user_id = request.args.get("user_id")
    created_at = request.args.get("datestamp")
    row = model.new_task(title, created_at, user_id)
    html = render_template("added_task.html")
    return html

if __name__ == "__main__":
    app.run(debug=True)