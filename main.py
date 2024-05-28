
#tik-tak-tow kennneth Manhica

count_ = 1#to be use on def play

def start():
    
    player_1=input("what is the symbol of the first player 'X' or 'O': ")[0].upper()
    print(player_1)

    while(player_1 !='X' and player_1 != 'O'):
        print("invalid option, choose between 'X' or 'O' ")
        player_1=input("what is the symbol of the first player 'X' or 'O': ").upper()
        print(player_1)

    if (player_1 == 'X'):
        player_1 = 'X'
        player_2 = 'O'
    elif (player_1 == "O"):
        player_1 ='O'
        player_2 ='X'
    
    return player_1, player_2


def Board():

    board = [[" "," "," "],[" "," "," "],[" "," "," "]]

    return board


def print_board(board):

    count = 1
    
    for i in range(3):
        if (i==0):
            print("  1    2   3")  

        print (f"{count} {board[i][0]} | {board[i][1]} | {board[i][2]}")
        count = count+1

        if (i<2):
            print(" ---+---+---")


def play (count_, player_1, player_2, board):

    if(count_ % 2 == 0):
        player = player_2
    else:
        player = player_1

    print(f"{player} it's your turn")
    l=int(input("choose a line: "))-1
    c=int(input("choose a colunm: "))-1
    

    while(l>2 or c>2):
        print("out of the board")
        l = int(input("choose a line: "))-1
        c = int(input("choose a colunm: "))-1
    
    while (board[l][c]=="X" or board[l][c]=="X" ):
        print("position occupied")
        l = int(input("choose a line: "))-1
        c = int(input("choose a colunm: "))-1
    
    board[l][c] = player


def win(board, count_, player_1, player_2):

    
    if(count_ % 2 == 0):
        player = player_2
    else:
        player = player_1

    
    for i in range(3):
        if(board[i][0] == board[i][1]== board[i][2] == player):
            return True
        elif(board[0][i] == board[1][i]== board[2][i]  == player):
            return True
    if(board[0][0] == board[1][1] == board [2][2]  == player):
        return True 
    elif(board[0][2] == board[1][1] == board [2][0]  == player):
        return True
    
    return False

def draw(count_):     
    print("game over!!!")
    print("it is a draw")


def playing(count_, board, player_1, player_2):

    while (count_<=9):
        play (count_, player_1, player_2, board)
        print_board(board)
        print()
               
        Winner = win(board, count_, player_1, player_2 )
        if Winner == True:
           
            if(count_ % 2 == 0):
                player = player_2
            else:
                player = player_1

            print("!!!!!!!!!!!!!!!!!!!!!")
            print (f"{player}, you won!!!!")
            break

        count_= count_ +1

    if(count_>9):
        draw(count_)

    
def main():

    player_1,player_2 = start()
    board = Board()
    Show_board = print_board(board)
    The_Play = playing(count_, board, player_1, player_2)

main()