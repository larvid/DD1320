
class Node:

    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class LinkedQ:

    def __init__(self, first = None, last = None):
        self.first = first
        self.last = last
    
    def enqueue(self, x):
        tmp = Node(x)
        if self.first == None:
            self.first = tmp
        else:
            self.last.next = tmp
        self.last = tmp

    def dequeue(self):
        if self.first == None:
            return None

        if self.first == self.last:
            tmp = self.first.val
            self.first = None
            self.last = None
            return tmp
        else:
            tmp = self.first.val
            self.first = self.first.next
            return tmp

    def isEmpty(self):
        return self.first == None
    
    def __str__(self):
        tmp = self.first
        while True:
            print(tmp.val)
            tmp = tmp.next
            if tmp == self.last:
                break

