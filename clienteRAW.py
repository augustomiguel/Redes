import socket
import struct
server_address = "15.228.191.109"
serverPort = 50000


class SocketRAW:
    raw_socket = None

    def send_message(self, message):
        # Convert message to MensagemRAW object
        

        # Convert MensagemRAW object to bytes
        message_bytes = mensagem_raw.to_bytes()

        # Send the message to the server
        sel.raw_socket.sendto(message_bytes, server_address)


    def criar_raw_socket(self,protocol=socket.IPPROTO_RAW):
        try:
            # Create a socket with AF_INET (IPv4) address family and SOCK_RAW socket type
            self.raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, protocol)

            # Set SO_REUSEADDR option to allow reusing the same address
            self.raw_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            return raw_socket
        except OSError as e:
            raise OSError(f"Failed to create raw socket: {e}")


