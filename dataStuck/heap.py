class Heap:
    def __init__(self):
        self.h = []
        self.size = 0
    def leftChild (self,i):
        if 2*i +1 < self.size:
            return 2*i +1
        return None
    def rightChild (self, i):
        if 2*i +2 < self.size:
            return 2*i+2
        return None
    def maxHeapify(self, node):
        if node < self.size:
            curNode= node
            lc = self.leftChild(node)
            rc = self.rightChild(node)
            if lc is not None and self.h[lc] > self.h[m]:
                m = lc
            if rc is not None and self.h[rc] > self.h[m]:
                m = rc
            if m!= node:
                self.h[node] , self.h[m] = self.h[m], self.h[node]
                self.maxHeapify(m)
    def buildHeap(self,a):
        self.size = len(a)
        self.h = list(a)
        for i in range(self.size // 2, -1, -1):
            self.maxHeapify(i)
    