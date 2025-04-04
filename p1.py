from flask import Flask
import os
import datetime
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    full_name = "Your Full Name"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME")
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    ist_time_str = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")
    
    # Run the 'top' command and get output
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <html>
        <head><title>/htop</title></head>
        <body>
            <h1>/htop Endpoint</h1>
            <p><b>Name:</b> {full_name}</p>
            <p><b>Username:</b> {username}</p>
            <p><b>Server Time (IST):</b> {ist_time_str}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
