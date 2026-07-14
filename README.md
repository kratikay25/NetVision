# 🚀 NetVision

> Enterprise Network Monitoring System built using Python Socket Programming.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Socket Programming](https://img.shields.io/badge/Networking-TCP-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📌 Overview

NetVision is a client-server based enterprise network monitoring system developed in Python.

The system continuously monitors multiple computers (agents) over TCP sockets and displays live system statistics such as CPU usage, memory usage, disk usage, battery percentage, health score, and connection status on a centralized dashboard.

---

# ✨ Features

- ✅ Multi-Agent Monitoring
- ✅ TCP Socket Communication
- ✅ JSON Packet Protocol
- ✅ Live Enterprise Dashboard
- ✅ SQLite Database Storage
- ✅ Health Score Calculation
- ✅ Offline Agent Detection
- ✅ Analytics Engine
- ✅ Automatic Graph Generation
- ✅ Active Alert System

---

# 🏗 Architecture

```
           Agent 1
               │
           Agent 2
               │
           Agent 3
               │
         TCP Socket Network
               │
               ▼
      NetVision Monitoring Server
               │
    ┌──────────┴───────────┐
    │ Dashboard            │
    │ SQLite Database      │
    │ Analytics Engine     │
    │ Alert System         │
    └──────────────────────┘
```

---

# 📂 Project Structure

```
NetVision/
│
├── agent/
├── server/
├── shared/
├── database/
├── reports/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🛠 Tech Stack

- Python
- Socket Programming
- SQLite
- JSON
- Matplotlib
- Git
- GitHub

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/kratikay25/NetVision.git
```

Move into the project

```bash
cd NetVision
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Start the server

```bash
python -m server.server
```

Start an agent

```bash
python -m agent.agent
```

Multiple agents

```bash
python -m agent.agent --name MacBook
python -m agent.agent --name Windows-PC
python -m agent.agent --name Ubuntu-Server
```

---

# 📊 Current Features

- Live Dashboard
- Multi-Agent Support
- Analytics Reports
- CPU/RAM Graphs
- SQLite Database
- Offline Detection
- Health Monitoring

---

# 🚀 Future Enhancements

- Web Dashboard
- Remote Command Execution
- Email Alerts
- Docker Support
- Authentication
- REST API
- Mobile Dashboard

---

# 👩‍💻 Author

**Kratika Yadav**

GitHub: https://github.com/kratikay25

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
