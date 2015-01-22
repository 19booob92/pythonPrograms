def kombinacje(n, k):
	if k == 0:
		yield set()
	else:
		for x in kombinacje(n, k-1):
			if x == set():
				start = 1
			else:
				start = x[-1] + 1
i			for i in range(start, n+1):
				yield {i} | x


for itera in kombinacje(5, 3):
	print(itera)



#1,2,3,4,5

