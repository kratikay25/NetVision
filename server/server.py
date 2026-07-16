"""
NetVision Server
"""

import threading
import time

from server.connection import ConnectionManager
from server.agent_manager import AgentManager
from server.router import Router
from server.dashboard import show_dashboard
from server.database import initialize_database
from server.command_manager import CommandManager
from shared.constants import PING


def monitor_agents(agent_manager):

    while True:

        agent_manager.check_offline_agents()

        show_dashboard(agent_manager)

        time.sleep(2)


def command_console(agent_manager):

    command_manager = CommandManager()

    # Give agents time to connect
    time.sleep(3)

    while True:

        try:

            hostname = input(
                "\nEnter agent name to PING "
                "(or type exit): "
            ).strip()

            if hostname.lower() == "exit":
                break

            agent = agent_manager.get(hostname)

            if not agent:
                print(f"Agent '{hostname}' not found.")
                continue

            if agent.get("status") != "ONLINE":
                print(f"Agent '{hostname}' is OFFLINE.")
                continue

            agent_socket = agent.get("socket")

            if not agent_socket:
                print("Agent socket not available.")
                continue

            command_manager.send_command(
                agent_socket,
                PING
            )

            print(f"PING sent to {hostname}.")

        except Exception as e:

            print(f"Command error: {e}")


connection = ConnectionManager()

agents = AgentManager()

router = Router(agents)

connection.start()

initialize_database()


# Start monitoring thread
monitor_thread = threading.Thread(
    target=monitor_agents,
    args=(agents,),
    daemon=True
)

monitor_thread.start()


# Start command console thread
command_thread = threading.Thread(
    target=command_console,
    args=(agents,),
    daemon=True
)

command_thread.start()


# Accept agent connections
connection.accept_clients(router.handle)