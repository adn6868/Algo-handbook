import functools

def synchronized(lock):
    def wrap (f):
        @functools.wraps(f)
        def newFunction (*args, **kw):
            with lock:
                return f(*args, **kw)
        return newFunction
    return wrap

    # ==========
import threading
lock = threading.Lock()

@synchronized(lock)
def taskA():
    print ("Hi")
    # pass
@synchronized(lock)
def taskB():
    print ("Hello")
    pass
