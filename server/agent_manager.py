"""
NetVision Agent Manager

Maintains information about all connected agents.
"""


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

            "status": "ONLINE"

        }

    def update_metrics(self, hostname, metrics):

        if hostname not in self.agents:
            return

        self.agents[hostname]["cpu"] = metrics["cpu"]

        self.agents[hostname]["memory"] = metrics["memory"]

        self.agents[hostname]["disk"] = metrics["disk"]

        self.agents[hostname]["battery"] = metrics["battery"]

    def remove(self, hostname):

        if hostname in self.agents:

            del self.agents[hostname]

    def get(self, hostname):

        return self.agents.get(hostname)

    def get_all(self):

        return self.agents

    def count(self):

        return len(self.agents)