from DictHash import *
from hashtable import *
import csv

korean_movies = DictHash()
korean_movies_hash = Hashtable(997)

with open("kdrama.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        tmp = Drama(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
        )

        korean_movies.store(tmp.name, tmp)
        korean_movies_hash.store(tmp.name, tmp)

# movie = korean_movies["Be my boyfriend"]
movie = korean_movies_hash.search("Be my boyfriend")

movie2 = korean_movies_hash.search("Lawless Lawyer")

print(korean_movies["Transformers 7"])

print(movie)
print(movie2)
