# Youssef Selkani
# 2020

import pyrebase
import os
from flask import Flask, render_template, url_for, json, jsonify, request
app = Flask(__name__)


config = {
    "apiKey": "AIzaSyA4SoLI5vW5U2q6AtKAX1XXZYEhyH2qSJE",
    "authDomain": "willapp-3ac45.firebaseapp.com",
    "databaseURL": "https://willapp-3ac45.firebaseio.com",
    "projectId": "willapp-3ac45",
    "storageBucket": "willapp-3ac45.appspot.com",
    "messagingSenderId": "712668492803",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v2/update', methods=['POST'])
def updateDB():
    data = request.json.get('data')
    db.child("master").update({"vendors": data})
    return jsonify({"code": 200, "data": data})


@app.route('/api/v2/pull')
def pullDB():
    vendors = db.child("master").get()
    return jsonify({"code": 200, "data": vendors.val()})


if __name__ == '__main__':
    app.run(debug=True)
