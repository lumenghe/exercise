from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Hehe !"


@app.route("/<name>")
def hi(name: str):
    return f"Hi, {name} !"


@app.get("/login_test")
def login_get():
    return "LOGIN GET"


@app.post("/login_test")
def login_post():
    return "LOGIN POST"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "POST"
    else:
        return "GET"


if __name__ == "__main__":
    app.run()
