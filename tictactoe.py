import random

def display_board(spots):
    print("--------------------")
    for i, row in enumerate(board_rows):
        if i == 0:
            print(f"| {spots[1]} | {spots[2]} | {spots[3]} |")
            print("--------------------")
        if i == 1:
            print(f"| {spots[4]} | {spots[5]} | {spots[6]} |")
            print("--------------------")
        if i == 2:
            print(f"| {spots[7]} | {spots[8]} | {spots[9]} |")
            print("--------------------")
            
def board_layout():
    print("--------------------")
    for i, row in enumerate(board_rows):
        if i == 0:
            print(f"|  1  |  2  |  3  |")
            print("--------------------")
        if i == 1:
            print(f"|  4  |  5  |  6  |")
            print("--------------------")
        if i == 2:
            print(f"|  7  |  8  |  9  |")
            print("--------------------")

def get_playernumber():
    player_num = ''

    while player_num not in ['1', '2']:

        player_num = input("Choose player number (1 or 2)?")
        if player_num not in ['1', '2']:
            print("Not Acceptable. Please enter player number 1 or 2 in digits only.")

    return int(player_num)

def player_choice(choices):

    player_choice = ''

    while player_choice not in choices:

        player_choice = input("Your move: ")
        if player_choice not in choices:
            print("Not Acceptable. Please enter a number 1 - 9 that is available")

    return int(player_choice)

def ask_ready():

    ans = ''
    while ans not in ['Y', 'N']:

        ans = input("Are you ready? (Y or N)")
        if ans not in ['Y', 'N']:
            print("Not Acceptable, please answer with letters: Y and N (case sensitive)")
        elif ans == 'N':
            print("Ok, have a nice day")
            exit(0)
        elif ans == 'Y':
            return ans
        
def game_on(spots, choices, current_player):


    if current_player == '1':
        print(f'Player {current_player}, its your turn')

        pos_choice = ''
        while pos_choice not in choices:
            
            pos_choice = input("Your move: ")
            
            if pos_choice not in choices:
                print("That spot has already been taken, please choose another spot")

        choice_int = int(pos_choice)
        choices = choices.remove(pos_choice)
        spots[choice_int] = ' X '
        display_board(spots) 
         
        
    if current_player == '2':
        print(f'Player {current_player}, its your turn')

        pos_choice = ''
        while pos_choice not in choices:
            
            pos_choice = input("Your move: ")
            
            if pos_choice not in choices:
                print("That spot has already been taken, please choose another spot")

        choice_int = int(pos_choice)
        choices = choices.remove(pos_choice)
        spots[choice_int] = ' O '
        display_board(spots)

def game_check(spots):

    if spots[1] == ' X ' and spots[2] == ' X ' and spots[3] == ' X ':
        return "Player 1 is winner"
    elif spots[4] == ' X ' and spots[5] == ' X ' and spots[6] == ' X ':
        return "Player 1 is winner"
    elif spots[7] == ' X ' and spots[8] == ' X ' and spots[9] == ' X ':
        return "Player 1 is winner"
    elif spots[1] == ' X ' and spots[4] == ' X ' and spots[7] == ' X ':
        return "Player 1 is winner"
    elif spots[2] == ' X ' and spots[5] == ' X ' and spots[8] == ' X ': 
        return "Player 1 is winner"
    elif spots[3] == ' X ' and spots[6] == ' X ' and spots[9] == ' X ':
        return "Player 1 is winner"
    elif spots[1] == ' X ' and spots[5] == ' X ' and spots[9] == ' X ': 
        return "Player 1 is winner"
    elif spots[3] == ' X ' and spots[5] == ' X ' and spots[7] == ' X ':
        return "Player 1 is winner"
    elif spots[1] == ' O ' and spots[2] == ' O ' and spots[3] == ' O ':
        return "Player 2 is winner"
    elif spots[4] == ' O ' and spots[5] == ' O ' and spots[6] == ' O ':
        return "Player 2 is winner"
    elif spots[7] == ' O ' and spots[8] == ' O ' and spots[9] == ' O ':
        return "Player 2 is winner"
    elif spots[1] == ' O ' and spots[4] == ' O ' and spots[7] == ' O ':
        return "Player 2 is winner"
    elif spots[2] == ' O ' and spots[5] == ' O ' and spots[8] == ' O ': 
        return "Player 2 is winner"
    elif spots[3] == ' O ' and spots[6] == ' O ' and spots[9] == ' O ':
        return "Player 2 is winner"
    elif spots[1] == ' O ' and spots[5] == ' O ' and spots[9] == ' O ': 
        return "Player 2 is winner"
    elif spots[3] == ' O ' and spots[5] == ' O ' and spots[7] == ' O ':
        return "Player 2 is winner"


board_rows = [1, 2, 3]
spots = {1: '   ', 2: '   ', 3: '   ', 4: '   ', 5: '   ', 6: '   ', 7: '   ', 8: '   ', 9: '   '}
choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
players = ['1', '2']

print("Welcome to Tic-Tac-Toe")

get_playernumber()
print("Player 1 is X and Player 2 is O")
print("The computer will decide who goes first using a randomizer to pick the player")
current_player = random.choice(players)
print("The game board will look like this. \nWhen its your turn, please pick the square you want your X or O at by choosing the respective number")
board_layout()
ans = ask_ready()

while ans == 'Y':

    winner = ''
    game_on(spots, choices, current_player)
    winner = game_check(spots)

    if winner == "Player 1 is winner":
        print(winner)
        ans = input("Do you want to play again")
        spots = {1: '   ', 2: '   ', 3: '   ', 4: '   ', 5: '   ', 6: '   ', 7: '   ', 8: '   ', 9: '   '}
        choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    elif winner == "Player 2 is winner":
        print(winner)
        ans = input("Do you want to play again")
        spots = {1: '   ', 2: '   ', 3: '   ', 4: '   ', 5: '   ', 6: '   ', 7: '   ', 8: '   ', 9: '   '}
        choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    elif choices == []:
        print("Its a Tie")
        ans = input("Do you want to play again")
        spots = {1: '   ', 2: '   ', 3: '   ', 4: '   ', 5: '   ', 6: '   ', 7: '   ', 8: '   ', 9: '   '}
        choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    


    if current_player == '1':
        current_player = '2'
    else:
        current_player = '1'
