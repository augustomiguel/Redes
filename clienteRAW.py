import socket
import struct
address = "15.228.191.109"
serverPort = 50000
server_address = (address, serverPort)


class SocketRAW:

    def send_message(self, mensagem):
        with self.criar_raw_socket() as socket:  # Usa o gerenciador de contexto para fechamento automático de socket
            # Envia a mensagem para o servidor
            print("enviando mensagem: ", mensagem)
            socket.sendto(mensagem, server_address)

            # Receba a resposta (assumindo que o servidor envie uma resposta)
            print("recebendo resposta")
            mensagem_recebida = socket.recvfrom(4096)  
            print(mensagem_recebida)
            return mensagem_recebida


    def criar_raw_socket(self):
        try:
            # Cria um soquete com família de endereços AF_INET (IPv4) e tipo de soquete SOCK_RAW e o protocolo IPPROTO_RAW
            raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

            #Defina a opção SO_REUSEADDR para permitir a reutilização do mesmo endereço
            raw_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            return raw_socket
        except OSError as e:
            raise OSError(f"Failed to create raw socket: {e}")
            


