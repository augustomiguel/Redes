

import socket  
from clienteRAW import SocketRAW
import binascii
import random
import struct

serverPort = 50000
ip_origem = str(socket.gethostbyname(socket.gethostname()))
ip_numerico_origem = [int(x) for x in ip_origem.split('.')]
# Empacote o endereço IP
endereco_binario_origem = struct.pack('!BBBB', *ip_numerico_origem)

ip_servidor = "15.228.191.109"
# Divida o endereço IP em seus componentes numéricos
ip_numerico = [int(x) for x in ip_servidor.split('.')]
# Empacote o endereço IP
endereco_binario = struct.pack('!BBBB', *ip_numerico)

comprimento_udp = "0x000B"
# Empacote o endereço IP
comprimento_binario = struct.pack('!BBBB', *ip_numerico)


def calcular_checksun (udp,payload):
    #codifica cabeçalho ip para calcular o checksun
    ip_origem = endereco_binario_origem # endereço de origem
    ip_destino = endereco_binario
    comprimento_udp = comprimento_binario
    mens = ip_origem
    mens += ip_destino
    mens += comprimento_udp
    mens += udp
    mens += payload
    print("ip",mens)
    
    checksun = 0
    
    if (len(mens) % 2 !=0):
        mens+=b"\x00"
    
    for i in range (0,len(mens),2):
        checksun = mens[i] + mens[i+1]
        checksun &= 0xFFFF

        if checksun > 0xFFFF:
            checksun = (checksun & 0xFFFF0000) + (checksun >> 16) + 1

    checksun = ~checksun & 0xFFFF
    return checksun
    
def udp(payload):
    #codifica cabeçalho
    porta_origem = struct.pack('>H',8080)
    print("origem",porta_origem)
    porta_destino = struct.pack('>H',serverPort)
    print("destino",porta_destino)
    comprimento_do_seguimento = comprimento_binario
    mensagem = porta_origem
    mensagem += porta_destino 
    mensagem += comprimento_do_seguimento
    print(mensagem)
    cheacksun = "0x0000"
    check = calcular_checksun(mensagem,payload)
    print(check)
    checksun = struct.pack('>H',check )
    print(checksun)
    mensagem += checksun
    print("check",mensagem )
    
    mensagem +=payload
    print("udp",mensagem)
    
    #envia mensagem para colocar o cabeçalho ip
    socket_raw = SocketRAW()
    mensagem_recebida = socket_raw.send_message(mensagem)
    
    #decodifica cabeçalho
    mensagem_recebida = mensagem_recebida[-8:]
    print("upd resposta",mensagem_recebida)
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
    print("payload",mensagem_enviada)
    
    mensagem_recebida = udp(mensagem_enviada)
    # decodificar mensagem
    if opcao == "1" or opcao == "2":
        mensagem_recebida = mensagem_recebida[4:-2]
        mensagem_recebida = mensagem_recebida.decode("utf-8")
    elif opcao == "3":
        mensagem_recebida = mensagem_recebida[-4:]
        mensagem_recebida = int.from_bytes(mensagem_recebida, byteorder='big', signed=False)
    #print("payload recebido",mensagem_recebida)
    return mensagem_recebida


while(True):
    print("O que você deseja fazer? ")
    print("1) Solicitar Data e Hora atual.")
    print("2) Uma mensagem motivacional para o fim do semestre.")
    print("3) A quantidade de respostas emitidas pelo servidor até o momento.")
    print("4) Sair.")
    opcao = input("-> ")

    payload = payload(opcao)
    print("payload",payload)
