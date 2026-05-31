import requests
import tkinter as tk
import keyboard
serverIP = 'http://192.168.86.53:5000'
url = f"{serverIP}/dataSending"

window = tk.Tk()
window.title("FlaskControlPanel")
window.geometry('500x500')

def sendForward():
    try:
        data = {"com": "SFCforward"} #SFC means Sent From Client :)
        comms = requests.post(url, json=data)
        recvmssg = comms.json()
        actualMssg = recvmssg["response"]
        responseLabel.config(text=actualMssg)
        
    except:
        responseLabel.config(text="the json Data did not get sent (SFCforward)")
def sendBackward():
    try:
        data = {"com": "SFCbackward"} #SFC means Sent From Client :)
        comms = requests.post(url, json=data)
        recvmssg = comms.json()
        actualMssg = recvmssg["response"]
        responseLabel.config(text=actualMssg)

    except:
        responseLabel.config(text="the json Data did not get sent (SFCbackward)")

def sendLeft():
    try:
        data = {"com": "SFCleft"} #SFC means Sent From Client :)
        comms = requests.post(url, json=data)
        recvmssg = comms.json()
        actualMssg = recvmssg["response"]
        responseLabel.config(text=actualMssg)

    except:
        responseLabel.config(text="the json Data did not get sent (SFCleft)")

def sendRight():
    try:
        data = {"com": "SFCright"} #SFC means Sent From Client :)
        comms = requests.post(url, json=data)
        recvmssg = comms.json()
        actualMssg = recvmssg["response"]
        responseLabel.config(text=actualMssg)

    except:
        responseLabel.config(text="the json Data did not get sent (SFCright)")

def stop():
    data = {"com": "SFCstop"}
    comms = requests.post(url, json=data)
    recvmssg = comms.json()
    actualMssg = recvmssg["response"]
    responseLabel.config(text=actualMssg)



forwardButton = tk.Button(window, text="Forward", command=lambda:sendForward())
backwardButton = tk.Button(window, text="Backward", command=lambda:sendBackward())
leftButton = tk.Button(window, text="Left", command=lambda:sendLeft())
rightButton = tk.Button(window, text="right", command=lambda:sendRight())
responseLabel = tk.Label(window, text="!@#YET TO RECEIVE#@!")
stopButton = tk.Button(window, text="STOP", command=lambda:stop())

forwardButton.grid(row=0, column=1)
leftButton.grid(row=1, column=0)
rightButton.grid(row=1, column=2)
backwardButton.grid(row=4, column=1)
stopButton.grid(row=5, column=1)
responseLabel.grid(row=7, column=1)

window.mainloop() 