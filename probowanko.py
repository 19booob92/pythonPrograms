#!/usr/bin/env python3
#Funkcja znajduje dzielniki danej liczby (różne od tej liczby).
from datetime import datetime

def findDivisors(number):
    totality=0
    for divisor in range(1,number):
        if number%divisor==0:
            totality+=divisor
    return totality

def isPerfect(number):
    if number==findDivisors(number):
        perfect=number
        return(perfect)
        
def areFriends(number):
    friend=findDivisors(number)
    if findDivisors(friend)==number and findDivisors(number)>number \
    and number!=findDivisors(number):
        return(number,friend)

start = datetime.now().microsecond

result1=[]
result2=[]
for number in range(1,1000):
    if isPerfect(number)!=None:
        result1.append(isPerfect(number))
    if areFriends(number)!=None:
        result2.append(areFriends(number))
    
print("Liczby doskonałe mniejsze od 1000 to:\n", result1)
print("Pary liczb zaprzyjaźnionych mniejszych od 1000 to:\n", result2)

stop = datetime.now().microsecond

print(stop - start)
    

