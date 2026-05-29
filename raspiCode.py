from flask import Flask, request, json
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

        if(command == 'SFCbackward'):
            ard.write(b'B')

        if(command == 'SFCleft'):
            ard.write(b'L')

        if(command == 'SFCright'):
            ard.write(b'R')

    except:
        print("Error Dude")
        return jsonify({"response": "An Error Has Occured"})


        

app.run(host='0.0.0.0', port=5000)

