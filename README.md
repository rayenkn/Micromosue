
```markdown
# 🤖 High-Performance Autonomous Micromouse

> 🚧 **Status:** Firmware Architecture Skeleton / Tooling Active (Implementation in progress)

Firmware architecture and telemetry tooling for a high-speed, precision autonomous Micromouse maze-solving robot. Built using **PlatformIO** (C++) and complemented by a **Python real-time telemetry suite**, this repository establishes the foundational structure for low-level hardware drivers, motion control loops, and navigation algorithms.

---

## 📂 Project Architecture

```text
├── include/
│   ├── Control/           # Motion profiling and closed-loop feedback
│   │   ├── MotionProfiler.h
│   │   └── PID.h
│   ├── Core/              # System architecture and task execution
│   │   ├── StateMachine.h
│   │   └── Tasks.h
│   ├── Drivers/           # Low-level hardware peripherals & sensors
│   │   ├── EncoderPCNT.h
│   │   ├── ICM42688.h     # 6-axis IMU driver
│   │   ├── IRArray.h      # Infrared wall-detection sensors
│   │   └── MotorController.h
│   ├── Navigation/        # Maze mapping and path planning
│   │   ├── AStarPlanner.h
│   │   └── Maze.h
│   └── config.h           # Global pinouts, tuning parameters, and constants
├── src/
│   ├── ICM42688.cpp
│   ├── MotorController.cpp
│   └── main.cpp           # Entry point and main loop execution
├── plotter.py             # Real-time PyQtGraph serial telemetry plotting tool[cite: 2]
└── platformio.ini         # Build configuration and dependencies

```

---

## 🚀 Modules & Tooling Overview

### 1. Telemetry & Tuning Tool (`plotter.py`)

* **Real-Time Visualization:** A high-performance Python script built with `pyqtgraph` and `pyserial` designed to stream and plot real-time control data.


* **Packet Parsing:** Decodes binary serial telemetry packets (at `115200` baud) featuring robust header matching (`0xAA` to `0xAD`) and floating-point sanity checks to prevent resync errors.


* **Profile Comparison:** Plots target trapezoidal velocity profiles against actual measured wheel speeds for both left and right motors to assist in tuning PID controllers and motion profiling.



### 2. Planned Firmware Modules (`include/`)

* **Control System (`include/Control/`):** Planned implementation of closed-loop PID feedback (`PID.h`) and trapezoidal/S-curve motion profiling (`MotionProfiler.h`).
* **Hardware Drivers (`include/Drivers/`):** Scaffolding for high-resolution encoder pulse counting (`EncoderPCNT.h`), ICM42688 IMU sensor fusion (`ICM42688.h/.cpp`), infrared wall sensing (`IRArray.h`), and motor actuation (`MotorController.h/.cpp`).
* **Navigation & Intelligence (`include/Navigation/`):** Grid-based maze representation (`Maze.h`) and shortest-path calculation (`AStarPlanner.h`).
* **Core Architecture (`include/Core/`):** Non-blocking task scheduling (`Tasks.h`) and state management (`StateMachine.h`).

---

## 🛠️ Getting Started & Usage

### Prerequisites

* [VS Code](https://code.visualstudio.com/) with the **PlatformIO IDE** extension.
* Python 3.x with required plotting dependencies for telemetry:
```bash
pip install pyserial pyqtgraph numpy

```



### Running the Telemetry Plotter

1. Connect your microcontroller via USB.
2. Update the `PORT` variable in `plotter.py` if necessary (defaults to `'COM3'`).


3. Execute the script to launch the live plotting interface:

```bash
python plotter.py

```

---

## 📝 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

```

```
