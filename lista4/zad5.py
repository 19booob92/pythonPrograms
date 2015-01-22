import pdb

#tupla zwraca ruchy (x, y)

selectionId = 0
iteationNumber = 2

actualPosition = (0,0)

BOARD_SIZE = 8

movesNumbers = list(range(BOARD_SIZE))
#tworzenie planszy
board = [[0 for x in range(BOARD_SIZE)] for x in range(BOARD_SIZE)] 
#tutaj jestesmy na poczatku
board[0][0] = 1


def findiTheWay(position, beforeChoice):
	global iteationNumber

	if (iteationNumber >= (BOARD_SIZE * BOARD_SIZE+3)):
		return board

	for tryMove in range(beforeChoice, BOARD_SIZE):
		#zapamietanie wyboru
		selectionId = tryMove
		
		changePosition = goTo(tryMove, position[0], position[1])
		if (changePosition != None):
			#obliczneie nowych wspolrzednych
			newX = position[0] + changePosition[0]
			newY = position[1] + changePosition[1]
			position = (newX, newY)
			#zaznaczenie odwiedzonego miejsca
			board[newX][newY] = iteationNumber
				
			#kolejna iteracja
			iteationNumber += 1
			#rekursja
			pdb.set_trace()
			findiTheWay(position, 0)
		else:
			pdb.set_trace()
			findiTheWay(position, selectionId+1)
	
def drawBoad(boardArray):
	for i in boardArray[::-1]:
		for j in i:
			if (j < 10):
				print(" ", end="")
			print("  ", j, end = "")
		print()

#przypadki
def goTo(move, x, y):
	if move == 0:
		if ((x + 1 <= 7) and (y+2 <= 7 ) and (board[x+1][y+2] == 0)):
			return (1,2)
	elif move == 1:
		if ((x -1 >= 0) and (y+2 <= 7) and (board[x-1][y+2] == 0)):
			return (-1, 2)
	elif move == 2:
		if ((x -2 >= 0) and (y+1 <= 7) and (board[x-2][y+1] == 0)):
			return (-2, 1)
	elif move == 3:	
		if ((x -2 >= 0) and (y-1 >= 0) and (board[x-2][y-1] == 0)):
			return (-2, -1)
	elif move == 4:
		if ((x -1 >= 0) and (y -2 >= 0) and (board[x-1][y-2] == 0)):
			return (-1, -2)
	elif move == 5:
		if ((x + 1 <= 7) and (y -2 >= 0) and (board[x+1][y-2] == 0)):
			return (1, -2)
	elif move == 6:
		if ((x+2 <= 7) and (y -1 >=0) and (board[x+2][y-1] == 0)):
			return (2,-1)
	elif move == 7:
		if ((x +2 <=7) and (y +1 <=7) and (board[x+2][y+1] == 0)):
			return (2,1)
	else:
		return None

findiTheWay(actualPosition, 0)
drawBoad(board)
