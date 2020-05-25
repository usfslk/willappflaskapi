# Youssef Selkani
# 2020

from flask import Flask, render_template, url_for, json, jsonify, request
import os
import pyrebase

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
storage = firebase.storage()


@app.route('/')
def main():
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


@app.route('/api/v2/restore')
def restoreDB():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "data.json")
    data = json.load(open(json_url))
    db.child("master").update({"vendors": data})
    return jsonify({"code": 200, "message": "ok"})


@app.route('/api/v2/upload-vendor', methods=['POST'])
def uploadVendor():
    vendor = request.json.get('vendor')
    url = request.json.get('url')
    db.child("master/vendors/"+vendor+"/photos").push({"url": url})
    return jsonify({"code": 200})

@app.route('/api/v2/upload-studio', methods=['POST'])
def uploadStudio():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    url = request.json.get('url')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/photos").push({"url": url})
    return jsonify({"code": 200})

if __name__ == '__main__':
    app.run(debug=True)
