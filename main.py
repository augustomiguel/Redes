from socket import *
from clienteUDP import SocketUDP
import binascii
import random

data = "\x00"
frase = "\x01"
quantidade = "\x02"
requisicao_invalida = "\x03"

mensagem_enviada = ""
mensagem_recebida = ""

serverName = "15.228.191.109"
serverPort = 50000

while(True):
    print("O que você deseja fazer? ")
    print("1) Solicitar Data e Hora atual.")
    print("2) Uma mensagem motivacional para o fim do semestre.")
    print("3) A quantidade de respostas emitidas pelo servidor até o momento.")
    print("4) Sair.")
    opcao = input("-> ")
    if opcao == "1":
        mensagem_enviada += data

        # Gera um número de 1 a 65535 
        random_number = random.randint(1, 65535)
        # Transforma o número em hexadecimal
        identificador = hex(random_number)
        # Remove o '0b'
        identificador = identificador[2:]
        # utiliza os primeiros 4 bits do número
        primeiro_byte = "\\x" + identificador[:2]
        # utiliza os 4 últimos bits do número
        segundo_byte = "\\x" + identificador[2:4]

        # Adiciona o número na mensagem
        mensagem_enviada += primeiro_byte
        mensagem_enviada += segundo_byte
       
        # Envia a mensagem 
        udp = SocketUDP()
        udp.mandar_mensagem(mensagem_enviada)
        mensagem_recebida = udp.resposta
        mensagem_recebida = mensagem_recebida[4:-2]
        mensagem_recebida = mensagem_recebida.decode("utf-8")
        print(mensagem_recebida)
        mensagem_enviada = ""


    elif opcao == "2":
        mensagem_enviada += frase
        # Gera um número de 1 a 65535 
        random_number = random.randint(1, 65535)
        # Transforma o número em hexadecimal
        identificador = hex(random_number)
        # Remove o '0b'
        identificador = identificador[2:]
        # utiliza os primeiros 4 bits do número
        primeiro_byte = "\\x" + identificador[:2]
        # utiliza os 4 últimos bits do número
        segundo_byte = "\\x" + identificador[2:4]

        # Adiciona o número na mensagem
        mensagem_enviada += primeiro_byte
        mensagem_enviada += segundo_byte
       
        # Envia a mensagem 
        udp = SocketUDP()
        udp.mandar_mensagem(mensagem_enviada)
        mensagem_recebida = udp.resposta
        mensagem_recebida = mensagem_recebida[4:-2]
        mensagem_recebida = mensagem_recebida.decode("utf-8")
        print(mensagem_recebida)
        mensagem_enviada = ""
    elif opcao == "3":
        mensagem_enviada += quantidade

        # Gera um número de 1 a 65535 
        random_number = random.randint(1, 65535)
        # Transforma o número em hexadecimal
        identificador = hex(random_number)
        # Remove o '0b'
        identificador = identificador[2:]
        # utiliza os primeiros 4 bits do número
        primeiro_byte = "\\x" + identificador[:2]
        # utiliza os 4 últimos bits do número
        segundo_byte = "\\x" + identificador[2:4]

        # Adiciona o número na mensagem
        mensagem_enviada += primeiro_byte
        mensagem_enviada += segundo_byte
       
        # Envia a mensagem 
        udp = SocketUDP()
        udp.mandar_mensagem(mensagem_enviada)
        mensagem_recebida = udp.resposta
        mensagem_recebida = mensagem_recebida[-4:]
        mensagem_recebida = int.from_bytes(mensagem_recebida, byteorder='big', signed=False)
        print(mensagem_recebida)
        mensagem_enviada = ""
    elif opcao == "4":
        print("Programa finalizado.")
        exit(0)
    else:
        print("Opcao inválida!")