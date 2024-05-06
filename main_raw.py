

from socket import *
from clienteRAW import SocketRAW
import binascii
import random
import struct

serverName = "15.228.191.109"
serverPort = 50000
    


def ip (udp,payload):
    #codifica cabeçalho
    ip_origem= b"\x103870" # endereço de origem
    ip_destino= b"\x38BABC185" 
    comprimento_udp =b"\x00x000B"
    mensagem = ip_origem
    mensagem += ip_destino
    mensagem += comprimento_udp
    mensagem += udp
    mensagem += payload
    print("ip",mensagem)
    
    checksun = 0

    # Iterate over each byte in the message
    for byte in mensagem:
        checksun += byte  # Add the byte value to the checksum
        checksun &= 0xFFFF  # Apply wraparound (modulo 2^16)
        if checksun & 0xFFFF0000:
            checksun = (checksun & 0xFFFF0000) + 1
    
    return checksun
    
def udp(payload):
    #codifica cabeçalho
    porta_origem = b"\x1F90"
    porta_destino = b"\x00xC350"
    comprimento_do_seguimento = b"\x00x000B"
    mensagem = porta_origem
    mensagem += porta_destino 
    mensagem += comprimento_do_seguimento
    check = ip(mensagem,payload)
    print(check)
    checksun = struct.pack('>H',check )
    mensagem += checksun
    
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
