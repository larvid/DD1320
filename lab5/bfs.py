from BintreeFile import Bintree
from linkedQFile import LinkedQ


class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent


def makechildren(nod, q, lista, gamla):

    bokstäver = "abcdefghijklmnopqrstuvxyzåäö"

    sökord = nod.word

    for i in range(len(sökord)):
        for bokstav in bokstäver:
            nytt_barn = sökord[:i] + bokstav + sökord[i + 1 :]
            if nytt_barn != sökord and nytt_barn not in gamla and nytt_barn in lista:
                tmp = ParentNode(nytt_barn, nod)
                q.enqueue(tmp)
                gamla.put(nytt_barn)


def writechain(nod):
    print(nod.word)
    if nod.parent == None:
        return
    writechain(nod.parent)


svenska = Bintree()
gamla = Bintree()

with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)

    svenska.makeBalanced()

    q = LinkedQ()

    startord = input()
    söktord = input()
    print("\n")
    found = False

    start = ParentNode(startord)

    q.enqueue(start)

    while not q.isEmpty():
        nod = q.dequeue()
        if nod.word == söktord:
            found = True
            slutordsnod = nod
            break
        makechildren(nod, q, svenska, gamla)

    if not found:
        print("Ingen väg hittades")
    else:
        writechain(slutordsnod)
