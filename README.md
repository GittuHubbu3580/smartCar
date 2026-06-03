# 🚗 SmartCar

A Raspberry Pi and Arduino powered smart robot car controlled over a local network using Python, Flask, OpenCV, and Serial Communication.

The project allows a client device to remotely control a robotic vehicle while receiving a live video stream from an onboard camera.

---

## ✨ Features

* 🌐 Remote control over local Wi-Fi network
* ⌨️ WASD keyboard controls
* 📷 Live camera streaming using OpenCV
* 🔄 Raspberry Pi ↔ Arduino serial communication
* ⚡ Flask-powered control server
* 🚗 Forward, Backward, Left, Right, and Stop controls
* 🧩 Easily expandable for sensors and autonomous features
* 🤖 Designed for future obstacle avoidance and computer vision projects

---

## 🏗️ System Architecture

```text
Client Device
(Laptop/Desktop)
        │
        ▼
HTTP Requests
        │
        ▼
Raspberry Pi
(Flask Server)
        │
        ▼
USB Serial Communication
        │
        ▼
Arduino
        │
        ▼
L298N Motor Driver
        │
        ▼
TT Motors
```

---

## 📂 Project Structure

```text
SmartCar/
│
├── client.py
│   └── Keyboard control client
│
├── raspiCode.py
│   └── Flask server, video streaming, serial communication
│
├── main.cpp
│   └── Arduino motor control code
│
├── requirements.txt
│   └── Python dependencies
│
└── README.md
```

---

## 🔧 Hardware Used

| Component          | Purpose                    |
| ------------------ | -------------------------- |
| Raspberry Pi       | Main server and networking |
| Arduino UNO/Nano   | Motor controller           |
| L298N Motor Driver | Drives motors              |
| TT Motors          | Vehicle movement           |
| USB Webcam         | Live video feed            |
| Battery Pack       | Power source               |
| Robot Chassis      | Vehicle frame              |

---

## 🎮 Controls

| Key         | Action        |
| ----------- | ------------- |
| W           | Move Forward  |
| A           | Turn Left     |
| S           | Move Backward |
| D           | Turn Right    |
| Release Key | Stop          |

---

## 📹 Live Video Streaming

The Raspberry Pi captures frames using OpenCV and streams them through Flask.

Video Stream URL:

```text
http://RASPBERRY_PI_IP:5000/stream
```

Example:

```text
http://192.168.1.25:5000/stream
```

Open the URL in any browser connected to the same network.

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/GittuHubbu3580/smartCar.git
cd smartCar
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Setup

### 1. Upload Arduino Code

Upload `main.cpp` to your Arduino using the Arduino IDE.

---

### 2. Connect Arduino to Raspberry Pi

Connect the Arduino via USB.

Check the serial port:

```bash
ls /dev/tty*
```

Update the port if necessary:

```python
port = "/dev/ttyACM0"
```

---

### 3. Connect Webcam

Check available cameras:

```bash
v4l2-ctl --list-devices
```

Update if needed:

```python
webcam = cv2.VideoCapture("/dev/video0")
```

---

### 4. Start the Flask Server

```bash
python3 raspiCode.py
```

The server will start on:

```text
http://0.0.0.0:5000
```

---

### 5. Configure Client

Open `client.py` and set:

```python
serverIP = "192.168.1.25:5000"
```

Replace with your Raspberry Pi's IP address.

---

### 6. Run the Client

```bash
python3 client.py
```

Use:

```text
W A S D
```

to control the vehicle.

---

## 📡 API Endpoints

### Send Movement Commands

```http
POST /dataSending
```

Example Request:

```json
{
    "com": "SFCforward"
}
```

Available Commands:

```text
SFCforward
SFCbackward
SFCleft
SFCright
SFCstop
```

---

### Video Stream

```http
GET /stream
```

Returns an MJPEG video stream.

---

## 🔮 Future Improvements

* 📏 Ultrasonic obstacle detection
* 🛑 Automatic emergency braking
* 🤖 Autonomous navigation
* 📍 GPS integration
* 🎮 Mobile application
* 🧠 Object detection using OpenCV
* 🗺️ Mapping and path planning
* 🎤 Voice control

---

## 🛠️ Troubleshooting

### Car Not Moving

* Check battery voltage
* Verify motor driver wiring
* Confirm Arduino connection
* Verify serial port configuration

### Client Cannot Connect

* Verify Raspberry Pi IP address
* Ensure Flask server is running
* Confirm both devices are on the same network

### Video Stream Not Working

* Verify camera connection
* Check camera device path
* Confirm OpenCV detects the webcam

---

## 📚 Technologies Used

* Python
* Flask
* OpenCV
* Requests
* PySerial
* Arduino C++
* Raspberry Pi OS

---

## 👨‍💻 Author

Created by **Shravan** as a robotics, networking, and computer vision learning project.

This project helped me learn:

* Embedded Systems
* Python Networking
* Computer Vision
* Raspberry Pi Development
* Arduino Programming

---

## ⭐ Support

If you found this project interesting, consider giving it a star.

It helps others discover the project and motivates future development.

---

## 📜 License

This project is open-source and available for educational purposes.

Feel free to modify, improve, and learn from it.

---

Made with ☕ Python, Flask, OpenCV, Arduino, Raspberry Pi, and many hours of debugging.

# DISCLAIMER!
 These programs were fully codes by me, and may not work for all. I'm still learning