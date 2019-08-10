import os

def draw_board(board):
    """
    A function with which prints a visual representation of the noughts and crosses board
    
    Parameters
    ----------
    board : List

    Outputs
    ----------
    os.system('cls') : Clears the console window
    3 * print statements : Prints the board on the console with the values of each cell

    Return values
    ----------
    None 
    """

    os.system('cls')
    print(f"   |   |   \n {board[6]} | {board[7]} | {board[8]} \n   |   |   \n-----------")
    print(f"   |   |   \n {board[3]} | {board[4]} | {board[5]} \n   |   |   \n-----------")
    print(f"   |   |   \n {board[0]} | {board[1]} | {board[2]} \n   |   |   ")

def player_choose_symbol():
    symbol = input("Press the 'x' or 'o' key to select your symbol: ")
    while not (symbol == 'x' or symbol == 'o'):
        symbol = input("You have not selected a valid symbol\nPress the 'x' or 'o' key to select your symbol: ")
    if symbol == 'x':
        return ('x', 'o')
    else:
        return ('o', 'x')

def place_marker(board, index, player):
    board[index] = player
    draw_board(board)

def win_check(board):
    for index in range(0,6,3):
            if board[index] != ' ' and board[index] == board[index + 1] == board[index + 2]: 
                return True
    else:
        for index in range(0,3,1):
            if board[index] != ' ' and board[index] == board[index + 3] == board[index + 6]:
                return True
        else:
            if board[0] != ' ' and board[0] == board[4] == board[8]:
                return True
            elif board[2] != ' ' and board[2] == board[4] == board[6]:
                return True
            else:
                return False

def space_check(board, index):
    return board[index] == ' '

def full_board_check(board):
    for cell in board:
            if cell == ' ':
                return False
    else:
        return True

def player_choice(board, player):
    input_pos = int(input(f"Player {player}: Please select the index where you would like to place your symbol (1-9): "))

    while not space_check(board, input_pos-1):
        input_pos = int(input("You cannot place your symbol there, as that position is already occupied. Please try again\n\nPlease select the index where you would like to place your symbol (1-9): "))
    place_marker(board, input_pos-1, player)

def replay():
    choice = input("Would you like to replay? Yes or No: ")
    if choice.lower() == 'yes':
        os.system('cls')
        run_game()
    elif choice.lower() == 'no':
        exit()

def run_game():
    board = [' '] * 9
    
    players = player_choose_symbol()
    draw_board(board)
    counter = -1
    while not win_check(board) and not full_board_check(board):
        counter += 1
        player_choice(board, players[counter % 2])
        
    if win_check(board):
        print(f"Victory! The {players[counter % 2]}'s win!!!!'")
        replay()
    elif full_board_check(board):
        print("The board is full and there are no winners")
        replay()

run_game()

    

