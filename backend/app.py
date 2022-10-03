from flask import Flask
from threading import Thread
import os
import subprocess


app = Flask(__name__)

curf = 0
p = 0

tc = 0
@app.before_first_request
def activate_job():
    global tc
    tc = 0

@app.route('/startfreq/<f>')
def startfreq(f):
    global curf
    global p
    print(f)
    curf = f
    p = subprocess.Popen(["beep", "-f", f, "-l", "100000"]).pid
    return("200")

@app.route('/stopfreq/<f>')
def stopfreq(f):
    print(f, curf)
    if f == curf:
        os.kill(p, 15)
    return("200")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

