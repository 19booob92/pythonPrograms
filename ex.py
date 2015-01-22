from datetime import datetime

def getDivSum(num):
	sum = 0
	for i in range(1,num):
		if (num % i == 0):
			sum += i
	return sum

def isPerf(num):
	if (num == getDivSum(num)):
		print (num)

start = datetime.now().microsecond

lista = []
lista2 = list(range(1,1001))
for i in range(1,1001):
	isPerf(i)
	lista.append(getDivSum(i))

for j in lista2:
	pos = 0
	if j in lista:
		pos = lista.index(j) + 1
		if getDivSum(j) == pos and j != pos:
			print(pos,j)
			lista.remove(pos)
stop = datetime.now().microsecond

print (stop - start , "[micro kurwa sekund]")
