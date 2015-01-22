#qpy:console
while 1==1:
    a=int(input('podaj liczbe a '))
    b=int(input('podaj liczbe b '))
    S=0
    if a==0:
        print('iloczyn to zero')
    else:
        if b==0:
            print('iloczyn to zero')
        
        else:
            if a>b:
                while(b>0):
                    S=S+a
                    b=b-1
                    print(S)
                print('iloczyn to', S)
            else:
                while(a>0):
                    S=S+b
                    a=a-1
                    print(S)
                print('iloczyn to', S)
        
            
