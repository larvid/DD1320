from array import array

class ArrayQ:

    def __init__(self):
        self._Q = array('i',[])
        self._first = None
        self._last = None
    
    def __str__(self):
        return str(self._Q)
    
    def enqueue(self, x):
        self._Q.append(x)

    def dequeue(self, i = 0):
        return self._Q.pop(0)
    
    def isEmpty(self):
        return len(self._Q) == 0