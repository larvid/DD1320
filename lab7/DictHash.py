class DictHash:

    def __init__(self):
        self.uppslag = {}

    def store(self, nyckel, data):
        self.uppslag[nyckel] = data

    def search(self, nyckel):
        return self.uppslag.get(nyckel)

    def __contains__(self, nyckel):
        if self.uppslag.get(nyckel):
            return True

    def __getitem__(self, nyckel):
        return self.search(nyckel)


class Drama:
    def __init__(
        self,
        name,
        rating,
        actors,
        viewership_rate,
        genre,
        director,
        writer,
        year,
        no_of_ep,
        network,
    ):
        self.name = name
        self.rating = rating
        self.actors = actors
        self.viewership_rate = viewership_rate
        self.genre = genre
        self.director = director
        self.writer = writer
        self.year = year
        self.no_of_ep = no_of_ep
        self.network = network

    def __str__(self):
        return (
            f"--- Drama Info ---\n"
            f"Namn:           {self.name}\n"
            f"Betyg:          {self.rating}/10\n"
            f"Skådespelare:   {self.actors}\n"
            f"Tittarsiffror:  {self.viewership_rate}\n"
            f"Genre:          {self.genre}\n"
            f"------------------"
        )
