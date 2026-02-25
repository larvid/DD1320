def utskrift(lista):
    if len(lista) > 0:
        print(lista[0])
        print(lista[1:])
        utskrift(lista[1:])


def omvänd(lista):
    if len(lista) > 0:
        omvänd(lista[1:])
        print(lista[0])
        print(lista[1:])


utskrift([1, 2, 3, 4, 5])
print("________________________________")
omvänd([1, 2, 3, 4, 5])
