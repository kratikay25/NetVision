import json


def send_json(sock, packet):

    data = json.dumps(packet.to_dict())

    sock.sendall(data.encode())


def receive_json(sock):

    data = sock.recv(4096).decode()

    dictionary = json.loads(data)

    return dictionary