from ClassFile import *
from SearchFile import *
import timeit

filename = "unique_tracks.txt"
song_list = readfile_list(filename)
kvartsLista = song_list[0:250000]
hundra_kLista = song_list[0:100000]
tio_kLista = song_list[0:10000]
kLista = song_list[0:1000]

tims_tid = timeit.timeit(stmt=lambda: timsort(kLista), number=1)
print("timsort tog", round(tims_tid, 4), "sekunder")

tims_tid = timeit.timeit(stmt=lambda: timsort(tio_kLista), number=1)
print("timsort tog", round(tims_tid, 4), "sekunder")

tims_tid = timeit.timeit(stmt=lambda: timsort(hundra_kLista), number=1)
print("timsort tog", round(tims_tid, 4), "sekunder")

tims_tid = timeit.timeit(stmt=lambda: timsort(song_list), number=1)
print("timsort tog", round(tims_tid, 4), "sekunder")


# urvalstid = timeit.timeit(stmt=lambda: urvalssortera(kLista), number=1)
# print("urvalssorteringen tog", round(urvalstid, 4), "sekunder")

# urvalstid = timeit.timeit(stmt=lambda: urvalssortera(tio_kLista), number=1)
# print("urvalssorteringen tog", round(urvalstid, 4), "sekunder")

urvalstid = timeit.timeit(stmt=lambda: urvalssortera(hundra_kLista), number=1)
print("urvalssorteringen tog", round(urvalstid, 4), "sekunder")


# Sorteringsmetoderna stämmer med teorin om tidskomplexitet, där urvalssortering är O(n^2), när vi ökar n med en faktor 10 ökar tidskomplexiteten med en faktor 10^2
# Timsort, pythons inbyggda funktion fungerar som bäst som O(n), men i genomsnitt: O(n log (n)), vilket vi kan se i början stämmer då tidskomplexiteten ökar med en faktor 10, då log(faktorn) är liten, sen bidrar den med mer kostnad
# Tidssökningarna stämmer också relativt bra, linjärsökningen är linjär O(n), då när man halverar n halverar tiden. För binärsökningen O(log(n)) kan vi se att det verkar vara overhead-kostnaderna som spelar störst roll, men där tiden minskar marginellt med minskning av n
# För hashsökning tar det lika lång tid för samtliga sökningar och stämmer överens med teorin O(1),
