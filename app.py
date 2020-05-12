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


@app.route('/update', methods=['GET', 'POST'])
def updateDB():
    data = request.form.get('data')
    # db.child("master").update({"vendors": data})
    return jsonify({"code": 200, "data": data})


@app.route('/pull')
def pullDB():
    vendors = db.child("master").get()
    return jsonify({"code": 200, "data": vendors.val()})


@app.route('/api/v1')
def main():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "data.json")
    data = json.load(open(json_url))
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
