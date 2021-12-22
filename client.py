from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR

from common.helpers import get_local_ip


class Client:
    def __init__(self, server_ip, server_port):
        # create a tcp socket
        self.clientSocket = None
        print(f'--- Created socket ---')
        self.dataToSend = " "
        self.dataReceived = " "
        self.init_connection(server_ip, server_port)

    def init_connection(self, server_ip: str, server_port: int) -> None:
        """
        Initializes the connection between the client and th server
        :param server_ip:
        :param server_port:
        :return: None
        """
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        # initiate three-way tcp handshake with the server
        self.clientSocket.connect((server_ip, server_port))
        print(f'Connected to server: {(server_ip, server_port)}')

    def send_request(self, message_to_send: str) -> None:
        """
        Send messages to server
        :param message_to_send
        :return: None
        """
        self.clientSocket.sendall(message_to_send.encode())

    def get_response(self) -> str:
        """
        Receives messages from server
        :return: message
        """
        message = self.clientSocket.recv(1024).decode()
        print(f'server says: {message}\n')

        return message

    def find_record(self, national_id: str) -> str:
        """
        Searches for entries in database
        :param national_id:
        :return: Tuple with user info or User not found
        """
        self.send_request("search," + national_id)  # send them
        return self.get_response()  # get back the user

    def create_record(self, data) -> str:
        """
        Adds user data to the database
        :param data:
        :return: added successfully
        """
        self.send_request("add," + ','.join(map(str, data)))
        return self.get_response()

    def close_connection(self) -> None:
        """
        Closees the connection with the server
        :return: None
        """
        self.clientSocket.shutdown(SHUT_RDWR)
        self.clientSocket.close()
        print(f'-- End connection from client Side --')
        # sys.exit()


if __name__ == "__main__":
    # assuming server is on same machine of client ,this function gets the default local  IPv4 Address for any machine.
    serverIp = get_local_ip()
    serverPort = 8080

    # client = TCPClient(serverIp, serverPort)
    # client2 = TCPClient(serverIp, serverPort)
    # client.create(('18745634113345', 'test', '11125896336985224779', 'aaaa', 'ss'))
    # client2.find_one('18745634113345')
