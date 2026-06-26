import ctypes

m = ctypes.CDLL("libm.so.6")

m.pow.argtypes = [ctypes.c_double, ctypes.c_double]
m.pow.restype = ctypes.c_double

r = m.pow(2.0, 10.0)

print(r)