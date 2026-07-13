"""
Packet Router

Routes packets received from agents.
"""

from shared.packet import Packet
from shared.protocol import receive_json, send_json
from shared.constants import REGISTER, WELCOME, HEARTBEAT, SYSTEM_INFO


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

                    print(f"\n🟢 Registered : {hostname}")

                    welcome = Packet(
                        WELCOME,
                        {
                            "message": f"Welcome {hostname}!"
                        }
                    )

                    send_json(agent_socket, welcome)

                elif packet.packet_type == HEARTBEAT:

                    print(f"Working {hostname}")

                elif packet.packet_type == SYSTEM_INFO:

                    self.agent_manager.update_metrics(
                        hostname,
                        packet.payload
                    )

                    info = self.agent_manager.get(hostname)

                    print("\n" + "=" * 45)
                    print(f"Agent    : {hostname}")
                    print(f"CPU      : {info['cpu']} %")
                    print(f"Memory   : {info['memory']} %")
                    print(f"Disk     : {info['disk']} %")
                    print(f"Battery  : {info['battery']} %")
                    print("=" * 45)

        except Exception as e:

            print(f"\n🔴 Disconnected : {hostname}")
            print(f"Reason: {e}")

        finally:

            self.agent_manager.remove(hostname)

            agent_socket.close()