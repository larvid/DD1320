class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class Bintree:
    def __init__(self):
        self.root = None

    def __str__(self):
        pass

    def __len__(self, p = "root"):
        if p == "root":
            p = self.root
        if p is None:
            return 0
        return 1 + self.__len__(p.left) + self.__len__(p.right)
    
    def _depth_(self):
        return self._depth_helper(self.root) - 1
        
    def _depth_helper(self,p):
        if p is None:
            return 0
        return 1 + max(self._depth_helper(p.left), self._depth_helper(p.right))
        
    
    def write(self, p = "root"):
        if p == "root":
            p = self.root
        if p is not None:
            self.write(p.left)
            print(p)
            self.write(p.right)
    
    def preorder(self, p = "root", depth = 0):
        if p == "root":
            p = self.root
        if p is not None:
            print("  " * depth + str(p.value))
            self.preorder(p.left, depth + 1)
            self.preorder(p.right, depth + 1)

    def postorder(self, p = "root"):
        if p == "root":
            p = self.root
        if p is not None:
            self.postorder(p.left)
            self.postorder(p.right)
            print(p)
        
    def level_index(self, p = "root", depth = 0):
        if p == "root":
            p = self.root
        if p is not None:
            return [(depth,p) + self.level_index(p.left, depth + 1) + self.level_index(p.right, depth + 1)]

    def inorderlist(self, p = "root"):
        if p == "root":
            p = self.root
        if p is None:
            return []
        return self.inorderlist(p.left) + [p.value] + self.inorderlist(p.right)

    def __contains__(self, val, p = "root"):
        if p == "root":
            p = self.root
        if p is None:
            return False
        if p.value == val:
            return True
        
        if p.value > val:
            return self.__contains__(val, p.left)
        if p.value < val:
            return self.__contains__(val, p.right)
    
    def put(self, val):
        my_list = self.inorderlist() + [val]
        my_list.sort()
        self.makeTree(my_list)
        
    def makeTree(self, my_list, depth = 0):
        if not my_list:
            return None
        length = len(my_list)
        middle = (length // 2)
        tmp = Node(my_list[middle])
        if depth == 0:
            self.root = tmp
        if len(my_list) == 1:
            return tmp
        tmp.left = self.makeTree(my_list[:middle], depth + 1)
        tmp.right = self.makeTree(my_list[middle+1:], depth + 1)
        return tmp