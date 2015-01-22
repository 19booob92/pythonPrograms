n = int(input("Wpisz liczbę n, dla której znajdziemy rozwiązanie zagadki: "))
solution = int(input("Wpisz liczbę, której ma się równać wyrażenie: "))

"""
Program wstawia wszystkie możliwe ułożenia liczb z danego przedziału,
pomiędzy nawiasy, po czym sprawdza czy otrzymane równanie spełnia warunek
równości, następnie wykonywane są wywołania rekurencyjne, które wstawiają
wcześniej otrzymane równania, pomiędzy nawiasy, przez co otrzymujemy nowe
równania.
"""
def evals(p,k,numbersList):
    if k==p+1: yield str(numbersList[p])
    else:
        for i in range (p,k):
            for s in evals(p,i,numbersList):
                for b in evals(i, k, numbersList):
                   for op in ["-", "*", "+"]:
                       yield "("+s+")"+op+"("+b+")"
                       yield "" + s+op+b
def quest(numbers, solution):
    for i in evals(0,len(numbers),numbers):
        if eval(i)==solution:
            yield i

for i in quest(list(range(1, n+1)), solution):
    print(i)

