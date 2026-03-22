from formel import *
from linkedQFile import *
from molgrafik import *


def searches():
    while True:
        findme = input().strip()
        if findme == "#":
            break
        q = LinkedQ()
        q.mega_enqueue(findme)
        try:
            mol, vikt = readFormel(q)
            print("Formeln är syntaktiskt korrekt")
        except Syntaxfel as e:
            print(e)

        print("Molekylen väger " + str(vikt) + "u")
        print("Molekylen väger också " + str(weight(mol)) + "u")

        mg = Molgrafik()
        mg.show(mol)


if __name__ == "__main__":
    searches()
