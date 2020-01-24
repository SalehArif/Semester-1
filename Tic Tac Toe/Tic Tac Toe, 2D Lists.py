import sys

def printboard(board):

    print('\n\t\t\t',board[0][0],' | ',board[0][1],' | ',board[0][2])
    print('\t\t\t','---|-----|---')
    print('\t\t\t',board[1][0],' | ',board[1][1],' | ',board[1][2])
    print('\t\t\t','---|-----|---')
    print('\t\t\t',board[2][0],' | ',board[2][1],' | ',board[2][2])
    print()
    '''for i in range(1,4):
        for j in range(1,4):
            if board[i-1][j-1]%3==0:
                print(board[i-1][j-1])
                if not i==3 and j==3:
                    print('--|---|--')
            else:
                print(board[i-1][j-1],end = ' | ')
'''
        
def playermove(lst):
    
    while True:
        move = int(input("Enter a number from 1-9 to place X: "))
        state = spacefree(lst,move)
        if state:
            break
        print('The space is already taken, pick a different spot')
        
    if move<=3:
        move -= 1
        lst[0][move] = 'X'
    elif move<=6:
        move -= 4
        lst[1][move] = 'X'
    elif move<=9:
        move -= 7
        lst[2][move] = 'X'
        
def spacefree(lst, ind):
    if ind<=3:
        move = ind -1
        if lst[0][move] == ind:
            return True
    elif ind<=6:
        move = ind -4
        if lst[1][move] == ind:
            return True
    elif ind<=9:
        move = ind -7
        if lst[2][move] == ind:
            return True
    return False

def win(lst):
    # check rows,columns and diagonals
    # rows
    for i in range(3):
        if lst[i][0]==lst[i][1]==lst[i][2]:#=='X' or lst[i][0]==lst[i][1]==lst[i][2]=='O':
            printboard(lst)
            print(lst[i][0],' has won the game')
            sys.exit()

    # columns
    for i in range(3):
        # 0,0   1,0     2,0
        # 1     4       7
        # 0,1   1,1     2,1
        # 2     5       8
        # 0,2   1,2     2,2
        # 3     6       9
        if lst[0][i]==lst[1][i]==lst[2][i]:#=='X' or lst[0][i]==lst[1][i]==lst[2][i]=='O':
            printboard(lst)
            print(lst[0][i],' has won the game')
            sys.exit()

    # 0,0   1,1     2,2
    # 1     5       9
    #0,2    1,1     2,0
    #3      5       7
    if lst[0][0]==lst[1][1]==lst[2][2]:#=='X' or lst[0][1]==lst[1][1]==lst[2][2]=='O':
        printboard(lst)
        print(lst[0][0],' has won the game')
        sys.exit()
        
    elif lst[0][2]==lst[1][1]==lst[2][0]:#=='X' or lst[0][2]==lst[1][1]==lst[2][0]=='O':
        printboard(lst)
        print(lst[0][2],' has won the game')
        sys.exit()

def space(lst,i,j):
    
    if not (lst[i][j]=='X' or lst[i][j]=='O'):
        return True
    return False

    
def compmove(lst,j):
    if j == 0:
        import random
        while True:
            move = random.randint(1,9)
            state = spacefree(lst,move)
            if state:
                break
        if move<=3:
            move -= 1
            lst[0][move] = 'O'
        elif move<=6:
            move -= 4
            lst[1][move] = 'O'
        elif move<=9:
            move -= 7
            lst[2][move] = 'O'
            
    for i in range(3):
        
        if lst[i][0]== lst[i][1] and space(lst,i,2):
            lst[i][2]= 'O'
            return None
        elif lst[i][0]== lst[i][2] and space(lst,i,1):
            lst[i][1] = 'O'
            return None
        elif lst[i][1]== lst[i][2] and space(lst,i,0):
            lst[i][0] = 'O'
            return None
        
    for i in range(3):
        if lst[0][i]==lst[1][i] and space(lst,2,i):
            lst[2][i] = 'O'
            return None
        elif lst[0][i]==lst[2][i] and space(lst,1,i):
            lst[1][i]='O'
            return None
        elif lst[1][i]==lst[2][i] and space(lst,0,i):
            lst[0][i] = 'O'
            return None

    if lst[0][0]==lst[1][1] and space(lst,2,2):
        lst[2][2] = 'O'
    elif lst[1][1]==lst[2][2] and space(lst,0,0):
        lst[0][0] = 'O'
    elif lst[0][0]==lst[2][2] and space(lst,1,1):
        lst[1][1] = 'O'
    elif lst[0][2]==lst[1][1] and space(lst,2,0):
        lst[2][0] = 'O'
    elif lst[1][1]==lst[2][0] and space(lst,0,2):
        lst[0][2] = 'O'
    elif lst[0][2]==lst[2][0] and space(lst,1,1):
        lst[1][1] = 'O'
        
def main():
    board = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    for i in range(5):
        printboard(board)
        playermove(board)
        win(board)
        compmove(board,i)
        win(board)
        
main()
