maxValue = input("podaj gorny zakres")


if maxValue.isdigi():
	maxValue = int(maxValue)
else:
	print("podana wartosc jest niewlasciwego typu")

print(lista)	
def fun():
	primeList = []
	actualPrime = 2
	while(actualPrime < maxValue):
		actualPrime = lista[0]
		toDel = actualPrime
		primeList.append(actualPrime)
		while (toDel < 13):
			if toDel in lista:
				lista.remove(toDel)
			toDel += actualPrime
	return primeList

print(fun())

