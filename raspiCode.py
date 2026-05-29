from flask import Flask, request, json
import time


app = Flask(__name__)

@app.route('/dataSending', methods=["POST"])
def dataStuff():
    data = request.json
    command = data["com"]


app.run(host='0.0.0.0', port=5000)
