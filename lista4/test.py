def permute(alist):
    if len(alist) <= 1:
        yield alist
        alist = set()

    for s in alist:
        rest = set(alist)
        tmp = set()
        for o in range(s):
            tmp | {rest.pop()}
        rest.pop()
        rest = tmp | rest
        for p in permute(rest):
            yield p | {s}

for p in permute({1,2,3}):
	print(p)

