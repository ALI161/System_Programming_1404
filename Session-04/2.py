import subprocess

while True:
    x = input("Program: ")

    if x == "exit":
        break

    try:
        subprocess.Popen(x)
    except:
        print("Error")