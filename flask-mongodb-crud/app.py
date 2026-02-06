# flask, pymongo
from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb://localhost:27017/")
db = client["lms_2306b1"]
students_collection = db["students"]

app = Flask(__name__)

@app.route("/")
def index():
    # logic to fetch data from mongodb collection

    students_list = list(students_collection.find())

    return render_template("index.html", 
                           students_list=students_list)

@app.route("/add-student", methods=["GET", "POST"])
def addStudent():

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        course = request.form['course']
        students_collection.insert_one({"name": name, 
                                        "email": email, 
                                        "contact": contact, 
                                        "course": course})
        return redirect(url_for("index"))

    return render_template("add-student.html")

@app.route("/delete-student/<id>")
def deleteStudent(id):
    students_collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

@app.route("/edit-student/<id>", methods=["GET", "POST"])
def editStudent(id):
    student = students_collection.find_one({"_id": ObjectId(id)})

    if request.method == "POST":
        updated_details = {
            "name": request.form['name'],
            "email": request.form['email'],
            "contact": request.form['contact'],
            "course": request.form['course'],
        }

        students_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_details})

        return redirect(url_for('index'))

    return render_template("edit-student.html", student=student)


# @app.route("/submit-student", methods=["POST"])
# def submitStudent():
#     name = request.form['name']
#     email = request.form['email']
#     contact = request.form['contact']
#     course = request.form['course']
#     students_collection.insert_one({"name": name, 
#                                     "email": email, 
#                                     "contact": contact, 
#                                     "course": course})
#     return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True, port=5001)