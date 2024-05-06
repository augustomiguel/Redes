from socket import *

class SocketUDP:

    def __init__(self):
        self.serverName = '15.228.191.109'
        self.serverPort = 50000
        self.clientSocket = socket(AF_INET, SOCK_DGRAM)
        self.resposta = ""
        self.serverAddress = ""

    def mandar_mensagem(self, mensagem):
        self.clientSocket.sendto(mensagem, (self.serverName,self.serverPort))
        self.resposta, self.serverAddress = self.clientSocket.recvfrom(2048)
        self.clientSocket.close()
