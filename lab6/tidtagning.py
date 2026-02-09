from ClassFile import *
from SearchFile import *

import timeit

filename = "unique_tracks.txt"
song_list = readfile_list(filename)
halvLista = song_list[0:500000]
kvartsLista = song_list[0:250000]
song_dict = create_dict(song_list)
song_dict_half = create_dict(halvLista)
song_dict_quarter = create_dict(kvartsLista)
# halvDict = song_dict[0:500000]


def linj_sok(lista, namn):
    n = len(lista)
    print("\nAntal element =", n)
    sista = lista[n - 1]
    testsong = sista.title
    print(namn)
    linjtid = timeit.timeit(stmt=lambda: linsok(lista, testsong), number=100)
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")


def bin_sok(lista, namn):
    n = len(lista)
    print("\nAntal element =", n)
    sista = lista[n - 1]
    testsong = sista.title
    lista.sort()
    print(namn)
    bintid = timeit.timeit(stmt=lambda: binsok(lista, testsong), number=10000)
    print("Binärsökningen tog", round(bintid, 4), "sekunder")


def hash_sok(dictionary, namn):
    n = len(dictionary)
    print("\nAntal element =", n)

    testsong = next(iter(dictionary.keys()))
    print(namn)
    hashtid = timeit.timeit(stmt=lambda: hashsok(dictionary, testsong), number=10000)
    print("hashsökningen tog", round(hashtid, 4), "sekunder")


linj_sok(song_list, "Hela listan")
linj_sok(halvLista, "Halva listan")
linj_sok(kvartsLista, "Kvarts lista")

bin_sok(song_list, "Hela listan")
bin_sok(halvLista, "Halva listan")
bin_sok(kvartsLista, "Kvarts lista")

hash_sok(song_dict, "Hela listan")
hash_sok(song_dict_half, "Hela listan")
hash_sok(song_dict_quarter, "Hela listan")
