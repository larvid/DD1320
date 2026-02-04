from BintreeFile import Bintree
from linkedQFile import LinkedQ


def makechildren(sökord, q, lista, gamla):

    bokstäver = "abcdefghijklmnopqrstuvxyzåäö"

    for i in range(len(sökord)):
        for bokstav in bokstäver:
            nytt_barn = sökord[:i] + bokstav + sökord[i + 1 :]
            if nytt_barn != sökord and nytt_barn not in gamla and nytt_barn in lista:
                parent[nytt_barn] = sökord
                q.enqueue(nytt_barn)
                gamla.put(nytt_barn)


svenska = Bintree()
gamla = Bintree()
parent = {}

with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        if ordet in svenska:
            pass
        else:
            svenska.put(ordet)

    svenska.makeBalanced()

    q = LinkedQ()

    startord = "mun"
    söktord = "bok"
    found = False

    q.enqueue(startord)

    while not q.isEmpty():
        nod = q.dequeue()
        if nod == söktord:
            print(söktord)
            break
        makechildren(nod, q, svenska, gamla)

    if found == False:
        ordet = söktord
        while True:
            print(parent[ordet])
            ordet = parent[ordet]
            if ordet == startord:
                break
