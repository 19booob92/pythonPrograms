from math import cos
from math import fabs

def rozwiazanie(fun, a,b,eps):
	fa = fun(a)
	fb = fun(b)
	
	if (fa * fb < 0):
		while(1==1):
			x0 = (a+b)/2
			f0 = fun(x0)

			if (fabs(f0) < eps):
				return (x0, f0)
			if (fa * f0 < 0):
				b = x0
			else:
				a = x0
	else:
		print ("warunek nie jest spelniony")

def funkcja(x):
	return cos(x/2)


for k in range(1, 9):
	result = rozwiazanie(funkcja, 2,4,10**(-k))

	print ("eps wynosi: " , 10**(-k) , "x0 wynosi: " , result[0], "wynik dla funkcji: " , result[1])

