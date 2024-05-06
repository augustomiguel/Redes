

from socket import *
from clienteRAW import SocketRAW
import binascii
import random

serverName = "15.228.191.109"
serverPort = 50000
def ip (udp):
    #codifica cabeçalho
    
    socket_raw = SocketRAW()
    mensagem_recebida = socket_raw.send_message(udp)
    
    #decodifica cabeçalho
    
    return mensagem_recebida
    
def udp(payload):
    #codifica cabeçalho
    
    
    mensagem_recebida = ip(payload)
    #decodifica cabeçalho
    return mensagem_recebida


def payload(opcao):
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
    #codificar mensagem
    random_number = random.randint(1, 65535)
    identificador = random_number.to_bytes(length=2, byteorder="big")
    mensagem_enviada += identificador

    mensagem_recebida = udp(mensagem_enviada)
    # decodificar mensagem
    if opcao == "1" or opcao == "2":
        mensagem_recebida = mensagem_recebida[4:-2]
        mensagem_recebida = mensagem_recebida.decode("utf-8")
    elif opcao == "3":
        mensagem_recebida = mensagem_recebida[-4:]
        mensagem_recebida = int.from_bytes(mensagem_recebida, byteorder='big', signed=False)
    return mensagem_recebida


while(True):
    print("O que você deseja fazer? ")
    print("1) Solicitar Data e Hora atual.")
    print("2) Uma mensagem motivacional para o fim do semestre.")
    print("3) A quantidade de respostas emitidas pelo servidor até o momento.")
    print("4) Sair.")
    opcao = input("-> ")
    if opcao != "1" or opcao != "2" or opcao != "3" or opcao != "4":
        print("Opção inválida!")
        continue
    else:
        payload = payload(opcao)
        udp = udp()
        ip = ip()
        udp += payload
        ip += udp
