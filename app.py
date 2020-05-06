# Youssef Selkani
# 2020

import os
from flask import Flask, render_template, url_for, json, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1')
def main():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "data.json")
    data = json.load(open(json_url))
    return jsonify(data)

if __name__ == '__main__': app.run(debug=True)