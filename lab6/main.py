from ClassFile import *
from SearchFile import *

import timeit

filename = "unique_tracks.txt"
song_list = readfile(filename)
halvLista = song_list[0:500000]
kvartsLista = song_list[0:250000]


def linj_sok(lista, namn):
    n = len(lista)
    print("\nAntal element =", n)
    sista = lista[n - 1]
    testsong = sista.title
    print(namn)
    linjtid = timeit.timeit(stmt=lambda: linsok(lista, testsong), number=1000)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")


def bin_sok(lista, namn):
    n = len(lista)
    print("\nAntal element =", n)
    sista = lista[n - 1]
    testsong = sista.title
    print(namn)
    linjtid = timeit.timeit(stmt=lambda: binsok(lista, testsong), number=1000)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")


# linj_sok(kvartsLista, "Kvarts lista")
# linj_sok(halvLista, "Halva listan")
# linj_sok(song_list, "Hela listan")

bin_sok(song_list, "Hela listan")

# for song in song_list[:100]:
# print(song)
