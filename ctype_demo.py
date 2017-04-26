from ctypes import *
import ctypes as c

mydll = c.WinDLL('user32')
myfunc = mydll['MessageBoxA']

myfunc.argtypes = (c.c_long, c.c_char_p, c.c_char_p, c.c_uint)
myfunc.restype = c.c_int
res = myfunc(0, "test", "message", 0)


