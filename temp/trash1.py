import json
from os import lockf
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
# import client
import hashlib
import socket,sys,threading,unittest

SERVER = "localhost:5000"
JSON_CONTENT_TYPE = "application/json; charset=UTF-8"

app = Flask(__name__)
exe_id = ""

HOST = "time-b-b.nist.gov"
PORT = 13
lock = threading.Lock()

def obtain():
    global HOST, PORT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        time = sock.recv(1024)
    time = time.decode("utf-8").strip()
    exe_id = hashlib.sha256(time.encode("utf-8")).hexdigest()
    return exe_id


if __name__ == "__main__":
    a_string = obtain()
    # exe_id = hashlib.sha256(a_string.encode("utf-8")).hexdigest()  
    print(obtain())
    app.run()
    