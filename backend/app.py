from flask import Flask
from threading import Thread
import os
import subprocess


app = Flask(__name__)

threadFlag = True
def playFunction(freq):
    global threadFlag
    p = subprocess.Popen(["beep", "-f", freq, "-l", "100000"])
    while not threadFlag:
        pass
        #print("beep -f %f" % (freq))
    os.kill(p.pid, 15)

thread2 = 0
tc = 0
@app.before_first_request
def activate_job():
    global tc
    tc = 0

@app.route('/startfreq/<freq>')
def freq(freq):
    global threadFlag
    global thread2
    threadFlag = False
    print(freq)
    thread2 = Thread(target=playFunction, args=(freq,))
    thread2.start()
    return("200")

@app.route('/stopfreq/<freq2>')
def freq2(freq2):
    global threadFlag
    global thread2
    threadFlag = True
    return("200")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



