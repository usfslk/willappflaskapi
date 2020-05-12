# Youssef Selkani
# 2020

import os
from flask import Flask, render_template, url_for, json, jsonify
app = Flask(__name__)
import pyrebase


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


@app.route('/firebase')
def new_event():
    db.child("events").push('new_event')
    return render_template('test.html')


@app.route('/api/v1')
def main():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "data.json")
    data = json.load(open(json_url))
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
