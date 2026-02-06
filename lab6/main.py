from ClassFile import * 
from SearchFile import * 

import timeit 

filename = "unique_tracks.txt"
song_list = readfile(filename)
halvLista = song_list[0:500000]
kvartsLista = song_list[0:250000]

n = len(song_list)
print("Antal element =", n)
sista = song_list[n-1]
testartist = sista.artist
print("Hel lista")
tider = []
for _ in range(10):
    linjtid = timeit.timeit(stmt = lambda: linsok(song_list, testartist), number = 10000)
    tider.append(linjtid)
    #print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")
med_tid = sum(tider) / len(tider)
print("Medel-linjärsökningen tog", round(med_tid, 4) , "sekunder")






#for song in song_list[:100]:
    #print(song)

