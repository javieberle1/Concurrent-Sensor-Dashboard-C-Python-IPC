# 📊 Concurrent Sensor Dashboard (C + Python IPC)

A hybrid real-time monitoring system demonstrating the integration of low-level concurrent programming (C) with modern data visualization (Python/Streamlit) via Inter-Process Communication (IPC).

## 🚀 Project Description

This project simulates a telemetry environment where multiple sensors generate data simultaneously. It uses **C** to handle concurrent data generation via POSIX threads and Mutex synchronization, ensuring high performance and memory safety.

The generated data is captured in real-time by an orchestrator in **Python** using system pipes. Finally, a web interface built with **Streamlit** processes and visualizes this information instantly.

## ✨ Key Technical Features

- **Multithreading (C):** Implementation of `pthreads` to simulate independent sensors (Temperature and Humidity) operating at different frequencies.
- **Synchronization (C):** Use of `pthread_mutex_t` to protect the critical section (standard output) and prevent race conditions.
- **Inter-Process Communication (IPC):** Seamless integration between C and Python using `subprocess.PIPE` to capture the data stream (`stdout`) in real-time.
- **Live Memory Management (Python):** Sliding window algorithm using `pandas` to maintain a maximum history of 30 records, optimizing RAM consumption in the visual interface.
- **Reactive Dashboard:** Web GUI built with Streamlit that updates metrics and line charts dynamically without reloading the page.

## 🛠️ Tech Stack

- **Core Engine:** C (GCC, `pthread.h`, `unistd.h`)
- **Orchestrator & Frontend:** Python 3.x
- **Python Libraries:** `streamlit`, `pandas`, `subprocess`

## ⚙️ Installation and Usage Instructions

### 1. Clone the repository

```bash
git clone [https://github.com/javiereberle1/Concurrent-Sensor-Dashboard-C-Python-IPC.git](https://github.com/javiereberle1/Concurrent-Sensor-Dashboard-C-Python-IPC.git)
cd Concurrent-Sensor-Dashboard-C-Python-IPC
```

### 2. Compile the C Engine

You need to compile the source code by linking the threads library:

```bash
gcc simulador.c -o sensors -lpthread
```

_(Note: Ensure the generated file is named exactly `sensors` or `sensors.exe` on Windows)._

### 3. Setup the Python Environment

It is recommended to use a virtual environment to install dependencies in isolation:

```bash
# Create virtual environment
python3 -m venv sensor_env

# Activate the environment (Linux/macOS)
source sensor_env/bin/activate
# On Windows use: sensor_env\Scripts\activate

# Install libraries
pip install streamlit pandas
```

### 4. Run the Dashboard

With the active environment and the compiled C engine, start the local server:

```bash
streamlit run dashboard.py
```

The browser will automatically open the control panel. Click on **"Iniciar Lectura desde C"** (Start Reading from C) to establish the IPC bridge and view the concurrent telemetry.

## 👨‍💻 Author

**Javier Andrés Eberle**

- [LinkedIn](www.linkedin.com/in/javiereberle)

---

_This project was developed to demonstrate core competencies in operating systems, data concurrency, and cross-language integration._
