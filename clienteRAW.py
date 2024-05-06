import socket
import struct
serverName = "15.228.191.109"
serverPort = 50000



import socket
import struct

class SocketRAW:
    def main:
        pass

def send_message(socket, message, server_address):
    # Convert message to MensagemRAW object
    mensagem_raw = MensagemRAW(message.tipo, message.id, message.payload)

    # Convert MensagemRAW object to bytes
    message_bytes = mensagem_raw.to_bytes()

    # Send the message to the server
    socket.sendto(message_bytes, server_address)


    
    