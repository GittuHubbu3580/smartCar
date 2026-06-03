from flask import Flask, request, jsonify, Response
import time
import serial
import threading
import cv2

webcam = cv2.VideoCapture('/dev/video0') #Insert the video device inside the parentheses if it differs on your Pi.
webcam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
port = '/dev/ttyACM0' #The port at which the Arduino is Connected to on the Raspberry PI...
ard = serial.Serial(port, 9600)
app = Flask(__name__)

def generate_frames():
    while True:
        ret, frame = webcam.read()
        frame = cv2.flip(frame, 1)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield(
             b'--frame\r\n'
             b'Content-Type: image/jpeg\r\n\r\n'
             + frame_bytes +
            b'\r\n'
        )

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

@app.route('/stream')
def video():
    ret, frame = webcam.read()

    if ret:
        return Response(
            generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame'
        )
    elif not ret:
        return "No Camera was Detected"

app.run(host='0.0.0.0', port=5000)
