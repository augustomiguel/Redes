import socket
import struct



ip_servidor = "15.228.191.109"
# Divida o endereço IP em seus componentes numéricos
ip_numerico = [int(x) for x in ip_servidor.split('.')]
# Empacote o endereço IP
endereco_binario = struct.pack('!BBBB', *ip_numerico)

address = "15228191109"
serverPort = 50000
server_address = (ip_servidor, serverPort)

class SocketRAW:

    def send_message(self, mensagem):
        try:
            with self.criar_raw_socket() as socket:  # Usa o gerenciador de contexto para fechamento automático de socket
                # Envia a mensagem para o servidor
                print("enviando a mensagem: {0} para o endereço: {1}".format( mensagem, server_address))
                socket.sendto(mensagem, (ip_servidor,serverPort))

                # Receba a resposta (assumindo que o servidor envie uma resposta)
                print("esperando resposta")
                mensagem_recebida, _ = socket.recvfrom(4096)  
                print(mensagem_recebida)
                return mensagem_recebida
        except OSError as e:
            raise OSError(f"Failed to create raw socket: {e}")

    def criar_raw_socket(self):
        try:
            # Cria um soquete com família de endereços AF_INET (IPv4) e tipo de soquete SOCK_RAW e o protocolo IPPROTO_RAW
            raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

            #Defina a opção SO_REUSEADDR para permitir a reutilização do mesmo endereço
            raw_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            return raw_socket
        except OSError as e:
            raise OSError(f"Failed to create raw socket: {e}")
            


