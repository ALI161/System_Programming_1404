#Create Deadlock
# import threading
# import time

# a = threading.Lock()
# b = threading.Lock()

# def f1():
#     with a:
#         print("T1 Lock A")
#         time.sleep(1)
#         with b:
#             print("T1 Lock B")

# def f2():
#     with b:
#         print("T2 Lock B")
#         time.sleep(1)
#         with a:
#             print("T2 Lock A")

# t1 = threading.Thread(target=f1)
# t2 = threading.Thread(target=f2)

# t1.start()
# t2.start()

#------------------
import threading
import time

a = threading.Lock()
b = threading.Lock()

def f1():
    with a:
        print("T1 Lock A")
        time.sleep(1)
        with b:
            print("T1 Lock B")

def f2():
    with a:
        print("T2 Lock A")
        time.sleep(1)
        with b:
            print("T2 Lock B")

t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")