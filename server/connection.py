"""
NetVision Server Connection Manager
"""

import socket
import threading

from server.config import HOST, PORT, MAX_CLIENTS


class ConnectionManager:

    def __init__(self):

        self.server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.server_socket.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(MAX_CLIENTS)

    def start(self):

        print("=" * 60)
        print(" NetVision Monitoring Server ")
        print("=" * 60)
        print(f"Listening on {HOST}:{PORT}")
        print("=" * 60)
        print("\nServer Ready...\n")

    def accept_clients(self, handler):

        while True:

            agent_socket, address = self.server_socket.accept()

            threading.Thread(
                target=handler,
                args=(agent_socket, address),
                daemon=True
            ).start()
