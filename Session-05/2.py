import threading
import time

b = 0

def add(x, n):
    global b

    for i in range(n):
        t = b
        time.sleep(0.001)
        b = t + x

t1 = threading.Thread(target=add, args=(1, 500))
t2 = threading.Thread(target=add, args=(1, 500))

t1.start()
t2.start()

t1.join()
t2.join()

print(b)