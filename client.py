import requests
import tkinter as tk
url = http://192.168.86.46:5000/dataSending

window = tk.Tk()
window.title("FlaskControlPanel")
window.geometry('500x500')

def sendForward():
    data = {"com": "SFCforward"} #SFC means Sent From Client :)
    comms = requests.post(url, json=data)
    recvmssg = comms.json
    actualMssg = recvmssg["mssg"]
    print(actualMssg)

def sendBackward():
    data = {"com": "SFCbackward"} #SFC means Sent From Client :)
    comms = requests.post(url, json=data)
    recvmssg = comms.json
    actualMssg = recvmssg["mssg"]
    print(actualMssg)

def sendLeft():
    data = {"com": "SFCleft"} #SFC means Sent From Client :)
    comms = requests.post(url, json=data)
    recvmssg = comms.json
    actualMssg = recvmssg["mssg"]
    print(actualMssg)

def sendRight():
    data = {"com": "SFCright"} #SFC means Sent From Client :)
    comms = requests.post(url, json=data)
    recvmssg = comms.json
    actualMssg = recvmssg["mssg"]
    print(actualMssg)


forwardButton = tk.Button(window, text="Forward", command=lambda:sendForward)
backwardButton = tk.Button(window, text="Backward", command=lambda:sendBackward)
leftButton = tk.Button(window, text="Left", command=lambda:sendLeft)
rightButton = tk.Button(window, text="right", command=lambda:sendRight)

forwardButton.grid(row=0, column=1, padx=5, pady=5)
leftButton.grid(row=1, column=0, padx=5, pady=5)
rightButton.grid(row=1, column=2, padx=5, pady=5)
backwardButton.grid(row=4, column=1, padx=5, pady=5)

window.mainloop()