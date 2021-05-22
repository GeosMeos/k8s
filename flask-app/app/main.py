import os
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def say_hello():
    hostname = os.uname()[1]
    return f"Hello from {hostname}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80, debug=True)