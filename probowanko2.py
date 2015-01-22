#!/usr/bin/env python3
#Funkcja znajduje dzielniki danej liczby (różne od tej liczby).
from datetime import datetime

def findDivisors(number):
    totality=0
    for divisor in range(1,number):
        if number%divisor==0:
            totality+=divisor
    return totality

start = datetime.now().microsecond
print("Liczby doskonałe mniejsze od 1000 to:")
for number in range(1,1000):
    if number==findDivisors(number):
        perfect=number
        print(perfect)
        
print("Pary liczb zaprzyjaźnionych mniejszych od 1000 to:")
for number in range(1,1000):
    friend=findDivisors(number)
    if findDivisors(friend)==number and findDivisors(number)>number \
    and number!=perfect:
        print(number,"i",friend)
    
stop = datetime.now().microsecond
print(stop - start)

