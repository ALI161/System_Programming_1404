import os
import time

for i in range(3):
    p = os.fork()

    if p == 0:
        if i == 0:
            os.system("ls")

        elif i == 1:
            f = open("test.txt", "w")
            f.write("Hello")
            f.close()

        else:
            time.sleep(5)
            print("Child 3 done")

        os._exit(0)
for i in range(3):
    os.wait()

print("end")