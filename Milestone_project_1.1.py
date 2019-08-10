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
    os.system('cls') # Clear console screen

    # Print the game board. Arguments in printf statement place the vaues stored within the board list, into the visual representation of the board
    print(f"   |   |   \n {board[6]} | {board[7]} | {board[8]} \n   |   |   \n-----------")
    print(f"   |   |   \n {board[3]} | {board[4]} | {board[5]} \n   |   |   \n-----------")
    print(f"   |   |   \n {board[0]} | {board[1]} | {board[2]} \n   |   |   ")

def player_choose_symbol():
    """
    A function which is used to collect the user's choice of symbol, at the start of the game
    
    Parameters
    ----------
    None

    Outputs
    ----------
    Text input statements which print requests for the user to input their choice of symbol

    Return values
    ----------
    tuple : Containing 'x' and 'o' in that order or reversed order, depending on which symbol is chosen by player 1 
    """

    symbol = input("Press the 'x' or 'o' key to select your symbol: ")
    while not (symbol == 'x' or symbol == 'o'): # While the user has not entered x or o, keep requesting one of those symbols
        symbol = input("You have not selected a valid symbol\nPress the 'x' or 'o' key to select your symbol: ")
    if symbol == 'x': # Depending on whether player 1 has selected x or o, assign x and o in the appropriate order and return them in a tuple
        return ('x', 'o')
    else:
        return ('o', 'x')

def place_marker(board, index, player):
    """Small function used to insert new markers into the list which represents the game board"""
    board[index] = player # Assign the list indes indicated to equal the symbol of the player which has been passed as an argument
    draw_board(board) # Call the function to redraw the board with the newly placed symbol

def win_check(board):
    """ 
    Function which checks all possible winning combinations against the current contents of the board
        
    Parameters
    ----------
    Board : List

    Outputs
    ----------
    None

    Return values
    ----------
    Returns True if a victory condition has been met
    Returns False if no victory condition has yet been met
    """
    for index in range(0,6,3): # For loop which iterates over each of the horizontal lines in the board by iterating through list position 0, 3 and 6
            if board[index] != ' ' and board[index] == board[index + 1] == board[index + 2]: # Checks if all the elements horizontally in line are equal and not equal to ' '(empty)
                return True
    else:
        for index in range(0,3,1): # For loop which checks all the vertical lines on the board, by iterating list positions 0, 1 and 2 (1,2 and 3 on the board)
            if board[index] != ' ' and board[index] == board[index + 3] == board[index + 6]: # Checks if all the elements vertically in line are equal and not equal to ' '(empty)
                return True
        else: # If no vertical or horizontal lines on the board contain 3 matching symbols, we check the diagonals within the board
            if board[0] != ' ' and board[0] == board[4] == board[8]: # Check if all symbols in the bottom-left --> top-right horizontal are not ' ' and are all equal
                return True
            elif board[2] != ' ' and board[2] == board[4] == board[6]: # Check if all symbols in the bottom-right --> top-left horizontal are not ' ' and are all equal
                return True
            else:
                return False # If no victory condition has been met, return False

def space_check(board, index):
    """ 
    Small function which checks if a board index is empty(==' '), and therefore whether the player can place their marker there.

    Parameters
    ----------
    board : List
    index : int

    Outputs
    ----------
    None

    Return values
    ----------
    Returns True if the specified location is empty
    Returns False if the specified location is not empty
    
    """
    return board[index] == ' '

def full_board_check(board):
    """
    Function which checks if the board is full (No indexes within the List = ' ').

    Parameters
    ----------
    board : List

    Outputs
    ----------
    None

    Return values
    ----------
    Returns True if all the indexes of the board list are filled (No index = ' ')
    Returns False if any of the spaces are available ( = ' ')

    """
    
    for cell in board: # Iterates over every cell in the list
            if cell == ' ':
                return False # Returns False as soon as any empty cell is detected
    else:
        return True # Returns True if the for loop is not exited at any point

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

    

