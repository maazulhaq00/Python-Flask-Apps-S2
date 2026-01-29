# A
### a
### b
# from A import a, b
# import A.a as abc


from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Abdul Muheet"
    # return f"<h3>Home!</h3><p>Welcome {name}</p>"
    return render_template("index.html", visiter_name=name)

@app.route("/about")
def aboutus():
    return render_template("about.html")

@app.route("/contact")
def contactus():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5003)
