import numpy as np


def isprime(tal):
    span = np.ceil(np.sqrt(tal)).astype(int)
    print(span)
    for i in range(span - 1):
        if tal % (i + 2) == 0:
            return False
    return True


print(isprime(int(input())))
