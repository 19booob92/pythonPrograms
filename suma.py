firstNum = input("Podaj a: ")
secondNum = input("Podaj b: ")

def sum(a,b):
	while (b > 0):
		a+=1
		b-=1
		print(a)
	return a

if firstNum.isdigit() and secondNum.isdigit():
	firstNum = int(firstNum)
	secondNum = int(secondNum)

	if firstNum == 0:
		print("sum : ", b)
	elif secondNum == 0:
		print("sum : ", a)
	else:
		sumAB =	sum(firstNum, secondNum)
		print ("Sum = ", sumAB)
else:
	print("wrong input type")
