"""
NetVision Command Manager
"""

from shared.packet import Packet
from shared.protocol import send_json
from shared.constants import COMMAND


class CommandManager:

    def send_command(self, agent_socket, command):

        packet = Packet(
            COMMAND,
            {
                "command": command
            }
        )

        send_json(agent_socket, packet)