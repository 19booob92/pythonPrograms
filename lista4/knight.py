import sys

startX = int(input("Podaj początkową współrzędną X:"))
startY = int(input("Podaj początkową współrzędną Y:"))

"""
Wszystkie możliwe ruchy
"""
knights_moves = ((-2,-1),(1,2),(2,-1),(-2,1),\
	(2,1),(-1,2),(1,-2),(-1,-2))

"""
Rozmiar planszy
"""
BOARD_SIZE = 8

board = []
"""
Tworzenie tablicy (planszy), wypełnionej zerami
"""
for i in range(0, BOARD_SIZE):
	board.append(BOARD_SIZE * [0])
"""
Prezentacja tablicy po określeniu kolenych ruchów konia
Tablica prezentowana jest w formie macierzy, reprezentującej
planszę
"""
def drawBoard():
	for i in board:
                for j in i:
                        if (j < 10):
                                print(" ", end="")
                        print("  ", j, end = "")
                print()

"""
Sprawdzenie czy można przejść na pole o współrzędnych
podanych jako argumenty funckji
"""
def isAvailable(x, y):
    if x < BOARD_SIZE and y < BOARD_SIZE and \
       x >= 0 and y >= 0 and board[x][y]==0:
        return True
    else:
        return False 

"""
Stworzenie listy zwierającej wszystkie możliwe przejścia,
dla pozycjji w jakiej aktualnie znajduje się koń
"""
def getPossibleMoves(x, y):
     possible_moves = []
     for move in knights_moves:
        cx,cy = x+move[0], y+move[1]
        if isAvailable(cx,cy):
            possible_moves.append((move[0],move[1]))
     return possible_moves  

"""
Jeśli lista dostępnych ruchów jest pusta, program rysuje planszę z
rozwiązaniem zadania, w przeciwnym wypadku wyznacza kolejny ruch 
""" 
def getNextMove (numMoves):
    smallestIndex = 0
    if not numMoves:
        drawBoard() 
        sys.exit(1)
    smallest = numMoves[0]
    for i in range(len(numMoves)):
        if numMoves[i] < smallest:
            smallest = numMoves[i]
            smallestIndex = i

    return smallestIndex

"""
Funkcja przyjmuje aktualną pozycję oraz licznik służacy do określenia
który ruch konia jest aktualnie wykonywany.
Jest to funkcja rekurencyjna, która przeszukuje drzewo możliwych
rozwiązań, w kolejnych krokach algorytmui, jako argumenty funkcji 
przekazywane są współrzędne konia, powiększone o przesunięcie 
wynikające z dostępnego, wybranego ruchu
"""
def solve (x,y,num_move):
    board[x][y] = num_move                                 
    possible_moves = getPossibleMoves(x,y)
    numOfMoves = []     
    for move in possible_moves:
        numOfMoves.append(len(getPossibleMoves(x+move[0],y+move[1])))
    
    nextMove = possible_moves[getNextMove(numOfMoves)]
    solve(x+nextMove[0],y+nextMove[1],num_move+1)   

"""
Pierwsze wywołanie głównej funkcji, w której występują 
rozwiązania rekurencyjne
"""
solve(startX,startY,1)

