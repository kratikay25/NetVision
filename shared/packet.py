"""
NetVision Packet Class

Every message exchanged between the
Server and Agents uses this packet format.
"""

from datetime import datetime


class Packet:

    def __init__(self, packet_type, payload):

        self.version = "1.0"

        self.packet_type = packet_type

        self.timestamp = datetime.now().isoformat()

        self.payload = payload

    def to_dict(self):

        return {
            "version": self.version,
            "packet_type": self.packet_type,
            "timestamp": self.timestamp,
            "payload": self.payload
        }

    @classmethod
    def from_dict(cls, data):

        packet = cls(
            data["packet_type"],
            data["payload"]
        )

        packet.version = data["version"]

        packet.timestamp = data["timestamp"]

        return packet