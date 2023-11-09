"""
运行两次
"""
from net.msg import Msg
from net.rpc_client import RPCClient
from net.socket_client import SocketClient


class Client(SocketClient, RPCClient):
    def handle_msg(self, msg: str):
        msg = Msg.load(msg)
        if msg.types == Msg.TYPE_RPC:
            callback = msg.data.pop('callback', None)
            if isinstance(callback, str):
                callback = getattr(self, callback)
            callback and callback(msg.data)
        else:
            print(msg)


if __name__ == '__main__':
    client = Client('172.23.208.1', 9999)
    client.start()

    while True:
        data = input()
        client.send(Msg(data, sender=client.sender).value)
