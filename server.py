import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1600)
            print('received "%s"' % data)
            if data:
                print('sending data back to the client')
                msg = str(data)
                msg = msg + ' plus extra from the server'
                msg = bytes(msg, 'utf-8')
                connection.sendall(msg)
            else:
                print('no more data from', client_address)
                connection.close()
                break

    finally:
        # Clean up the connection
        connection.close()
