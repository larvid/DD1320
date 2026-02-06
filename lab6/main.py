from ClassFile import *
from SearchFile import *

import timeit

filename = "unique_tracks.txt"
song_list = readfile(filename)
halvLista = song_list[0:500000]
kvartsLista = song_list[0:250000]


def linj_sok(list, namn):
    n = len(list)
    print("Antal element =", n)
    sista = list[n - 1]
    testsong = sista.title
    print(namn)
    linjtid = timeit.timeit(stmt=lambda: linsok(list, testsong), number=100)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")


def bin_sok(list, namn):
    n = len(list)
    sista = list[n - 1]
    testsong = sista.title
    list.sort()
    print(namn)
    bintid = timeit.timeit(stmt=lambda: binsok(list, testsong), number=100)
    print("Binärsökningen tog", round(bintid, 4), "sekunder")


# linj_sok(song_list, "Hela listan")
# linj_sok(halvLista, "Halva listan")
# linj_sok(kvartsLista, "Kvarts lista")
bin_sok(song_list, "Hela listan")

# for song in song_list[:100]:
# print(song)
