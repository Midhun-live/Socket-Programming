import socket


def srv():
    # config socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(('0.0.0.0', 8081))

    sock.listen()
    print('listening...')

    conn, addr = sock.accept()
    print('Client connected.')

    while True:
        print(conn.recv(1024).decode())
        conn.send(input('Enter text to send: ').encode())


def client():
    # config socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(('localhost', 8081))
    print('connected')

    while True:
        mess = input('Enter text to send: ').encode()
        sock.send(mess)
        print(sock.recv(1024).decode())


a = input('srv or cli?: ')
if a == 'srv':
    srv()
elif a == 'cli':
    client()