from socket import *
import json
from interfaceConn.registerFunc import showLoginForm


class Client:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect(('localhost', 9091))

    def sender(self, message_type, message):
        message = {"type": message_type, "message": message}
        self.sock.send(json.dumps(message).encode('utf-8'))

    def getter(self):
        try:
            data = json.loads(self.sock.recv(10000).decode('utf-8'))
        except Exception as e:
            print(e)
            data = ''
        return data

    def checkEmail(self, email):
        self.sender(message_type="check register", message=f"{email}")
        return self.getter()["message"]

    def checkUser(self, login, password):
        self.sender(message_type="check user", message=[f"{login}", f"{password}"])
        return self.getter()["message"]

    def addNewUser(self, email, login, password):
        self.sender(message_type="add new user", message=[f"{email}", f"{login}", f"{password}"])

    def sendTestStrategyData(self, data):
        self.sender(message_type="test new strategy", message=data)

    def updateStrategies(self, login):
        self.sender(message_type="update strategies", message=login)
        return self.getter()["message"]

    def checkMarketData(self, market, key, secret):
        self.sender(message_type="connect to market", message=[f"{market}", f"{key}", f"{secret}"])
        return self.getter()["message"]


if __name__ == '__main__':
    client = Client()
    showLoginForm(client)

