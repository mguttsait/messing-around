import socket

def fetchHostDetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return host_name, host_ip