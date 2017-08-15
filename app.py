from flask import Flask, render_template
from random import random
app = Flask(__name__)

@app.route("/")
def index():
    instructors = ["Elie", "Matt", "Tim"]
    number = random()
    return render_template("index.html", number=number, instructors=instructors)

@app.route("/about/<name>")
def about(name):
    return render_template("about.html", name=name)

@app.route("/foo")
def foo():
    return render_template("foo.html")
    
if __name__ == "__main__":
    app.run(debug=True)