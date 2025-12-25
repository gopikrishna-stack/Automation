from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevSecOps"

@app.route("/cmd")
def cmd():
    command = request.args.get("cmd")
    return os.popen(command).read()

app.run(host="0.0.0.0", port=5000)
