class HashNode:
    """Noder till klassen Hashtable"""

    def __init__(self, key="", data=None):
        """key är nyckeln som anvands vid hashningen
        data är det objekt som ska hashas in"""
        self.key = key
        self.data = data


class Hashtable:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        self.table = [[] for _ in range(size)]

    def store(self, key, data):
        """key är nyckeln
        data är objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen."""
        index = self.hashfunction(key)
        bucket = self.table[index]

        for node in bucket:
            if node.key == key:
                node.data = data
                return

        tmp = HashNode(key, data)
        bucket.append(tmp)

    def search(self, key):
        """key är nyckeln
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska det bli KeyError"""
        index = self.hashfunction(key)
        bucket = self.table[index]

        for node in bucket:
            if node.key == key:
                return node.data

        raise KeyError

    def hashfunction(self, key):
        """key är nyckeln
        Beräknar hashfunktionen för key"""
        hash_val = 1663
        for char in key:
            hash_val = (((hash_val) << 5) - hash_val) + ord(char)

        hash_val = hash_val % self.size

        return hash_val

    def __contains__(self, key):
        bucket = self.table[self.hashfunction(key)]
        for node in bucket:
            if node.key == key:
                return True

    def __setitem__(self, key, data):
        self.store(key, data)

    def __getitem__(self, key):
        return self.search(key)
