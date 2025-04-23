import sqlite3
from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('quotes.db') 
    cur = conn.cursor()
    qnum = cur.execute("SELECT COUNT(id) FROM quotes;")
    num = int(qnum.fetchone()[0])
    N = random.randint(1, num)
    cur.execute("SELECT phrase, author FROM quotes WHERE id = ?" , (N, ))
    rows = cur.fetchall()
    phrases = [row[0] for row in rows]
    authors = [row[1] for row in rows]
    phrase = phrases[0]
    author = authors[0]

    connect = sqlite3.connect('tasks.db')
    current = connect.cursor()
    current.execute("SELECT id, task, time, importance FROM tasks;")
    rows_db = current.fetchall()

    return render_template("home.html", phrase=phrase, author=author, tasks=rows_db)
    

@app.route("/tasks.html", methods=["GET", "POST"])
def tasks():
    if request.method == "GET":
        return render_template("tasks.html") 
       
    else:
        task = request.form.get("task")
        time = request.form.get("time")
        importance = request.form.get("importance")

        connect = sqlite3.connect('tasks.db')
        current = connect.cursor()
        current.execute("INSERT INTO tasks(task, time, importance) VALUES (?, ?, ?)", (task, time, importance))
        connect.commit()
        
        return redirect("/tasks.html")


@app.route("/", methods=["POST"])
def home():
    task_id = request.form.get('id')
    if task_id:
        connect = sqlite3.connect('tasks.db')
        current = connect.cursor()
        current.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        connect.commit()

        current.execute("SELECT * FROM tasks")
        tasks = current.fetchall()

        # Fetch a new phrase and author
        conn = sqlite3.connect('quotes.db') 
        cur = conn.cursor()
        qnum = cur.execute("SELECT COUNT(id) FROM quotes;")
        num = int(qnum.fetchone()[0])
        N = random.randint(1, num)
        cur.execute("SELECT phrase, author FROM quotes WHERE id = ?" , (N, ))
        rows = cur.fetchall()
        phrase = rows[0][0]
        author = rows[0][1]

        return render_template("/home.html", tasks=tasks, phrase=phrase, author=author)  
        
@app.route("/suggest.html")
def suggest():
    return render_template("suggest.html")
    