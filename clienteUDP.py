from socket import *
import struct
from mensagem import MensagemUDP


serverName = "15.228.191.109"
serverPort = 50000
processar_mensagem = Mensagem()

def udp (self,opcao):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = opcao

    clientSocket.sendto(message.encode(),(serverName, serverPort))
    enviar_mensagem()
    sen

    print(modifiedMessage.decode())
    clientSocket.close()
    

def enviar_mensagem(socket, message, server_address):
    # Convert message to MensagemUDP object
    mensagem_udp = MensagemUDP(message.tipo, message.payload)

    # Convert MensagemUDP object to bytes
    message_bytes = mensagem_udp.to_bytes()

    # Send the message to the server
    socket.sendto(message_bytes, server_address)