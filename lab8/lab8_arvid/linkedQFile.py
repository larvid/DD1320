class Node:

    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class LinkedQ:

    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def get_rest(self):
        string = ""
        while self.peek() is not None:
            val = self.dequeue()
            string += val
        return string

    def peek(self):
        if self.first is None:
            return None
        return self.first.val

    def enqueue(self, x):
        tmp = Node(x)
        if self.first is None:
            self.first = tmp
        else:
            self.last.next = tmp
        self.last = tmp

    def mega_enqueue(self, list):
        for i in range(len(list)):
            self.enqueue(list[i])

    def dequeue(self):
        if self.first is None:
            return None

        if self.first is self.last:
            tmp = self.first.val
            self.first = None
            self.last = None
            return tmp
        else:
            tmp = self.first.val
            self.first = self.first.next
            return tmp

    def isEmpty(self):
        return self.first is None

    def show(self):
        if self.isEmpty():
            return None
        tmp_list = []
        tmp = self.first
        while tmp is not None:
            tmp_list.append(tmp.val)
            tmp = tmp.next
        return tmp_list
