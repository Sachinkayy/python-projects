import random
board = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
]

position_dict = {'1':[0,0],'2':[0,1],'3':[0,2],'4':[1,0],'5':[1,1],\
'6':[1,2],"7":[2,0],"8":[2,1],'9':[2,2]}

computer = ""
turns =0

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ",end ="")
        print()

def check_input(user_input):
    #check if input is a number
    if not isnum(user_input): return False
    user_input =int(user_input)
    #check if its bw 1-9
    if not bounds(user_input) : return False
    return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid input")
        return False
    else:
        return True

def bounds(user_input):
    if user_input > 9 or user_input<1:
     print("This number is out of bounds")
     return False
    else:
        return True


def placeChoice(user_input,activeplayer):
    if activeplayer == player:
        while True:
            if check_input(user_input):
                x, y = position_dict[user_input]
                if board[x][y] != "O" and board[x][y] != "X":
                    board[x][y] = player
                    break
                else:
                    user_input = input("That place is already taken, Please enter again: ")
                    print("---------------------------------------------")
            else:
                user_input = input("Please enter again: ")
                print("---------------------------------------------\n\n")
                continue
                
            print()
            print_board(board)
            print()
    else:
        while True:
            comp= random.randint(1,9)
            x,y = position_dict[str(comp)]
            if board[x][y] != "O" and board[x][y] !="X":
                board[x][y] = computer
                print_board(board)
                break

def swap_active_player():
    global activeplayer
    if activeplayer == player:
        activeplayer= computer
    else:
        activeplayer = player


def iswin(activeplayer,board):
    if check_row(activeplayer,board): return True
    if check_col(activeplayer,board):return True
    if check_diag(activeplayer,board):return True
    return False

def check_row(activeplayer,board):
    for row in board:
        complete_row =True
        for slot in row:
            if slot != activeplayer:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_col(activeplayer,board):
  for col in range(3):
    complete_col = True
    for row in range(3):
        if board[row] [col] != activeplayer:
            complete_col = False
            break
    if complete_col: return True
  return False

def check_diag(activeplayer, board):
  #top left to bottom right
  if board[0][0] == activeplayer and board[1][1] == activeplayer and board[2][2] == activeplayer: return True
  elif board[0][2] == activeplayer and board[1][1] == activeplayer and board[2][0] == activeplayer: return True
  else: return False

while True:
    player = input("You are X or O, enter your choice: ").upper()
    print("--------------------------------------------- \n")
    if player != "X" and player !="O":
        print("Illegal input, please choose X or O")
        continue     

    if player == "X" or player =="O":
        if player == "X":
            computer = "O"
        else:
            computer ='X'
    
        print(f" \nYou are {player}, your opponent is {computer} \n")
        print_board(board)
        print()
        
        activeplayer=player #player has the first turn
        user_input = input("PLEASE ENTER WHERE YOU WANT TO PLACE YOURSELF: ")
        print("--------------------------------------------- \n")
        
        placeChoice(user_input,activeplayer)
        swap_active_player() #changing current player
        placeChoice(user_input,activeplayer)

        while turns < 8 :   
            user_input = input("choose your next place or q to quit: ")
            print("--------------------------------------------- \n")
            
            if user_input != "q": 
                swap_active_player() #changing current player from comp to player
                placeChoice(user_input,activeplayer)

                if iswin(activeplayer,board):
                    print_board(board)
                    print(" \n\n=============================================")
                    print(f"{activeplayer} won!!!")
                    print("=============================================\n\n")
                    break

                swap_active_player() #changing, player to comp
                placeChoice(user_input,activeplayer)

                if iswin(activeplayer,board):
                    #print_board(board)
                    print(" \n\n=============================================")
                    print(f"{activeplayer} WON, YOU LOST!!!")
                    print("=============================================\n\n")
                    break

                turns +=1
                
                if turns ==3 and iswin ==False:
                    print(" TIE! ")
                    break
                continue

            break
    break