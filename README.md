# Controlling System Volume with Fingers

This Python project uses your webcam and computer vision to control the system volume using hand gestures. It tracks your fingers in real-time using **MediaPipe** and adjusts the volume based on the distance between your **thumb** and **index finger**, creating a fun and interactive experience.

---

## 🎯 Features

* Real-time hand tracking using MediaPipe
* System volume control with gesture recognition
* Webcam-based interaction without any hardware modules

---

## ✅ Prerequisites

* Python 3.7 or above installed on your system
* A webcam
* Git and a code editor (VS Code or PyCharm recommended)

---

## 🔧 Setup & Run Instructions

### 1. Open your IDE or terminal window.

### 2. Clone the repository:

```
git clone https://github.com/Javeria-Sheraz/Controlling-system-volume-with-fingers.git
cd Controlling-system-volume-with-fingers
```

### 3. Create a virtual environment:

```
python -m venv venv
```
Ensure venv folder is created in the cloned repo folder

### 4. Activate the environment (for CMD terminal):

```
venv\Scripts\activate
```

> ⚠️ If you're using PowerShell and encounter script permission errors:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 5. Ensure `requiredLibraries.txt` is in the same folder.

### 6. Install the required libraries:

```
pip install -r requiredLibraries.txt
```

### 7. Run the main file:

```
python GestureVolumeControl.py
```

---

## ▶️ Optional: Use `run.bat

Create a file named `run.bat` and paste this:

```bat
@echo off
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requiredLibraries.txt
python GestureVolumeControl.py
```

## 🗂️ Project Structure

```
Controlling-system-volume-with-fingers/
├── GestureVolumeControl.py
├── requiredLibraries.txt
├── README.md
└── venv/
```

By [Javeria Sheraz](https://github.com/Javeria-Sheraz)

