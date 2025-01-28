from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/test/<int:value1>/<int:value2>")
def test(value1, value2):
    return f"<p>Answer is: {value1**2+value2**2}</p>"


