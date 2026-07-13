"""
NetVision Server
"""

from server.connection import ConnectionManager
from server.agent_manager import AgentManager
from server.router import Router


connection = ConnectionManager()

agents = AgentManager()

router = Router(agents)

connection.start()

connection.accept_clients(router.handle)