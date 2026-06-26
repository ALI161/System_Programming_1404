import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("0.0.0.0", 9090))

print("Waiting...")

while True:
    d, a = s.recvfrom(1024)
    print("From:", a)
    print(d.decode())