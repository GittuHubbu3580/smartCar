from flask import Flask, request, jsonify
import time
import serial
import threading
port = '/dev/ttyACM0'
ard = serial.Serial(port, 9600)


app = Flask(__name__)

@app.route('/dataSending', methods=["POST"])
def dataStuff():
    data = request.json
    command = data["com"]

    try:
        if(command == 'SFCforward'):
            ard.write(b'F\n')
            return jsonify({"response": "Command Sent (Forward)"})

        elif(command == 'SFCbackward'):
            ard.write(b'B\n')
            return jsonify({"response": "Command Sent (Backward)"})

        elif(command == 'SFCleft'):
            ard.write(b'L\n')
            return jsonify({"response": "Command Sent (Left)"})

        elif(command == 'SFCright'):
            ard.write(b'R\n')
            return jsonify({"response": "Command Sent (Right)"})

        elif(command == 'SFCstop'):
            ard.write(b'S\n')
            return jsonify({"response": "Command Sent Stop"})

    except:
        print("Error Dude")
        return jsonify({"response": "An Error Has Occured"})


        

app.run(host='0.0.0.0', port=5000)