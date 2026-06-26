import socket
import threading
import time

ip = "127.0.0.1"

def scan(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    if s.connect_ex((ip, p)) == 0:
        print("Open:", p)

    s.close()

t = time.time()

ts = []

for i in range(1, 101):
    x = threading.Thread(target=scan, args=(i,))
    ts.append(x)
    x.start()

for x in ts:
    x.join()

print("Time:", time.time() - t)