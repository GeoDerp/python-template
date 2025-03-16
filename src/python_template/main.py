import logging

from flask import Flask, render_template
from waitress import serve

app = Flask(__name__, template_folder="templates")


@app.route("/")
@app.route("/index")
def index() -> str:
    return "hi"


@app.route("/hello")
def hello() -> str:
    return render_template("hello.html")


def main() -> None:
    app.logger.setLevel(logging.DEBUG)
    serve(app, host="0.0.0.0", port=8080, threads=8)


if __name__ == "__main__":
    main()
