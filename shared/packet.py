"""
Packet Builder
"""


def create_packet(packet_type, payload):
    """
    Creates a packet dictionary.
    """

    return {
        "type": packet_type,
        "payload": payload
    }