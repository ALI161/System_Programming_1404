import threading
import time

s = threading.Semaphore(3)

def d(n):
    print("User", n, "waiting")

    with s:
        print("User", n, "downloading")
        time.sleep(3)
        print("User", n, "done")

for i in range(6):
    t = threading.Thread(target=d, args=(i,))
    t.start()