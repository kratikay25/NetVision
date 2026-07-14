

"""
NetVision Agent Manager

Maintains information about all connected agents.
"""

from datetime import datetime
class AgentManager:

    def __init__(self):
        self.agents = {}

    def register(self, hostname, socket, info):

        self.agents[hostname] = {
            "socket": socket,
            "hostname": hostname,
            "os": info.get("os"),
            "username": info.get("username"),
            "cpu": 0,
            "memory": 0,
            "disk": 0,
            "battery": "N/A",
            "health": 100,
            "status": "ONLINE",
            "last_seen": datetime.now()
        }

    def update_metrics(self, hostname, metrics):

        if hostname not in self.agents:
            return

        agent = self.agents[hostname]

        agent["last_seen"] = datetime.now()

        agent["cpu"] = metrics["cpu"]
        agent["memory"] = metrics["memory"]
        agent["disk"] = metrics["disk"]
        agent["battery"] = metrics["battery"]

        if "username" in metrics:
            agent["username"] = metrics["username"]

        if "os" in metrics:
            agent["os"] = metrics["os"]

        # Calculate Health Score
        health = 100

        health -= min(agent["cpu"] * 0.2, 20)
        health -= min(agent["memory"] * 0.1, 10)
        health -= min(agent["disk"] * 0.1, 10)

        if isinstance(agent["battery"], (int, float)) and agent["battery"] < 20:
            health -= 15

        agent["health"] = max(0, round(health))

    def remove(self, hostname):

        if hostname in self.agents:
            del self.agents[hostname]

    def get(self, hostname):
        return self.agents.get(hostname)

    def get_all(self):
        return self.agents

    def check_offline_agents(self):

        for agent in self.agents.values():

            seconds = (
                datetime.now() - agent["last_seen"]
            ).total_seconds()

            if seconds > 15:
                agent["status"] = "OFFLINE"
            else:
                agent["status"] = "ONLINE"

    def count(self):
        return len(self.agents)