import random
import struct
import socket

serverIP = "15.228.191.109"
serverPort = 50000


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.connect(("8.8.8.8", 80))

        endereco_ip_local = s.getsockname()[0]

        return endereco_ip_local
    except Exception as e:
        print(f"Erro: {e}")
        return


def calcular_checksum(
    ip_origem,
    ip_destino,
    protocolo_transporte,
    comprimento_do_seguimento,
    porta_origem,
    porta_destino,
    payload,
):
    checksum = 0
    dados_checksum = (
        ip_origem
        + ip_destino
        + protocolo_transporte
        + comprimento_do_seguimento
        + porta_origem
        + porta_destino
        + payload
    )
    
    dados_checksum += struct.pack(">H",checksum)
    print("dados_checksum",dados_checksum)
    
    if len(dados_checksum) % 2 == 1:
        dados_checksum += b"\x00"

    for i in range(0, len(dados_checksum), 2):
        palavra = (dados_checksum[i] << 8) + dados_checksum[i + 1]
        checksum += palavra
    while checksum >> 16:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)
    return ~checksum & 0xFFFF


def cabecalho_udp(payload):
    ip_local = get_ip()
    ip_servidor = "15.228.191.109"

    ip_origem = struct.pack("!4B", *map(int, ip_local.split(".")))
    ip_destino = struct.pack("!4B", *map(int, ip_servidor.split(".")))

    protocolo_transporte = struct.pack(">H", 17)

    porta_origem = struct.pack(">H", 59155)
    porta_destino = struct.pack(">H", 50000)

    comprimento_do_seguimento = struct.pack(">H", 11)

    get_checksum = calcular_checksum(
        ip_origem,
        ip_destino,
        protocolo_transporte,
        comprimento_do_seguimento,
        porta_origem,
        porta_destino,
        payload,
    )
    get_checksum = int(get_checksum)
    checksum = struct.pack(">H", get_checksum)

    cabecalho_udp = porta_origem + porta_destino + comprimento_do_seguimento + checksum

    return cabecalho_udp


def criar_payload(opcao):
    data = 0
    frase = 1
    quantidade = 2

    tipo_requisicao = 0

    if opcao == "1":
        dados = tipo_requisicao | data
    elif opcao == "2":
        dados = tipo_requisicao | frase
    elif opcao == "3":
        dados = tipo_requisicao | quantidade
    else:
        print("Opção inválida!")
        return

    identificador = random.randint(1, 65535)
    payload = struct.pack(">BH", dados, identificador)

    return payload


def processar_resposta(opcao,mensagem_recebida):
    # mensagem_recebida = udp(mensagem_enviada)

    # decodificar mensagem
    if opcao == "1" or opcao == "2":
        mensagem_recebida = mensagem_recebida[28:-2]
        mensagem_recebida = mensagem_recebida.decode("utf-8")
    elif opcao == "3":
        mensagem_recebida = mensagem_recebida[-4:]
        mensagem_recebida = int.from_bytes(mensagem_recebida, byteorder="big", signed=False)
    print("payload recebido",mensagem_recebida)
    return payload


def main():
    while True:
        print("O que você deseja fazer? ")
        print("1) Solicitar Data e Hora atual.")
        print("2) Uma mensagem motivacional para o fim do semestre.")
        print("3) A quantidade de respostas emitidas pelo servidor até o momento.")
        print("4) Sair.")
        opcao = input("-> ")
        if opcao == '4':
            print("encerrando programa!")
            return
        payload = criar_payload(opcao)
        cabecalho = cabecalho_udp(payload)
        print("payload: ",payload)
        print("udp: ",cabecalho)
        mensagem = cabecalho + payload
        print("mensagem: ", mensagem)
        
        
        socket_cliente = socket.socket(
            socket.AF_INET,
            socket.SOCK_RAW,
            socket.IPPROTO_UDP,
        )

        socket_cliente.sendto(mensagem, (serverIP, serverPort))        
        
        # recebe a resposta
        resposta, _ = socket_cliente.recvfrom(4000)
        print(resposta)
        # processar_resposta(opcao,resposta)
        
        opcao = None

    
    
main()