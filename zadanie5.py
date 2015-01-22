#!/usr/bin/env python3
#Funkcja znajduje dzielniki danej liczby (różne od tej liczby)i zwraca ich sumę:
def findDivisors(number):
    totality=0
    for divisor in range(1,number):
        if number%divisor==0:
            totality+=divisor
    return totality

print("Liczby doskonałe mniejsze od 1000 to:")
for number in range(1,1000):
#Suma dzielników liczby doskonałej jest równa tej liczbie, stąd warunek:
    if number==findDivisors(number):
        perfect=number
        print(perfect)

print("Pary liczb zaprzyjaźnionych mniejszych od 1000 to:")
for number in range(1,1000):
    friend=findDivisors(number)
#Gdy suma dzielników sumy dzielników pewnej liczby jest równa tej liczbie,
#to liczba ta jest zaprzyjaźniona ze swoją sumą dzielników. Definiujemy warunek:
    if findDivisors(friend)==number and findDivisors(number)>number \
    and number!=perfect:
        print(number,"i",friend)
    

