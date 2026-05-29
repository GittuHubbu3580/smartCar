from flask import Flask, request, jsonify
import time
import serial
port = ''
ard = serial.Serial(port, 9600)

app = Flask(__name__)

@app.route('/dataSending', methods=["POST"])
def dataStuff():
    data = request.json
    command = data["com"]

    try:
        if(command == 'SFCforward'):
            ard.write(b'F')
            return jsonify({"response": "Command Sent"})

        if(command == 'SFCbackward'):
            ard.write(b'B')
            return jsonify({"response": "Command Sent"})

        if(command == 'SFCleft'):
            ard.write(b'L')
            return jsonify({"response": "Command Sent"})

        if(command == 'SFCright'):
            ard.write(b'R')
            return jsonify({"response": "Command Sent"})

    except:
        print("Error Dude")
        return jsonify({"response": "An Error Has Occured"})


        

app.run(host='0.0.0.0', port=5000)

