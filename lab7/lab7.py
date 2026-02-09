from DictHash import *
import csv

korean_movies = DictHash()

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

movie = korean_movies["Be my boyfriend"]

print(korean_movies["Transformers 7"])

print(movie)
