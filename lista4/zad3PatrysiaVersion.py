#! usr/bin/env python3
"""
funkcja dla pozbiorów k-elementowych, zbioru n-elementowego
gdy k jest większe niż 1, dzielimy zbiór na mniejsze częsci, a
następnie wywołujemy rekurencyjnie funkcję na tych podzbiorach.
Kolejnym krokiem jest dodanie 
"""
def podzbiory(k, n):
    if k==0:
        print(set())
    elif k==1:
        for i in range(1, n+1):
            yield {i}
    else:
        for i in podzbiory(k-1, n):
            for n in range (list(i)[k-2]+1,n+1):
                yield i | {n}


n=int(input("Wpisz ilość elementów w zbiorze: "))
k=int(input("Wpisz ilość elementów w podzbiorze: "))

for i in podzbiory(k, n):
    print(i)
