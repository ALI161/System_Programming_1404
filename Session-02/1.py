import ctypes

u = ctypes.windll.user32
r = u.LockWorkStation()

print()