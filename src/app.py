from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "this is my main site"


if __name__ == "__main__":
    app.run()
