from formel import *
from linkedQFile import *


def searches():
    while True:
        findme = input().strip()
        if findme == "#":
            break
        q = LinkedQ()
        q.mega_enqueue(findme)
        try:
            readFormel(q)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as e:
            print(e)


searches()
