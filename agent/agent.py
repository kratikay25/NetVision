"""
=========================================
NetVision Agent
Author: Kratika Yadav
=========================================
"""

import socket
import platform
import getpass
import sys
import os

# Allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.config import HOST, PORT
from shared.protocol import send_json, receive_json
from shared.constants import REGISTER

# -------------------------------
# Create Socket
# -------------------------------

agent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

agent.connect((HOST, PORT))

print("=" * 50)
print("NetVision Agent Started")
print("=" * 50)

# -------------------------------
# Device Information
# -------------------------------

device = {
    "hostname": platform.node(),
    "os": platform.system(),
    "username": getpass.getuser()
}

packet = {
    "type": REGISTER,
    "payload": device
}

send_json(agent, packet)

reply = receive_json(agent)

print("\nServer Response")
print(reply["payload"]["message"])

agent.close()