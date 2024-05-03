from socket import *
import struct
serverName = "15.228.191.109"
serverPort = 50000

def udp (self):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input('Digite string em minusculo:')

    clientSocket.sendto(message.encode(),(serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print(modifiedMessage.decode())
    clientSocket.close()
    



# class MensagemUDP:
#     def __init__(self, tipo, id, payload):
#         self.tipo = tipo
#         self.id = id
#         self.payload = payload

#     def to_bytes(self):
#         tipo_bytes = struct.pack('!H', self.tipo)
#         id_bytes = struct.pack('!H', self.id)
#         tamanho_resposta_bytes = struct.pack('!B', len(self.payload))

#         mensagem_bytes = tipo_bytes + id_bytes + tamanho_resposta_bytes + self.payload

#         return mensagem_bytes

#     @classmethod
#     def from_bytes(self, mensagem_bytes):
#         tipo_bytes, id_bytes, tamanho_resposta_bytes = mensagem_bytes[:5]

#         tipo = struct.unpack('!H', tipo_bytes)[0]
#         id = struct.unpack('!H', id_bytes)[0]
#         tamanho_resposta = struct.unpack('!B', tamanho_resposta_bytes)[0]

#         payload = mensagem_bytes[5:5 + tamanho_resposta]

#         return MensagemUDP(tipo, id, payload)
