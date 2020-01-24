#tic tac toe (Easy Difficulty)
import sys
import random

def board(lst):
    print()
    for i in range(1,len(lst)+1):
        if i%3==0:
            if i==9:
                print(lst[i-1])
            else:
                print(lst[i-1])
                print('--|---|--')
        else:
            print(lst[i-1],end = ' | ')
    print()
            
def playermov(lst): 
    move = int(input("Enter number from 1-9 where you want to place an X: "))
    while lst[move-1] == 'X' or lst[move-1] == 'O':
        move = int(input("Enter number from 1-9 where you want to place an X: "))
    lst[move-1] = 'X'
    return lst


def compmov(lst,i):
    ok = random.randint(1,9)
    while lst[ok-1] == 'X' or lst[ok-1] == 'O':
        ok = random.randint(1,9)
    lst[ok-1] = 'O'
    return lst

def win(lst):
    #Rows
    # for i in range(0,9,3)
    # check i i+1 i+2
    if lst[0]==lst[1]==lst[2]:
        board(lst)
        print(lst[0],' has won the game')
        sys.exit()
    elif lst[3]==lst[4]==lst[5]:
        board(lst)
        print(lst[3],' has won the game')
        sys.exit()

    elif lst[6]==lst[7]==lst[8]:
        print(lst[6],' has won the game')
        board(lst)
        sys.exit()

    #Columns
    # for i in range(0,9,3)
    # check i i+3 i+6
    elif lst[0]==lst[3]==lst[6]:
        
        board(lst)
        print(lst[0],' has won the game')
        sys.exit()

    elif lst[1]==lst[4]==lst[7]:
        board(lst)
        print(lst[1],' has won the game')
        sys.exit()

    elif lst[2]==lst[5]==lst[8]:
        board(lst)
        print(lst[2],' has won the game')
        sys.exit()
        
    #Diagonals
    # for i in range(0,9)
    # check i i+4 i+8
    elif lst[0]==lst[4]==lst[8]:
        board(lst)
        print(lst[0],' has won the game')
        sys.exit()
        
    # for i in range(0,9)
    # check i i+2 (i+2(1)) i+4 (i+2(2))
    elif lst[2]==lst[4]== lst[6]:
        board(lst)
        print(lst[2],' has won the game')
        sys.exit()

        
def main():
    print('*********************************************************************')
    print("This Program runs a game of TIC TAC TOE on Easy Difficulty\n Try your best to not lose!\n Have fun!")
    print('*********************************************************************')
    print()
    lis = [1,2,3,
       4,5,6,
       7,8,9]
    for i in range(5):
        board(lis)
        lis = playermov(lis)
        win(lis)
        lis = compmov(lis,i)
        win(lis)

main()
