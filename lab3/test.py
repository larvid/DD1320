from BintreeFile import *
import random

tree = Bintree()

values = [random.randint(0, 40) for _ in range(20)]
#values.sort()

print(values)
tree.makeTree(values)

tree.write()

my_list = tree.inorderlist(tree.root)
print(my_list)

tree.put(45)
tree.put(42)
tree.write()

print(tree.__contains__(45))

tree.preorder()