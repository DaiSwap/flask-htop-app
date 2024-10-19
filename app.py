from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(_name_)

@app.route('/htop')
def htop():
    # Full name
    full_name = "Your Full Name"

    # Username (system username)
    username = os.getlogin()

    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    # top command output
    top_output = subprocess.getoutput('top -bn1')

    # HTML Output
    return f"""
    <h1>HTOP Information</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
