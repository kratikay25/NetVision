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


def monitor_agents(agent_manager):

    while True:

        agent_manager.check_offline_agents()

        show_dashboard(agent_manager)

        time.sleep(2)


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

connection.accept_clients(router.handle)