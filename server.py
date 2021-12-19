import json
from os import lockf
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import client
import hashlib
import socket,sys,threading,unittest

SERVER = "localhost:5000"
JSON_CONTENT_TYPE = "application/json; charset=UTF-8"

app = Flask(__name__)
exe_id = ""

HOST = "time-a-g.nist.gov"
PORT = 5000
lock = threading.Lock()


def get_daytime(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(1024)
    return data.decode('utf-8').strip()


@app.route("/query/<name:string>",methods=["GET"])
def query(name):
    data = json.loads(request.data)
    for i,item in enumerate():
        if item["name"] == name:
            return i
            break
    return jsonify({"error": "todo item not found"}), 404


@app.route("/buy/<name:string>/<quantity:int>",method =["POST"])
def buy(name,quantity):
    data = json.loads(request.data)
    for i,item in enumerate():
        if item["name"] == name:
            if (quantity<=item["quantity"]):
                finalprice = item["price"]*quantity
                item["quantity"] -= quantity
                return finalprice
            else: return jsonify({"error": "quantity exceed"},404)    
                

@app.route("/replenish/<name:string>/<quantity:int>",method=["POST"])
def replenish(name,quantity):
    data = json.loads(request.data)
    for i,item in enumerate():
        if item["name"] == name:
            item["quantity"] += quantity
            return item["quantity"]
        else: return jsonify({"error": "todo item not found"},404)
    




if __name__ == "__main__":
    a_string = get_daytime(HOST,PORT)
    exe_id = hashlib.sha256(a_string.encode("utf-8")).hexdigest()  
    app.run()
    