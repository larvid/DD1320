from ClassFile import *


def linsok(lista, key):
    for song in lista:
        if song.artist == key:
            return song
    return None


def binsok(lista, key):
    low = 0
    high = len(lista) - 1

    while low <= high:
        # Hitta mitten utan att skapa en ny lista
        mid = (low + high) // 2
        current_title = lista[mid].title

        if current_title == key:
            return lista[mid]  # Hittad!

        elif current_title < key:
            # Sök i höger halva genom att flytta den nedre gränsen
            low = mid + 1
        else:
            # Sök i vänster halva genom att flytta den övre gränsen
            high = mid - 1

    return None  # Om vi kommer hit finns inte 'key' i listan


def readfile(filename):
    lista = []
    with open(f"{filename}", "r", encoding="utf-8") as songfil:
        for rad in songfil:
            delar = rad.strip().split("<SEP>")
            song = Song(
                trackid=delar[0], time=delar[1], artist=delar[2], title=delar[3]
            )
            lista.append(song)
        return lista
