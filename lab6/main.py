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
    testartist = sista.artist
    print(namn)
    linjtid = timeit.timeit(stmt=lambda: linsok(list, testartist), number=10000)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")


linj_sok(song_list, "Hela listan")
linj_sok(halvLista, "Halva listan")
linj_sok(kvartsLista, "Kvarts lista")

# for song in song_list[:100]:
# print(song)
