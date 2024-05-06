from socket import *
from clienteUDP import SocketUDP
import binascii
import random

data = b"\x00"
frase = b"\x01"
quantidade = b"\x02"
requisicao_invalida = b"\x03"


serverName = "15.228.191.109"
serverPort = 50000

mensagem_enviada = b""

def enviar_mensagem(opcao):
    data = b"\x00"
    frase = b"\x01"
    quantidade = b"\x02"
    requisicao_invalida = b"\x03"

    mensagem_enviada = b""
    if opcao == "1":
        mensagem_enviada += data
    elif opcao == "2":
        mensagem_enviada += frase
    elif opcao == "3":
        mensagem_enviada += quantidade
    elif opcao == "4":
        exit(0)
    else:
        print("Opção inválida!")
        return

    random_number = random.randint(1, 65535)
    identificador = random_number.to_bytes(length=2, byteorder="big")
    mensagem_enviada += identificador

    udp = SocketUDP()
    udp.mandar_mensagem(mensagem_enviada)
    mensagem_recebida = udp.resposta
    if opcao == "1" or opcao == "2":
        mensagem_recebida = mensagem_recebida[4:-2]
        mensagem_recebida = mensagem_recebida.decode("utf-8")
    elif opcao == "3":
        mensagem_recebida = mensagem_recebida[-4:]
        mensagem_recebida = int.from_bytes(mensagem_recebida, byteorder='big', signed=False)
    print(mensagem_recebida)
    
    return



while(True):
    print("\nO que você deseja fazer? ")
    print("1) Solicitar Data e Hora atual.")
    print("2) Uma mensagem motivacional para o fim do semestre.")
    print("3) A quantidade de respostas emitidas pelo servidor até o momento.")
    print("4) Sair.")
    opcao = input("-> ")
    enviar_mensagem(opcao)