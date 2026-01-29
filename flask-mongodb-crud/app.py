# flask, pymongo

from flask import Flask, render_template
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["lms_2306b1"]
students_collection = db["students"]


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-student")
def hello_world():
    return render_template("add-student.html")



if __name__ == "__main__":
    app.run(debug=True, port=5001)