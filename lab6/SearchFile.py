from ClassFile import *
def linsok(lista, key):
    for song in lista:
        if song.artist == key:
            return song
    return None
    

def readfile(filename):
    lista = []
    with open(f"{filename}", "r", encoding="utf-8") as songfil:
        for rad in songfil:
            delar = rad.strip().split("<SEP>")
            song = Song(trackid=delar[0], time=delar[1], artist=delar[2], title=delar[3])
            lista.append(song)
        return lista
