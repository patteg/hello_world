from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "to be or not to be"


if __name__ == "__main__":
    app.run()
