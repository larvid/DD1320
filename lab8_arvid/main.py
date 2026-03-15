from molekyl import *
from linkedQFile import *


def searches():
    while True:
        findme = input().strip()
        if findme == "#":
            break
        q = LinkedQ()
        q.mega_enqueue(findme)
        try:
            readMolekyl(q, findme)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as e:
            print(e)


searches()
