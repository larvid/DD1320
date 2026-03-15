class Node:

    def __init__(self, x, next = None):
        self.data = x
        self.next = next

class Stack:

    def __init__(self):
        self.top = None

    def push(self, x):
        tmp = Node(x)
        tmp.next = self.top
        self.top = tmp
    
    def pop(self):
        if self.isEmpty():
            return None
        tmpdata = self.top.data
        self.top = self.top.next
        return tmpdata
    
    def isEmpty(self):
        return self.top == None