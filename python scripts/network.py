import socket

class TCPSocket :

    def __init__(self,ip,port) :
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip,port))
        self.socket.listen(1)
        self.wait()

    def wait(self) :
        self.client,addr = self.socket.accept()

    def send(self,data) :
        if self.client is not None :
            self.client.send(data)

class UDPSender :

    def __init__(self,ip,port) :
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1)
        self.ip = ip
        self.port = port

    def send(self,data) :
        self.socket.sendto(str.encode(data),(self.ip,self.port))

class UDPReciever :
    def __init__(self,ip,port) :
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.ip = ip
        self.port = port
        self.socket.bind((self.ip, self.port))

    def recv(self,buff_size):
        data, _ = self.socket.recvfrom(buff_size)
        return data
