> 🚧 **Status:** Work in Progress / Architectural Skeleton (Implementation in progress)
---

# 🤖 High-Performance Autonomous Micromouse

Firmware architecture for a high-speed, precision autonomous Micromouse maze-solving robot. Built using **PlatformIO** and modern embedded C++, this repository houses low-level hardware drivers, advanced motion control loops, and graph-based maze navigation algorithms.

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
└── platformio.ini         # Build configuration and dependencies

```

---

## 🚀 Key Modules & Features

### 1. Control System (`include/Control/`)

* **PID Controller (`PID.h`):** Robust closed-loop control loops implemented for precise velocity, heading, and distance tracking.
* **Motion Profiler (`MotionProfiler.h`):** Trapezoidal/S-curve motion profiling for smooth acceleration, maximum cornering velocity, and deceleration management.

### 2. Hardware Drivers (`include/Drivers/`)

* **Encoders (`EncoderPCNT.h`):** High-resolution hardware pulse counting (PCNT) for accurate odometry and position estimation.
* **IMU Integration (`ICM42688.h/.cpp`):** Gyroscope and accelerometer data fusion for precise heading stabilization and drift correction during high-speed straights and turns.
* **IR Sensor Array (`IRArray.h`):** Real-time front and diagonal wall detection for immediate reflex navigation and grid alignment.
* **Motor Control (`MotorController.h/.cpp`):** PWM signal generation and directional switching interface for differential drive actuation.

### 3. Navigation & Intelligence (`include/Navigation/`)

* **Maze Representation (`Maze.h`):** Grid data structure mapping wall states, visited nodes, and exploration status.
* **Path Planning (`AStarPlanner.h`):** Optimal path calculation algorithm used for navigating the shortest path from the start cell to the center once the maze has been mapped.

### 4. Core Architecture (`include/Core/`)

* **State Machine (`StateMachine.h`):** Manages robot states (e.g., *Standby, Searching, Speed Run, Calibration, Error*).
* **Task Manager (`Tasks.h`):** Non-blocking execution scheduler ensuring deterministic timing for sensor polling, control updates, and logging.

---

## 🛠️ Getting Started

### Prerequisites

* [VS Code](https://code.visualstudio.com/) with the **PlatformIO IDE** extension installed.

### Building & Flashing

1. Clone the repository:
```bash
git clone https://github.com/your-username/micromouse-firmware.git

```


2. Open the folder in VS Code / PlatformIO.
3. Build the project:
```bash
pio run

```


4. Upload firmware to your target board:
```bash
pio run --target upload

```



---

## 📝 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
