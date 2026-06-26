import socket
import threading

cs = []

def client(c):

    while True:

        try:
            d = c.recv(1024)

            if not d:
                break

            for x in cs:
                if x != c:
                    x.send(d)

        except:
            break

    cs.remove(c)
    c.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 9999))

s.listen(5)

print("Server Started")

while True:

    c, a = s.accept()

    cs.append(c)

    t = threading.Thread(target=client, args=(c,))
    t.start()