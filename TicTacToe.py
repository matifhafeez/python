from random import randrange

board = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

def PrintHorizontalLine():
    for x in range(0,19):
        if x % 6 == 0:
            print('+', end = ' ')
        else:
            print('-', end = ' ')

def PrintVerticalLine(row):
    row_count = 0
    for y in range(0,19):
        if y % 6 == 0:
            print('|', end = ' ')
        elif y % 3 == 0 and y != 0 and y != 18:
            print(row[row_count], end = ' ')
            row_count += 1
        else:
            print(' ', end = ' ')
        
def DisplayBoard(board):
    for a in range(0,3):
        PrintHorizontalLine()
        print("\n")
        PrintVerticalLine(board[a])
        print("\n")   
        if a == 2:
            PrintHorizontalLine()    
    print("\n") 

def DrawMove(board):        
    row = randrange(3)
    column = randrange(3)
    draw_successfull = False
    while draw_successfull != True:
        if board[row][column] != 'x'.upper() and board[row][column] != 'o'.upper():
            board[row][column] = 'X'
            draw_successfull = True
        row = randrange(3)
        column = randrange(3)
    DisplayBoard(board)

def EnterMove(board):
    i = 1
    user_position = int(input("Enter your move:"))
    while(user_position < 1 or user_position > 9):
        print("That's not the correct position!")
        user_position = int(input("Enter your move:"))
    for a in range(len(board)):
        for b in range(len(board[a])):
            if i == user_position:
                board[a][b] = 'O'                
            i += 1

def VictoryFor(board,sign):
    #Check Horizontally
    for a in range(len(board)):
        not_found = False        
        for b in range(len(board[a])):
            if board[a][b] != sign:
                not_found = True
                break     
        if not_found == False:
            break     
    if not_found == False:
        return True     
    #Check Vertically
    not_found = False
    for a in range(len(board)):
        for b in range(len(board[a])):
            if board[b][a] != sign:
                not_found = True
                break
        if not_found == False:
            break 
    if not_found == False:
        return True
    #Check Diagonally
    not_found = False
    for a in range(len(board)):
        if board[a][a] != sign:
            not_found = True
            break
    if not_found == False:
        return True    
    #Check Diagonally
    not_found = False
    b = len(board) - 1
    for a in range(len(board)):    
        if board[a][b] != sign:
            not_found = True
            break
        b -= 1        
    if not_found == False:
        return True
    else:
        return False

if __name__ == "__main__":
    while(True):
        DrawMove(board)  
        if VictoryFor(board,'X') == True:
            DisplayBoard(board)
            print("Computer won!")
            break
        EnterMove(board)
        if VictoryFor(board,'O') == True:
            DisplayBoard(board)
            print("You won!")            
            break        

