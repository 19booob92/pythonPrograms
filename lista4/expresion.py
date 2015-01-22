import re
""
NUMBERS_TO_USE = [1,2,3,4]

SIZE = len(NUMBERS_TO_USE)
"Dozwolone operacje"
permitedOperations = ["+","-","*"]

"""
Zmienna przechowująca domniemane rozwiązanie
"""
exampleExpression = ""

"""
Metoda sprawdza czy przekazane jako argument
rozwiązanie, jest liczbą, czy wyrażeniem,
jeśli jest to wyrażenie, obejmuje je w nawiasy
"""
def needBracket(expression):
	if (1 in [c in expression for c in set(permitedOperations)]):
		return "(" + expression + ")"
	else:
		return expression

"""
Funkcja, której przekazujemy 
"""
def napisy(p,k,lista):#funkcja od poczatku, konca i listy
    global exampleExpression
    if k==p+1: yield str(lista[p])#jeśli koniec i poczatek sa obok siebie, to zwróć p-ty element listy
    else:#jeśli nie
        for i in range (p,k):#to dla kolejnych elementów od poczatku do konca
            for s in napisy(p,i,lista):#bierz czesc od poczaktku do i i dziel na kolejne mniejsze czesci
                for b in napisy(i, k, lista):# i od i do konca tak samo
                   for op in permitedOperations:
                      exampleExpression = needBracket(s) + op + needBracket(b) 
                      yield exampleExpression

"""
Funkcja zwraca elementy, których wartość jest
równa oczekiwanej wartości
"""
def zagadka(wynik):
    for i in napisy(0,SIZE,NUMBERS_TO_USE):
        if eval(i)==wynik:
            yield i

"""
Wypisanie wszystkich zwróconych rozwiązań
"""
for i in zagadka(15):
    print(i)

