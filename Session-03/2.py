import os

p = "/proc/cpuinfo"

if os.path.exists(p):
    f = open(p, "r")
    c = 0

    for i in f:
        if i.startswith("processor"):
            c += 1

    f.close()
    print("CPU Cores:", c)

else:
    print("Linux only")