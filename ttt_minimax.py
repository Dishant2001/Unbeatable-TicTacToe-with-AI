import random

matrix=[' ' for _ in range(10)]

def printMat(matrix):
    print('   |   |   ')
    print(' '+matrix[1]+' '+'|'+' '+matrix[2]+' '+'|'+' '+matrix[3]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+matrix[4]+' '+'|'+' '+matrix[5]+' '+'|'+' '+matrix[6]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+matrix[7]+' '+'|'+' '+matrix[8]+' '+'|'+' '+matrix[9]+' ')
    print('   |   |   ')

def winner(matrix):
    if (matrix[1]=='X' and matrix[2]=='X' and matrix[3]=='X') or (matrix[4]=='X' and matrix[5]=='X' and matrix[6]=='X') or (matrix[7]=='X' and matrix[8]=='X' and matrix[9]=='X') or (matrix[1]=='X' and matrix[4]=='X' and matrix[7]=='X') or (matrix[2]=='X' and matrix[5]=='X' and matrix[8]=='X') or (matrix[3]=='X' and matrix[6]=='X' and matrix[9]=='X') or (matrix[1]=='X' and matrix[5]=='X' and matrix[9]=='X') or (matrix[3]=='X' and matrix[5]=='X' and matrix[7]=='X'):
        return -10
    elif (matrix[1]=='O' and matrix[2]=='O' and matrix[3]=='O') or (matrix[4]=='O' and matrix[5]=='O' and matrix[6]=='O') or (matrix[7]=='O' and matrix[8]=='O' and matrix[9]=='O') or (matrix[1]=='O' and matrix[4]=='O' and matrix[7]=='O') or (matrix[2]=='O' and matrix[5]=='O' and matrix[8]=='O') or (matrix[3]=='O' and matrix[6]=='O' and matrix[9]=='O') or (matrix[1]=='O' and matrix[5]=='O' and matrix[9]=='O') or (matrix[3]=='O' and matrix[5]=='O' and matrix[7]=='O'):
        return 10
    return 0

def insertChar(matrix,pos,p):
    matrix[pos]=p

def isFull(matrix):
    return matrix.count(' ')==1

def isEmpty(matrix,pos):
    return matrix[pos]==' '

def random_select(li):
    l=len(li)
    r=random.randrange(0,l)
    return li[r]


def minimax(matrix,maximizer):
    score=winner(matrix)
    if score==10 or score==-10:
        return score
    if isFull(matrix):
        return 0
    if maximizer:
        bestScore=-50
        for i,char in enumerate(matrix):
            if char==' ':
                matrix[i]='O'
                bestScore=max(bestScore,minimax(matrix,not maximizer))
                matrix[i]=" "
        return bestScore
    else:
        bestScore=50
        for i,char in enumerate(matrix):
            if char==' ':
                matrix[i]='X'
                bestScore=min(bestScore,minimax(matrix,not maximizer))
                matrix[i]=' '
        return bestScore


def computer_move(matrix):
    bestScore=-50
    move=0
    for i,char in enumerate(matrix):
        if char==' ':
            matrix[i]='O'
            score=minimax(matrix,False)
            matrix[i]=' '
            if score>bestScore:
                bestScore=score
                move=i
    return move


def player_move(matrix,pos):
    insertChar(matrix,pos,'X')

if __name__=='__main__':
    print('Welcome Player!')
    while True:
        printMat(matrix)
        while True:
            move=input("You are 'X', enter position (1-9): ")
            try:
                move=int(move)
                if move>0 and move<=9:
                    if isEmpty(matrix,move):
                        player_move(matrix,move)
                        break
                    else:
                        print("Position Occupied!")
                else:
                    print("Enter in valid range!")
            except:
                print("Enter a number!")
        if winner(matrix)==-10:
            printMat(matrix)
            print('Congratulations!, you won!')
            break
        move=computer_move(matrix)
        if isFull(matrix):
            printMat(matrix)
            print('Tie Game!')
            break
        insertChar(matrix,move,'O')
        if winner(matrix)==10:
            printMat(matrix)
            print('You lose!')
            break
        
                