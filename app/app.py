from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/run")
def run_cmd():
    cmd = request.args.get("cmd")
    # ❌ HIGH: Command Injection
    return os.popen(cmd).read()

app.run(host="0.0.0.0", port=5000)
