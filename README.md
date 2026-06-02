# SmartCar 🚗🤖

A Raspberry Pi + Arduino powered smart robot car controlled over a local network using Python, Flask, serial communication, and keyboard input.

This project allows you to control a robotic car remotely from another device on the same network using **WASD controls**. Commands are sent from a client device → Raspberry Pi Flask server → Arduino → Motor Driver → Motors.

---

## Features ✨

* 🌐 Remote control over local network
* ⌨️ Keyboard-based driving (`W`, `A`, `S`, `D`)
* 🔄 Raspberry Pi ↔ Arduino serial communication
* ⚡ Flask-powered API server
* 🚗 Motor movement control (Forward, Backward, Left, Right, Stop)
* 🧩 Modular architecture for adding sensors and computer vision later

---

## How It Works 🛠️

The system works in 3 stages:

1. **Client Device (`client.py`)**

   * Detects keyboard input
   * Sends movement commands to the Raspberry Pi using HTTP requests

2. **Raspberry Pi (`raspiCode.py`)**

   * Runs a Flask server
   * Receives commands from the client
   * Sends serial commands to the Arduino

3. **Arduino (`main.cpp`)**

   * Reads serial commands
   * Controls motor directions through motor pins

### Data Flow

```text
Laptop / Client
      ↓
HTTP Request (Flask)
      ↓
Raspberry Pi
      ↓
Serial Communication (USB)
      ↓
Arduino
      ↓
L298N Motor Driver
      ↓
TT Motors
```

---

## Project Structure 📂

```text
SmartCar/
│── client.py        # Sends keyboard commands to Raspberry Pi
│── raspiCode.py     # Flask server running on Raspberry Pi
│── main.cpp         # Arduino motor control code
│── README.md
```

---

## Hardware Used 🔧

* Raspberry Pi
* Arduino (UNO/Nano compatible)
* L298N Motor Driver
* TT Motors
* Chassis + Wheels
* Battery Pack
* USB connection between Raspberry Pi and Arduino

---

## Controls 🎮

| Key         | Action        |
| ----------- | ------------- |
| W           | Move Forward  |
| A           | Turn Left     |
| S           | Move Backward |
| D           | Turn Right    |
| Release Key | Stop          |

---

## Installation ⚙️

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

---

### 2. Install Client Dependencies

For `client.py`:

```bash
pip install pyobjc-framework-Quartz==12.2 requests==2.34.2 six==1.17.0 urllib3==2.7.0
```

---

### 3. Install Raspberry Pi Dependencies

For `raspiCode.py`:

```bash
pip install blinker==1.9.0 click==8.4.1 Flask==3.1.3 itsdangerous==2.2.0 Jinja2==3.1.6 MarkupSafe==3.0.3 pyserial==3.5 Werkzeug==3.1.8
```

---

## Setup 🚀

### Step 1 — Upload Arduino Code

Upload `main.cpp` to your Arduino using the Arduino IDE.

---

### Step 2 — Connect Arduino to Raspberry Pi

Connect the Arduino via USB.

Check the serial port:

```bash
ls /dev/tty*
```

Update this line in `raspiCode.py` if needed:

```python
port = '/dev/ttyACM0'
```

---

### Step 3 — Start Flask Server on Raspberry Pi

Run:

```bash
python3 raspiCode.py
```

The Flask server will run on:

```text
http://RASPBERRY_PI_IP:5000
```

---

### Step 4 — Configure Client

Open `client.py` and edit:

```python
serverIP = ''
```

Example:

```python
serverIP = 'http://192.168.1.10:5000'
```

Replace with your Raspberry Pi's local IP.

---

### Step 5 — Run Client

Run:

```bash
python3 client.py
```

Now use:

```text
W A S D
```

to control the car 🎉

---

## Example Architecture Diagram

```text
Client (Laptop)
      │
      ▼
HTTP POST Requests
      │
      ▼
Raspberry Pi Flask Server
      │
      ▼
Serial Commands
      │
      ▼
Arduino
      │
      ▼
L298N Motor Driver
      │
      ▼
Motors
```

---

## Future Improvements 🚀

* 📷 OpenCV live camera streaming
* 📏 Ultrasonic obstacle detection
* 🛑 Emergency braking system
* 🎮 Mobile app controller
* 🤖 Autonomous driving mode

---

## Troubleshooting 🧰

### Car not moving?

* Check battery power
* Verify Arduino is connected to Raspberry Pi
* Confirm correct serial port (`/dev/ttyACM0`)
* Ensure Flask server is running
* Check Raspberry Pi IP address

### Commands not being sent?

Make sure `serverIP` in `client.py` is correct:

```python
serverIP = 'http://YOUR_RASPBERRY_PI_IP:5000'
```

---

## License 📜

This project is open-source and free to modify for educational purposes.

---

Made with ☕ Python, Flask, Arduino, and a lot of debugging 😆
