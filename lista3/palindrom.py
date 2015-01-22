#!/usr/bin/env python3

def function(word):
    head=0
    tail=len(word)-1
    while(head < tail):
        if word[head]==word[tail]:
            head+=1
            tail-=1
        else:
            return False           
    return True        
                
word=(input("wpisz łańcuch znaków aby sprawdzić czy jest palindromem:\n"))
print(function(word))


