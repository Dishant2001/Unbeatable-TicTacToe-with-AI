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

def winner(matrix,p):
    return (matrix[1]==p and matrix[2]==p and matrix[3]==p) or (matrix[4]==p and matrix[5]==p and matrix[6]==p) or (matrix[7]==p and matrix[8]==p and matrix[9]==p) or (matrix[1]==p and matrix[4]==p and matrix[7]==p) or (matrix[2]==p and matrix[5]==p and matrix[8]==p) or (matrix[3]==p and matrix[6]==p and matrix[9]==p) or (matrix[1]==p and matrix[5]==p and matrix[9]==p) or (matrix[3]==p and matrix[5]==p and matrix[7]==p)

def insertChar(matrix,pos,p):
    matrix[pos]=p

def isFull(matrix):
    return matrix.count(' ')==1

def isEmpty(matrix,pos):
    return matrix[pos]==' '

# insertChar(matrix,1,'X')
# insertChar(matrix,2,'O')
# insertChar(matrix,9,'X')
# insertChar(matrix,5,'O')
# insertChar(matrix,3,'X')
# insertChar(matrix,4,'O')
# insertChar(matrix,6,'X')
# insertChar(matrix,7,'O')
# insertChar(matrix,8,'X')
# printMat(matrix)
# print(isFull(matrix))
# print(win(matrix,'X'))
# print(win(matrix,'O'))

def random_select(li):
    l=len(li)
    r=random.randrange(0,l)
    return li[r]

second_step=0

def computer_move(matrix,first_move):
    global second_step
    move=0
    possibleMoves=[x for x,char in enumerate(matrix) if char==' ' and x!=0]
    for i in ['O','X']:
        for j in possibleMoves:
            duplicate_matrix=matrix[:]
            insertChar(duplicate_matrix,j,i)
            if winner(duplicate_matrix,i):
                move=j
                return move
    if first_move==True:
        if matrix[1]==' ' and matrix[3]==' ' and matrix[7]==' ' and matrix[9]==' ':
            corners=[1,3,7,9]
            move=random_select(corners)
            return move
        if matrix[1]!=' ' or matrix[3]!=' ' or matrix[7]!=' ' or matrix[9]!=' ':
            second_step=1
            return 5
    if second_step==1:
        second_step=0
        openEdges=[2,4,6,8]
        move=random_select(openEdges)
        return move
    if matrix[5]==' ':
        return 5
    openCorners=[]
    for i in [1,3,7,9]:
        if i in possibleMoves:
            openCorners.append(i)
    if len(openCorners)>0:
        move=random_select(openCorners)
        return move
    openEdges=[]
    for i in [2,4,6,8]:
        if i in possibleMoves:
            openEdges.append(i)
    if len(openEdges)>0:
        move=random_select(openEdges)
        return move
    return move

    


def player_move(matrix,pos):
    insertChar(matrix,pos,'X')

if __name__=='__main__':
    print('Welcome Player!')
    first_move=True
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
        if winner(matrix,'X'):
            printMat(matrix)
            print('Congratulations!, you won!')
            break
        move=computer_move(matrix,first_move)
        first_move=False
        if move==0 or  isFull(matrix):
            print('Tie Game!')
            break
        insertChar(matrix,move,'O')
        if winner(matrix,'O'):
            printMat(matrix)
            print('You lose!')
            break
        
                