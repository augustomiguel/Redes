import socket
import struct

# Define o formato da mensagem
class Mensagem:
    def __init__(self, tipo, id, payload):
        self.tipo = tipo
        self.id = id
        self.payload = payload

    def to_bytes(self):
        # Converte o tipo e o ID em bytes
        tipo_bytes = struct.pack('!H', self.tipo)
        id_bytes = struct.pack('!H', self.id)

        # Combina os bytes do tipo, ID e payload
        mensagem_bytes = tipo_bytes + id_bytes + self.payload

        return mensagem_bytes

    @classmethod
    def from_bytes(self, mensagem_bytes):
        # Extrai os bytes do tipo e do ID
        tipo_bytes, id_bytes = mensagem_bytes[:4]

        # Converte os bytes em valores numéricos
        tipo = struct.unpack('!H', tipo_bytes)[0]
        id = struct.unpack('!H', id_bytes)[0]

        # Extrai o payload
        payload = mensagem_bytes[4:]

        # Retorna um objeto Mensagem
        return Mensagem(tipo, id, payload)

# Função para enviar a requisição ao servidor
def enviar_requisicao(socket, mensagem, servidor_endereco):
    # Envia a mensagem para o servidor
    socket.sendto(mensagem.to_bytes(), servidor_endereco)

# Função para receber a resposta do servidor
def receber_resposta(socket):
    # Recebe a resposta do servidor
    resposta_bytes, servidor_endereco = socket.recvfrom(1024)

    # Converte os bytes da resposta em um objeto Mensagem
    resposta = Mensagem.from_bytes(resposta_bytes)

    return resposta

# Função para exibir a resposta ao usuário
def exibir_resposta(resposta):
    if resposta.tipo == 0:  # Data e hora
        data_hora = resposta.payload.decode('utf-8')
        print(f"Data e hora: {data_hora}")
    elif resposta.tipo == 1:  # Frase motivacional
        frase_motivacional = resposta.payload.decode('utf-8')
        print(f"Frase motivacional: {frase_motivacional}")
    elif resposta.tipo == 2:  # Número de respostas
        numero_respostas = struct.unpack('!I', resposta.payload)[0]
        print(f"Número de respostas: {numero_respostas}")
    elif resposta.tipo == 3:  # Requisição inválida
        print("Requisição inválida recebida pelo servidor.")
    else:
        print("Tipo de resposta desconhecido.")

# Cria o socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereço do servidor
servidor_endereco = ('15.228.191.109', 50000)

while True:
    # Solicita o tipo de requisição ao usuário
    tipo