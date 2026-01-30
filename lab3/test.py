from BintreeFile import *
import random

tree = Bintree()

values = [random.randint(0, 40) for _ in range(29)]
values.sort()
tree.makeTree(values)

tree.put(43)
tree.put(34)

tree.tree_list()
tree.makeBalanced()
tree.tree_list()