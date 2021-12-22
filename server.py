import selectors
import types
from socket import socket, AF_INET, SOCK_STREAM

from common.helpers import get_local_ip
from database.db import VaccineDB


class MultiConnectionServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.dataBase = VaccineDB()
        # initiate a default selector to handle multiple connections
        self.sel = selectors.DefaultSelector()
        self.chatLoop()

    def find_one(self, national_id):
        return self.dataBase.find_one(national_id)

    def accept_wrapper(self, sock):
        # Since the listening socket was registered for the event selectors.EVENT_READ,
        # it should be ready to read. We call sock.accept()
        conn, addr = sock.accept()  # Should be ready to read
        print("accepted connection from", addr)
        conn.setblocking(False)
        # we create an object to hold the data we want included along with the socket
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        # Since we want to know when the client connection is ready for reading and writing,
        # both of those events are set in the events mask.
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        # then we register this connection to the selector
        self.sel.register(conn, events, data=data)

    def service_connection(self, key, mask):
        # key is the namedtuple returned from select() that contains the socket object (fileobj) and data object.
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            # If the socket is ready for reading, then mask & selectors.EVENT_READ is true, and sock.recv() is called
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                # Any data that’s read is appended to data.outb so it can be sent later.
                data.outb = recv_data
            else:
                # This means that the client has closed their socket, so the server should too.
                print("closing connection to", data.addr)
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            # When the socket is ready for writing,
            # which should always be the case for a healthy socket,
            # any received data stored in data.outb is processed and the answer is sent to the client
            if data.outb:
                print("processing", repr(data.outb), "to", data.addr)
                data_to_send = self.process_message(data.outb.decode())
                print(data_to_send)
                # Should be ready to write
                sent = sock.send(data_to_send.encode())
                # The bytes sent are then removed from the send buffer
                data.outb = None

    def process_message(self, message) -> str:
        print(f"message structure: {message}")
        if type(message) != str:
            message = message.decode()
        message_words = message.replace(" ", "").split(",")
        print(message_words)
        if len(message_words) > 0:
            if message_words[0] == "search":
                print("search mode")
                national_id = message_words[1]
                user = self.find_one(national_id)
                if user == 'User not found':
                    return user
                return ','.join(map(str, user))
            elif message_words[0] == "add":
                print("add mode")
                data = tuple(message_words[1:])
                user = self.dataBase.create_user(data)
                return user
            else:
                print("strange message structure")
        else:

            print("empty message")
            return message

    def chatLoop(self, host=None, port=None):
        if host == None:
            host = self.host
        if port == None:
            port = self.port

        lsock = socket(AF_INET, SOCK_STREAM)
        lsock.bind((host, port))
        lsock.listen()
        print("listening on", (host, port))
        # configure the socket in non-blocking mode
        # so, calls made to this socket will no longer block
        lsock.setblocking(False)
        # registering the socket to be monitored with sel.select() for the events we are interested in.
        # For the listening socket, we want read events --> selectors.EVENT_READ
        self.sel.register(lsock, selectors.EVENT_READ, data=None)

        try:
            while True:
                # blocks until there are sockets ready for I/O
                events = self.sel.select(timeout=None)
                # It returns a list of (key, events masks--> read or write or both) tuples, one for each socket.
                for key, mask in events:
                    # key is a SelectorKey namedtuple that contains a fileobj attribute.
                    # key.fileobj is the socket object, and mask is an event mask of the operations that are ready.
                    if key.data is None:
                        # print("wrapper called")
                        # then we know it’s from the listening socket and we need to accept() the connection.
                        self.accept_wrapper(key.fileobj)
                        # this wrapper function gets the new socket object and register it with the selector.
                    else:
                        # if key.data is not None, then we know it’s a client socket that’s already been accepted, and we need to service it.
                        # service_connection() is then called and passed key and mask,
                        # which contains everything we need to operate on the socket.
                        self.service_connection(key, mask)
        except KeyboardInterrupt:
            print("keyboard interrupt, exiting")
        finally:
            self.sel.close()


if __name__ == "__main__":
    # ------------------------ multiple connection server ------------------------ #
    print(f'ip : {get_local_ip()}')
    host, port = (get_local_ip(), 8080)
    MultiServer = MultiConnectionServer(host, port)
    # ---------------------------------------------------------------------------- #
