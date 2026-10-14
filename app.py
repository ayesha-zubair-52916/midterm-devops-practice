import os
from flask import Flask
app=Flask(__name__)
@app.route("/")
def home(): 
    return f"Hello {os.getenv('STUDENT_ROLL', 'UNKNOWN')}"

app.run(host="0.0.0.0", port=8000)