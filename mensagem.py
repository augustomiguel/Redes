import binascii
import struct

gerar_identificador():
    return random.randint(1, 65535)

class MensagemUDP:
    def __init__(self, tipo, payload):
        self.tipoE = 0000
        self.id = gerar_identificador()
        self.payload = payload

    def para_bytes(self):
        tipo_bytes = struct.pack('!H', self.tipoE)
        id_bytes = struct.pack('!H', self.id)
        tamanho_resposta_bytes = struct.pack('!B', len(self.payload))

        # Calculate checksum
        checksum = binascii.crc32(tipo_bytes + id_bytes + tamanho_resposta_bytes + self.payload)
        checksum_bytes = struct.pack('!I', checksum)  # Pack checksum as unsigned int (4 bytes)

        mensagem_bytes = tipo_bytes + id_bytes + tamanho_resposta_bytes + self.payload + checksum_bytes

        return mensagem_bytes

    def de_bytes(self, mensagem_bytes):
        # ... existing code ...
        # Extract and verify checksum
        checksum_bytes = mensagem_bytes[-4:]
        expected_checksum = struct.unpack('!I', checksum_bytes)[0]
        actual_checksum = binascii.crc32(mensagem_bytes[:-4])

        if expected_checksum != actual_checksum:
            raise ValueError("Checksum mismatch!")  # Raise exception for invalid data



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
