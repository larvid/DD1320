from BintreeFile import *
import random

tree = Bintree()

values = [random.randint(0, 40) for _ in range(29)]
#values.sort()
tree.makeTree(values)

my_list = tree.inorderlist(tree.root)
print(my_list)

tree.put(45)
tree.put(42)

tree.preorder()

print(len(tree))
print(tree._depth_())
print(tree.level_index())
tree.tree_list()