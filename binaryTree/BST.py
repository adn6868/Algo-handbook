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
# '''
# problem: print out BST beauty
# solution:
# overload __pre__ with extra variable
# currently failing and are looking for new solution
# pass vao trong day mot cai varible de dem tab

# nen se tao ra 1 cai wrapper around cai __pre__ goi la _repr(self, depth) return (node repr, tab)
# c= _repv
# ans = ans + c[1]*' ' +c[2]  
# muon implement
# '''
    # def __len__(self):
    #     '''
    #     number of Node 
    #     '''
    #     if (self.data is None):
    #         return 0
    #     if (self.l == None and self.r == None):
    #         pass
    #     else:
    #         return 1 + len(self.l) + len(self.r)
        
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
    


        # if self.l == self.r == None:
        #     return repr(self.data)
        # tab = depth * '  '
        # return "%s %s--%s \n |_%s "% (tab,repr(self.data),repr(self.r,depth+1),repr(self.l,depth+1))



a = Node(3)
a.add(7)
a.add(5)
a.add(6)
# a.add(1)
# a.add(2)
# a.add(4)
# b= repr(a)
# print (b)
print(repr(a))
