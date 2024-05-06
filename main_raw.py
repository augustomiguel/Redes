

from socket import *
from clienteRAW import SocketRAW
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
        pass

    elif opcao == "2":
       pass
       
    elif opcao == "3":
        pass
        
    elif opcao == "4":
        print("Programa finalizado.")
        exit(0)
    else:
        print("Opcao inválida!")