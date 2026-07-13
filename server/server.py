"""
=========================================
NetVision Monitoring Server
Author: Kratika Yadav
=========================================
"""

import socket
import threading
import sys
import os

# Allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server.config import HOST, PORT, BUFFER_SIZE, MAX_CLIENTS
from shared.protocol import send_json, receive_json
from shared.constants import REGISTER, WELCOME

# -------------------------------
# Create Server Socket
# -------------------------------

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(MAX_CLIENTS)

print("=" * 60)
print(" NetVision Monitoring Server ")
print("=" * 60)
print(f"Listening on {HOST}:{PORT}")
print("=" * 60)

# Store connected agents
agents = {}

# -------------------------------
# Handle Agent
# -------------------------------

def handle_agent(agent_socket, address):

    try:

        packet = receive_json(agent_socket)

        if packet["type"] == REGISTER:

            info = packet["payload"]

            hostname = info["hostname"]

            agents[hostname] = agent_socket

            print(f"\nAgent Registered : {hostname}")
            print(f"Address          : {address}")

            reply = {
                "type": WELCOME,
                "payload": {
                    "message": f"Welcome {hostname} to NetVision!"
                }
            }

            send_json(agent_socket, reply)

    except Exception as e:

        print("Error:", e)

    finally:

        agent_socket.close()

        print("Connection Closed")


# -------------------------------
# Accept Agents
# -------------------------------

print("\nServer Ready...\n")

while True:

    agent_socket, address = server.accept()

    thread = threading.Thread(
        target=handle_agent,
        args=(agent_socket, address)
    )

    thread.start()