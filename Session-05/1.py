import urllib.request
import threading
import time

u = [
    "https://picsum.photos/200",
    "https://picsum.photos/201",
    "https://picsum.photos/202",
    "https://picsum.photos/203",
    "https://picsum.photos/204"
]

def d(x, n):
    urllib.request.urlretrieve(x, f"img{n}.jpg")

s = time.time()

for i in range(len(u)):
    d(u[i], i)

e = time.time()

print("Normal:", e - s)

s = time.time()

ts = []

for i in range(len(u)):
    t = threading.Thread(target=d, args=(u[i], i))
    ts.append(t)
    t.start()

for t in ts:
    t.join()

e = time.time()

print("Thread:", e - s)