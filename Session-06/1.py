import threading
import time

b = 1000
l = threading.Lock()

def w(x):
    global b
    with l:
        if b >= x:
            t = b
            time.sleep(0.2)
            b = t - x
            print("Withdraw:", x, "Balance:", b)
        else:
            print("Not enough balance")

t1 = threading.Thread(target=w, args=(300,))
t2 = threading.Thread(target=w, args=(500,))
t3 = threading.Thread(target=w, args=(400,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Final Balance:", b)