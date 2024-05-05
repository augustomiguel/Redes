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
        random_number = random.randint(1, 65535)
        identificador = hex(random_number)
        
        # Remove o '0b' e preenche os números a esquerda até que tenham 16 dígitos
        identificador = identificador[2:].zfill(16)  
        primeiro_4bits = int(identificador[:4],16)
        segundo_4bits = int(identificador[4:8],16)
        terceiro_4bits = int(identificador[8:12],16)
        quarto_4bits = int(identificador[12:16],16)
        
        print(f'''identificador: {identificador}\n
        primeiro 4bits: {primeiro_4bits}\n
        segundo 4bits: {segundo_4bits}\n
        terceiro 4bits: {terceiro_4bits}\n
        quarto 4bits: {quarto_4bits}\n
        ''')


        mensagem_enviada += identificador
       

        udp = SocketUDP()
        udp.mandar_mensagem("\x00\x00\x11")
        mensagem_recebida = udp.resposta
        print(mensagem_recebida)
        mensagem_enviada = ""


    elif opcao == "2":
        pass
    elif opcao == "3":
        pass
    elif opcao == "4":
        print("Programa finalizado.")
        exit(0)
    else:
        print("Opcao inválida!")