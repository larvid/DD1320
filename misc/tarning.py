import random

class Tarning:

    def __init__(self, färg):
        self.färg = färg
        self.utfall = random.randint(1,6)

    def __repr__(self):
        pass

    def kasta(self):
        self.utfall = random.randint(1,6)

t1 = Tarning('Röd')
t2 = Tarning('Vit')

print(t1.utfall)
print(t2.utfall)

n = 5
tärningarna = list()
for i in range(n):
    tärningarna.append(Tarning('Gul'))

for i in range(n):
    tärningarna[i].kasta()
    print(tärningarna[i].utfall)