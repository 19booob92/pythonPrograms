print 'Type word'
word = list(raw_input())

print('1: aB -> A_B \n2: A_B -> aB \n3: AB -> Ab')
choice = raw_input()

i = 0

if (choice == '1'):
	for char in word:
		if char.isupper():
			word.insert(i, "_")
			break
		i+=1

	print "".join(word).upper()
elif (choice == '2'):
	word = "".join(word).lower()
	word = list(word)
	
	underScoreIdx = word.index('_')
	word.remove('_')
	word.insert(underScoreIdx, word[underScoreIdx].upper())
	del word[underScoreIdx + 1]
	i+=1

	print "".join(word)
elif (choice == '3'):
	word = "".join(word).lower()
	word = list(word)

	spaceIndex = word.index(" ")
	secondChar = word[spaceIndex + 1]
	del word[spaceIndex + 1]
	word.insert(spaceIndex + 1, secondChar.upper())

	firstChar = word[0]
	del word[0]
	word.insert(0, firstChar.upper())

	print "".join(word)
