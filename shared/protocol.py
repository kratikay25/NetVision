import json


def send_json(socket, data):
    """
    Send a JSON object through a socket.
    """

    message = json.dumps(data)

    socket.sendall(message.encode())


def receive_json(socket):
    """
    Receive a JSON object from a socket.
    """

    message = socket.recv(4096).decode()

    return json.loads(message)