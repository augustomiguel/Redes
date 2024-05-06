import socket
import struct
server_address = "15.228.191.109"
serverPort = 50000


class SocketRAW:
    raw_socket = None

    def send_message(self, mensagem):
        criar_raw_socket()

        # Send the message to the server
        self.raw_socket.sendto(mensagem, server_address)
        
        return mensagem_recebida


    def criar_raw_socket(self):
        try:
            # Cria um soquete com família de endereços AF_INET (IPv4) e tipo de soquete SOCK_RAW e o protocolo IPPROTO_RAW
            self.raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

            #Defina a opção SO_REUSEADDR para permitir a reutilização do mesmo endereço
            self.raw_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
        except OSError as e:
            raise OSError(f"Failed to create raw socket: {e}")


