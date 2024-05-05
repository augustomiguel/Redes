from socket import *
from clienteUDP import SocketUDP
import random

class UDP:
    
    def __init__(self):
        self.data = "\x00"
        self.frase = "\x01"
        self.quantidade = "\x02"

        self.mensagem_enviada = ""
        self.mensagem_recebida = ""

        self.serverName = "15.228.191.109"
        self.serverPort = 50000

    def enviar_requisicaoUDP(self, opcao):
        if opcao == "1":
            self.mensagem_enviada += self.data
        elif opcao == "2":
            self.mensagem_enviada += self.frase
        elif opcao == "3":
            self.mensagem_enviada += self.quantidade
        elif opcao == "4":
            print("Programa finalizado com sucesso.")
            exit(0)
        random_number = random.randint(1, 65535)
        identificador = hex(random_number)

        identificador = identificador[2:]
        primeiro_byte = "\\x" + identificador[:2]
        segundo_byte = "\\x" + identificador[2:4]

        self.mensagem_enviada += primeiro_byte
        self.mensagem_enviada += segundo_byte

        # Envia a mensagem 
        udp = SocketUDP()
        udp.mandar_mensagem(mensagem_enviada)
        self.mensagem_recebida = udp.resposta
        if opcao == "1" or opcao == "2":
            self.mensagem_recebida = self.mensagem_recebida[4:-2]
            self.mensagem_recebida = self.mensagem_recebida.decode("utf-8")
        elif opcao == "3":
            self.mensagem_recebida = self.mensagem_recebida[-4:]
            self.mensagem_recebida = int.from_bytes(self.mensagem_recebida, byteorder='big', signed=False)
        print(self.mensagem_recebida)
        self.mensagem_enviada = ""
