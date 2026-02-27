from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return "available endpoints: /ping, /system-info, /home"
@app.route("/ping")
def ping():
    return "pong"
@app.route("/system-info")
def system_info():
    info = subprocess.run(["cat", "/etc/os-release"], capture_output=True, text=True)
    return f"System Info: {info.stdout}"
@app.route("/home")
def home():
    return "test"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)