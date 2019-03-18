from os import system, name
from time import sleep


def display_board(board):
    """Displays game board."""

    print ("\n\n")
    print ("\t\t|\t\t|")
    print ('\t' + board[1] + '\t|\t' + board[2] + '\t|\t' + board[3])
    print ("\t\t|\t\t|")
    print ("--------------------------------------------------")
    print ("\t\t|\t\t|")
    print ('\t' + board[4] + '\t|\t' + board[5] + '\t|\t' + board[6])
    print ("\t\t|\t\t|")
    print ("--------------------------------------------------")
    print ("\t\t|\t\t|")
    print ('\t' + board[7] + '\t|\t' + board[8] + '\t|\t' + board[9])
    print ("\t\t|\t\t|")
    print ("\n\n")


def clear(): 
    """Clears screen."""
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


test_board = ["#","(1)","(2)","(3)","(4)","(5)","(6)","(7)","(8)","(9)"]
player = 1
i = 1


def choice():
    """Takes input from the user."""

    x = input("Your Choice?[1-9] ('Yes' or 'No' to stop the game) :")

    if x.lower() == "yes" or x.lower() == 'y' :
        return True
    elif x.lower() == "no" or x.lower() == 'n':
        return False
    elif int(x) in range(1,10):
        update(int(x))
        return True
    

def update(position):
    """Updates the game board."""

    if test_board[position] == "X" or test_board[position] == "O":
        print("Wrong Choice!!!")
        exit()
    elif player == 1:
        test_board[position] = "X"
    elif player == 2:
        test_board[position] = "O" 


def win_check():

    #condition 1,2,3
    if test_board[1] == test_board[2] == test_board[3]:
        print (f"\n\n\t\t\t!!! Player {player} won !!!")
        sleep(2)
        exit()

    #condition 1,4,7    
    elif test_board[1] == test_board[4] == test_board[7]:
        print (f"\n\n\t\t\t!!! Player {player} won !!!")
        sleep(2)
        exit()

    #condition 2,5,8
    elif test_board[2] == test_board[5] == test_board[8]:
        print (f"\n\n\t\t\t!!! Player {player} won !!!")
        sleep(2)
        exit()
    
    #condition 3,6,9
    elif test_board[3] == test_board[6] == test_board[9]:
        print (f"\n\n\t\t\t!!! Player {player} won !!!")
        sleep(2)
        exit()

    #condition 4,5,6
    elif test_board[4] == test_board[5] == test_board[6]:
        print (f"\n\n\t\t\t!!! Player {player} won !!!")
        sleep(2)
        exit()

    #condition 7,8,9
    elif test_board[7] == test_board[8] == test_board[9]:
        print (f"\n\n\t\t\t!!! Player {player} won !!!")
        sleep(2)
        exit()

    #condition 1,5,9
    elif test_board[1] == test_board[5] == test_board[9]:
        print (f"\n\n\t\t\t!!! Player {player} won !!!")
        sleep(2)
        exit()

    #condition 3,5,7
    elif test_board[3] == test_board[5] == test_board[7]:
        print (f"\n\n\t\t\t!!! Player {player} won !!!")
        sleep(2)
        exit()


while True:
    clear()
    print (f"Remainig chances: {i}\tPlayer {player} chance" )
    display_board(test_board)

    game = choice()

    #checking for continuation of game   
    if game == True:
        pass
    elif game == False:
        break

    #checking for the number of steps
    if i == 9:
        break

    win_check()

    i = i + 1

    #updating current player 
    if player == 1:
        player = 2
    else:
        player = 1 