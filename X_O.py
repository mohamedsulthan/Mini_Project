import random
def board1(board):
    print(board[1]+ "|" + board[2] + "|" + board[3])
    print("_____")
    print(board[4]+ "|" + board[5] + "|" + board[6])
    print("_____")
    print(board[7]+ "|" + board[8] + "|" + board[9])

def insertLetter(letter,pos):
    board[pos]=letter

def FreeSpace1(pos):
    return (board[pos]==" ")

def boardfull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def iswinner(b,l):

    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def player_1_move():#it will get input from 1st player and check the corresponding position is available or not,if available then it fills the box untill it returns false
    run = True
    while run:
        try:
           move = int(input(x1+" "+"select position b/w 1 & 9 to insert X:"))
           if move > 0 and move < 10:
                if FreeSpace1(move):
                    insertLetter ("x",move)
                    run = False

                else:
                    print("position is full")
           else:
                print("Enter a valid number")
        except:
            print("Enetr a valid number")

def player_2_move():#it will get input from 2nd player and check the corresponding position is available or not,if available then it fills the box untill it returns false
    run = True
    while run:
        try:
           move = int(input(y+" "+"select position b/w 1 & 9:"))
           if move > 0 and move < 10:
                if FreeSpace1(move):
                    insertLetter("o", move)
                    run = False

                else:
                    print("position is full")
           else:
                print("Enter a valid number")
        except:
            print("Enetr a valid number")

def mainlogic():
    board1(board)
    while (boardfull(board) == False):#also we can use while not condition
        if (iswinner(board,"o") == False):#also we can use if not condition also
           player_1_move()
           print(board1(board))
        else:
           print(y+" "+"is the winner!!!")
           break
        if (iswinner(board,"x") == False):#also we can use if not condition also
            player_2_move()
            print(board1(board))

        else:
            print(x1+" "+"is the winner!!!")
            break
    if boardfull(board):
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n):")

    if x.lower() == 'y':
        x1 = input("Enter Player_1 Name:")
        y = input("Enter Player_2 Name:")
        board = [' ' for i in range(10)]
        #print('--------------------')

        mainlogic()
    elif x.lower() == 'n':
        print("bye")
        break

    else:
        print("Please type y or n:")

