import requests
from pynput import keyboard
import time
serverIP = 'http://192.168.86.53:5000'
url = f"{serverIP}/dataSending"
current_key = None

def sendForward():
    try:
        data = {"com": "SFCforward"} #SFC means Sent From Client :)
        comms = requests.post(url, json=data)
        recvmssg = comms.json()
        actualMssg = recvmssg["response"]
        print(actualMssg)
        
    except:
        print("the json Data did not get sent (SFCforward)")
def sendBackward():
    try:
        data = {"com": "SFCbackward"} #SFC means Sent From Client :)
        comms = requests.post(url, json=data)
        recvmssg = comms.json()
        actualMssg = recvmssg["response"]
        print(actualMssg)

    except:
        print("the json Data did not get sent (SFCbackward)")

def sendLeft():
    try:
        data = {"com": "SFCleft"} #SFC means Sent From Client :)
        comms = requests.post(url, json=data)
        recvmssg = comms.json()
        actualMssg = recvmssg["response"]
        print(actualMssg)

    except:
        print("the json Data did not get sent (SFCleft)")

def sendRight():
    try:
        data = {"com": "SFCright"} #SFC means Sent From Client :)
        comms = requests.post(url, json=data)
        recvmssg = comms.json()
        actualMssg = recvmssg["response"]
        print(actualMssg)

    except:
        print("the json Data did not get sent (SFCright)")

def stop():
    try:
        data = {"com": "SFCstop"}
        comms = requests.post(url, json=data)
        recvmssg = comms.json()
        actualMssg = recvmssg["response"]
        print(actualMssg)

    except:
        print("the json Data did not get sent (SFCstop)")

def on_press(key):
    global current_key

    try:
        if key.char == current_key:
            return

        current_key = key.char

        if key.char == "w":
            sendForward()

        elif key.char == "s":
            sendBackward()

        elif key.char == "a":
            sendLeft()

        elif key.char == "d":
            sendRight()

    except AttributeError:
        pass


def on_release(key):
    global current_key

    try:
        if key.char in ["w", "a", "s", "d"]:
            current_key = None
            stop()

    except AttributeError:
        pass
    
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:

    listener.join()