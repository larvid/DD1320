class Song:
    def __init__(self, trackid, time, artist, title):
        self.trackid = trackid
        self.time = time
        self.artist = artist
        self.title = title

    def __lt__(self, other):
        return self.title < other.title

    def __str__(self):
        return f"{self.artist}, {self.title}"
