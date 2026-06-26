import os

t = input("Text: ")

os.write(2, ("\033[31m" + t + "\033[0m\n").encode())