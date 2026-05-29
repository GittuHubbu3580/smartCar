from flask import Flask, request, jsonify
import time
import serial
import threading
port = ''
ard = serial.Serial(port, 9600)
USvalue = 0;

app = Flask(__name__)

def getUSvalue():
    USvalue = ard.read_until('\n')

threading.Thread(target=getUSvalue).start()

@app.route('/dataSending', methods=["POST"])
def dataStuff():
    data = request.json
    command = data["com"]

    try:
        if(command == 'SFCforward'):
            ard.write(b'F\n')
            return jsonify({"response": "Command Sent"})

        elif(command == 'SFCbackward'):
            ard.write(b'B\n')
            return jsonify({"response": "Command Sent"})

        elif(command == 'SFCleft'):
            ard.write(b'L\n')
            return jsonify({"response": "Command Sent"})

        elif(command == 'SFCright'):
            ard.write(b'R\n')
            return jsonify({"response": "Command Sent"})

    except:
        print("Error Dude")
        return jsonify({"response": "An Error Has Occured"})


        

app.run(host='0.0.0.0', port=5000)

