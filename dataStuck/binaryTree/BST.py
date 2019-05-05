from time import time
def timeDec(func):
    def f(*args, **kwargs):
        sTime = time()
        rv = func(*args, **kwargs)
        eTime= time()
        print("Elapse time : ", eTime - sTime)
        return rv
    return f


class Node:
    def __init__(self, data = None):
        self.data = data
        self.r = None
        self.l = None
    def add(self,data):
        if data <= self.data:
            if self.l == None:
                self.l = Node(data)
            else:
                self.l.add(data)
        else:
            if self.r == None:
                self.r = Node(data)
            else:
                self.r.add(data)
    def __str__(self):
        if self.l == self.r == None:
            return str(self.data)
        elif self.l == None:
            return'[%s: ,%s]' % (str(self.data), str(self.r))
        elif self.r == None:
            return'[%s:%s, ]' % (str(self.data), str(self.l))
        else:
            return'[%s:%s,%s]' % (str(self.data), str(self.l), str(self.r))
        
    def _repr(self,depth=0):
        ans = ''
        if self.data == None:
            return ''
        tab = '| '*depth
        R = 'None'
        L = 'None'
        if self.l: 
            L = self.l._repr(depth + 1)  
        if self.r: 
            R = self.r._repr(depth + 1)
        ans = '''%s---%s\n%s|--%s'''% ( str(self.data), L,tab, R)
        return ans

    def __repr__(self):
        return (self._repr(0))

@timeDec
def toString(aNode):
    return str(aNode)

a = Node(3)
a.add(7)
a.add(5)
a.add(6)
a.add(1)
a.add(2)
a.add(4)
print (toString(a))
