"""
Packet Router

Routes packets received from agents.
"""

from shared.packet import Packet
from shared.protocol import receive_json, send_json
from shared.constants import REGISTER, WELCOME, HEARTBEAT, SYSTEM_INFO
from server.dashboard import show_dashboard


class Router:

    def __init__(self, agent_manager):
        self.agent_manager = agent_manager

    def handle(self, agent_socket, address):

        hostname = None

        try:

            while True:

                data = receive_json(agent_socket)

                packet = Packet.from_dict(data)

                if packet.packet_type == REGISTER:

                    hostname = packet.payload["hostname"]

                    self.agent_manager.register(
                        hostname,
                        agent_socket,
                        packet.payload
                    )

                    welcome = Packet(
                        WELCOME,
                        {
                            "message": f"Welcome {hostname}!"
                        }
                    )

                    send_json(agent_socket, welcome)

                elif packet.packet_type == HEARTBEAT:

                    # Heartbeat received.
                    # Dashboard will refresh when SYSTEM_INFO arrives.
                    pass

                elif packet.packet_type == SYSTEM_INFO:

                    self.agent_manager.update_metrics(
                        hostname,
                        packet.payload
                    )

                    show_dashboard(self.agent_manager)

        except Exception as e:

            print(f"\nDisconnected: {hostname}")
            print(f"Reason: {e}")

        finally:

          if hostname and hostname in self.agent_manager.agents:
            self.agent_manager.agents[hostname]["status"] = "OFFLINE"

          agent_socket.close()