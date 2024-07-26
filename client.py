# Create a TCP/IP socket for a client
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # send data
    message = 'New message. Please repeat also.'
    print('sending "%s"' % message)
    sock.sendall(bytes(message, 'utf-8'))

    # look for a response back
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1600)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing client')
    sock.close()
