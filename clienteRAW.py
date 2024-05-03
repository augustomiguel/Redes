import socket
import struct
serverName = "15.228.191.109"
serverPort = 50000

gerar_identificador():
    return random.randint(1, 65535)

class MensagemRAW:
    def __init__(self, tipo, id, payload):
        self.tipo = tipo
        self.id = id
        self.payload = payload

    def to_bytes(self):
        tipo_bytes = struct.pack('!H', self.tipo)
        id_bytes = struct.pack('!H', self.id)

        mensagem_bytes = tipo_bytes + id_bytes + self.payload

        return mensagem_bytes

    @classmethod
    def from_bytes(self, mensagem_bytes):
        tipo_bytes, id_bytes = mensagem_bytes[:4]

        tipo = struct.unpack('!H', tipo_bytes)[0]
        id = struct.unpack('!H', id_bytes)[0]

        payload = mensagem_bytes[4:]

        return MensagemRAW(tipo, id, payload)

    
    