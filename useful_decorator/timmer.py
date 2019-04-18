import sys
from time import time
O = sys.stdout
def timmer(func):
    def f(*args, **kw):
        startTime = time()
        rv = func(*args, *kw)
        endTime = time()
        O.write("Elapse time %s \n" % (endTime-startTime))
        return rv
    return f

@timmer
def adding(a,b):
    return a + b

adding(1,2)
adding(3,4)


