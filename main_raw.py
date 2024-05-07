

import socket  
from clienteRAW import SocketRAW
import binascii
import random
import struct

serverPort=50000

def calcular_checksun (udp,payload):
    #codifica cabeçalho ip para calcular o checksun
    ip_servidor = "15.228.191.109"
    ip_destino = int.from_bytes(socket.inet_aton(ip_servidor),byteorder='big')
    
    ip_origem = str(socket.gethostbyname(socket.gethostname()))
    endereco_binario_origem =  int.from_bytes(socket.inet_aton(ip_origem),byteorder='big')
    protocolo_byte = b"\x00x0011"
    comprimento_udp = struct.pack('>H', 11)
    check = b"\x00"
   
    mens = endereco_binario_origem
    mens += ip_destino
    mens = protocolo_byte
    mens += comprimento_udp
    print("cabeçalho ip: ", mens)
    mens += udp
    mens += check
    print("cabeçalho ip + udp: ", mens)
    mens += payload
    
    
    checksun = 0
    
    if (len(mens) % 2 !=0):
        mens+=b"\x00" #* (len(mens) % 2)
        
    
    for i in range (0,len(mens),2):
        checksun += ((mens[i]<<8) + mens[i+1])
        checksun &= 0xFFFF

        if checksun > 0xFFFF0000:
            checksun = (checksun & 0xFFFF) + (checksun >> 16) + 1

    checksun = ~checksun & 0xFFFF
    return checksun
    
def udp(payload):
    #codifica cabeçalho
    porta_origem = struct.pack('>H',59155)
    print("porta origem",porta_origem)
    porta_destino = struct.pack('>H',50000)
    print("porta destino",porta_destino)
    comprimento_do_seguimento = struct.pack(">H", 11)
    print("Comprimento:" , comprimento_do_seguimento )
    
    mensagem = porta_origem
    mensagem += porta_destino 
    mensagem += comprimento_do_seguimento
    print("cabeçalho udp",mensagem)
    cheacksun = b"\x00x0000"
    check = calcular_checksun(mensagem,payload)
    print("checksum",check)
    #envia para colocar o pseudoIP e cacular o checksum
    
    checksun = struct.pack('!H',check )
    print("checksum byte",checksun)
    mensagem += checksun
    print("check",mensagem )
    
    mensagem +=payload
    print("datagrama : ",mensagem)
    
    #envia mensagem 
    socket_raw = SocketRAW()
    mensagem_recebida = socket_raw.send_message(mensagem)
    
    #decodifica cabeçalho
    mensagem_recebida = mensagem_recebida[-8:]
    print("upd resposta",mensagem_recebida)
    return mensagem_recebida





def payload(opcao):
    data = 0
    frase = 1
    quantidade = 2
    requisicao_invalida = 3
    tipo_requisicao = 0

    
    if opcao == "1":
        mensagem_enviada = tipo_requisicao | data
        print("tipo data:",data)
    elif opcao == "2":
        mensagem_enviada = tipo_requisicao | frase
        print("tipo frase:",frase)
    elif opcao == "3":
        mensagem_enviada = tipo_requisicao | quantidade
        print("tipo quantidade:",quantidade)
    else:
        print("Opção inválida!")
        return
    #codificar mensagem
    
    random_number = random.randint(1, 65535)
    #print(f'identificador: {random_number}')
    identificador = 60000
    mensagem_enviada = struct.pack(">BH", mensagem_enviada, identificador)
    
    print(f'tipo requisicao: {tipo_requisicao}')
    print(f'identificador: {identificador}')
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
    if opcao== 4:
        print("encerrando programa!")
    payload = payload(opcao)
    print("payload",payload)
    opcao=None
