from socket import *
serverName = "15.228.191.109"
serverPort = 50000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Digite string em minusculo:')

clientSocket.sendto(message.encode(),(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())
clientSocket.close()