def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
n=int(input("Wpisz n, dla których program wydrukuje permutacje zbioru n-elementowego: "))
for i in all_perms(list(range(1,n+1))):
	print(i)

