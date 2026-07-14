"""
=========================================
NetVision Agent
=========================================
"""

import socket
import platform
import getpass
import time
import argparse

from agent.config import HOST, PORT, AGENT_NAME
from shared.protocol import send_json, receive_json
from shared.packet import Packet
from shared.constants import REGISTER, HEARTBEAT, SYSTEM_INFO
from agent.monitor import get_system_info

# ----------------------------
# Command-line arguments
# ----------------------------

parser = argparse.ArgumentParser()

parser.add_argument(
    "--name",
    help="Agent hostname"
)

args = parser.parse_args()

hostname = args.name if args.name else AGENT_NAME

# ----------------------------
# Connect to Server
# ----------------------------

agent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

agent.connect((HOST, PORT))

print("=" * 50)
print("NetVision Agent Started")
print("=" * 50)

device = {
    "hostname": hostname,
    "os": platform.system(),
    "username": getpass.getuser()
}

register_packet = Packet(
    REGISTER,
    device
)

send_json(agent, register_packet)

reply = receive_json(agent)

print(reply["payload"]["message"])

print("\nSending heartbeat every 5 seconds...\n")

try:

    while True:

        heartbeat = Packet(
            HEARTBEAT,
            {
                "hostname": hostname
            }
        )

        send_json(agent, heartbeat)

        system_packet = Packet(
            SYSTEM_INFO,
            get_system_info()
        )

        send_json(agent, system_packet)

        time.sleep(5)

except KeyboardInterrupt:

    print("\nAgent Stopped")

finally:

    agent.close()