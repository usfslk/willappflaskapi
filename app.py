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


@app.route('/api/v2/update-room-name', methods=['POST'])
def updateRoomName():
    data = request.json.get('data')
    vendorIndex = request.json.get('vendorIndex')
    studioIndex = request.json.get('studioIndex')
    path = "vendors/" + vendorIndex + \
        "/faciltiy_studio_rooms/" + studioIndex + "/room_name"
    db.child("master").update({path: data})
    return jsonify({"code": 200, "data": data})


@app.route('/api/v2/update-room-number', methods=['POST'])
def updateRoomNumber():
    data = request.json.get('data')
    vendorIndex = request.json.get('vendorIndex')
    studioIndex = request.json.get('studioIndex')
    path = "vendors/" + vendorIndex + \
        "/faciltiy_studio_rooms/" + studioIndex + "/room_number"
    db.child("master").update({path: data})
    return jsonify({"code": 200, "data": data})


@app.route('/api/v2/update-room-type', methods=['POST'])
def updateRoomType():
    data = request.json.get('data')
    vendorIndex = request.json.get('vendorIndex')
    studioIndex = request.json.get('studioIndex')
    path = "vendors/" + vendorIndex + \
        "/faciltiy_studio_rooms/" + studioIndex + "/room_type"
    db.child("master").update({path: data})
    return jsonify({"code": 200, "data": data})


@app.route('/api/v2/update-room-dimensions', methods=['POST'])
def updateRoomDimensions():
    data = request.json.get('data')
    vendorIndex = request.json.get('vendorIndex')
    studioIndex = request.json.get('studioIndex')
    path = "vendors/" + vendorIndex + "/faciltiy_studio_rooms/" + \
        studioIndex + "/room_dimensions"
    db.child("master").update({path: data})
    return jsonify({"code": 200, "data": data})


@app.route('/api/v2/update-float', methods=['POST'])
def updateFloat():
    vendorIndex = request.json.get('vendorIndex')
    studioIndex = request.json.get('studioIndex')
    path = "vendors/" + vendorIndex + \
        "/faciltiy_studio_rooms/" + studioIndex + "/room_floated"
    db.child("master").update({path: True})
    path2 = "vendors/" + vendorIndex + \
        "/faciltiy_studio_rooms/" + studioIndex + "/room_isolated"
    db.child("master").update({path2: False})
    return jsonify({"code": 200})


@app.route('/api/v2/update-iso', methods=['POST'])
def updateIso():
    vendorIndex = request.json.get('vendorIndex')
    studioIndex = request.json.get('studioIndex')
    path = "vendors/" + vendorIndex + \
        "/faciltiy_studio_rooms/" + studioIndex + "/room_floated"
    db.child("master").update({path: False})
    path2 = "vendors/" + vendorIndex + \
        "/faciltiy_studio_rooms/" + studioIndex + "/room_isolated"
    db.child("master").update({path2: True})
    return jsonify({"code": 200})


@app.route('/api/v2/update-functions', methods=['POST'])
def updateFunctions():
    vendorIndex = request.json.get('vendorIndex')
    studioIndex = request.json.get('studioIndex')
    data = request.json.get('data')
    path = "vendors/" + vendorIndex + "/faciltiy_studio_rooms/" + \
        studioIndex + "/room_functions"
    db.child("master").update({path: data})
    return jsonify({"code": 200})

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

# --------------

@app.route('/api/v2/new-display', methods=['POST'])
def newDisplay():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    display = request.json.get('display')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_displays").push(display)
    return jsonify({"code": 200})

@app.route('/api/v2/new-console', methods=['POST'])
def newConsole():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    console = request.json.get('console')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_mixing_consoles").push(console)
    return jsonify({"code": 200})

@app.route('/api/v2/new-speaker', methods=['POST'])
def newSpeaker():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    speaker = request.json.get('speaker')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_speakers").push(speaker)
    return jsonify({"code": 200})

@app.route('/api/v2/new-micro', methods=['POST'])
def newMicro():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    micro = request.json.get('micro')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_microphones").push(micro)
    return jsonify({"code": 200})

# ----------------

@app.route('/api/v2/delete-display', methods=['POST'])
def deleteDisplay():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    key = request.json.get('key')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_displays").child(key).remove()
    return jsonify({"code": 200})

@app.route('/api/v2/delete-console', methods=['POST'])
def deleteConsole():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    key = request.json.get('key')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_mixing_consoles").child(key).remove()
    return jsonify({"code": 200})

@app.route('/api/v2/delete-speaker', methods=['POST'])
def deleteSpeaker():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    key = request.json.get('key')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_speakers").child(key).remove()
    return jsonify({"code": 200})

@app.route('/api/v2/delete-micro', methods=['POST'])
def deleteMicro():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    key = request.json.get('key')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_microphones").child(key).remove()
    return jsonify({"code": 200})

# ----------------

@app.route('/api/v2/new-workstation', methods=['POST'])
def newWT():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    wt = request.json.get('wt')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_workstations").push(wt)
    return jsonify({"code": 200})

@app.route('/api/v2/workstation-os', methods=['POST'])
def newOS():
    vendor = request.json.get('vendor')
    studio = request.json.get('studio')
    os = request.json.get('os')
    key = request.json.get('key')
    db.child("master/vendors/"+vendor+"/faciltiy_studio_rooms/" +
             studio+"/room_workstations/"+key+).update({workstation_hardware_os: os})
    return jsonify({"code": 200})

if __name__ == '__main__':
    app.run(debug=True)
