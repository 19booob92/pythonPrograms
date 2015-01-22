given = int(input("Wpisz zakres: "))

allValues = [1]*(given+1)

squared=int(given**0.5)

allValues[0] = allValues[1] = 0

for i in range(2, squared+1):
	if allValues[i] == 1:
		w = i**2
		while (w <= given):
	
			allValues[w] = 0
			w += i
			
print(allValues.count(1))

for i in range (0, given+1):
	if (allValues[i] == 1):
		print(i, end=", ")

