import random

values = [random.randint(0, 40) for _ in range(20)]
values.sort()

def exists(the_list, key):
    for i, x in enumerate(the_list):
        if x == key:
            return i
    return False

def binary_search(lista, key):
    if len(lista) == 0:
        return False
    middle = len(lista)//2
    if key == lista[middle]:
        return True
    else:
        if key > lista[middle]:
            return binary_search(lista[middle+1:], key)
        else:
            return binary_search(lista[:middle], key)

def siffersumma(n):
      if n == 0:  
         return 0
      else:               
         return n%10 + siffersumma(n//10)

x = 4

print(binary_search(values, x))

#print(siffersumma(x))
