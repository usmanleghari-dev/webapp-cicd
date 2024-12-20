from flask import render_template, request, redirect, url_for
from app import app, mongo

@app.route("/")
def index():
    tasks = mongo.db.tasks.find()
    return render_template("index.html", tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    task = request.form.get("task")
    mongo.db.tasks.insert_one({"task": task, "completed": False})
    return redirect(url_for("index"))
