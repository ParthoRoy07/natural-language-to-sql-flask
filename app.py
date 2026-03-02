
from flask import Flask, render_template, request
import sqlite3
import pandas as pd

app = Flask(__name__)

def nl_to_sql(query):
    query = query.lower()

    if "all students" in query:
        return "SELECT * FROM students"
    elif "cse" in query:
        return "SELECT * FROM students WHERE branch='CSE'"
    elif "ece" in query:
        return "SELECT * FROM students WHERE branch='ECE'"
    elif "marks greater than 80" in query or "marks > 80" in query:
        return "SELECT * FROM students WHERE marks > 80"
    elif "highest marks" in query:
        return "SELECT * FROM students ORDER BY marks DESC LIMIT 1"
    else:
        return "SELECT * FROM students"

def run_query(sql):
    conn = sqlite3.connect("students.db")
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

@app.route("/", methods=["GET","POST"])
def index():
    table = None
    sql = ""

    if request.method == "POST":
        question = request.form["query"]
        sql = nl_to_sql(question)
        result = run_query(sql)
        table = result.to_html(classes="table", index=False)

    return render_template("index.html", table=table, sql=sql)

if __name__ == "__main__":
    app.run(debug=True)
