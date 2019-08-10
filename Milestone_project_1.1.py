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
    """
    Small function used to insert new markers into the list which represents the game board
    
    Parameters
    ----------
    board : List
    index : int
    player : char

    Outputs
    ----------
    None

    Return values
    ----------
    None 

    """
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
    """
    Function which stores user input of position where they want to place one of their markers.
    Uses the space_check() function to check whether the user's selected index is empty or not.
    Calls the place_marker() function to place the marker into the board, once the user's selected index has been checked
    
    Parameters
    ----------
    board : List
    player : char

    Outputs
    ----------
    Print statements requesting user input of their chosen index for placing a marker

    Return values
    ----------
    None
    
    """
    input_pos = int(input(f"Player {player}: Please select the index where you would like to place your symbol (1-9): ")) # Input statement that stores user input in input_pos variable

    while not space_check(board, input_pos-1): # While the users input does not correlate to a free space on the board, request that they choose andother
        input_pos = int(input("You cannot place your symbol there, as that position is already occupied. Please try again\n\nPlease select the index where you would like to place your symbol (1-9): "))
    place_marker(board, input_pos-1, player) # Once an approved index has been selected, call place_marker() to place it into the board

def replay():
    """
    Function which is called at the end of a game to ask the user if they would like to play again.
    If yes, the function calls os.system('cls') to clear the screen, and run_game() to restart the game
    If no, the function calls exit() to exit the program in the console
    
    Parameters
    ----------
    None

    Outputs
    ----------
    Print statements requesting user choose weather to continue or not

    Return values
    ----------
    None
    
    """
    choice = input("Would you like to replay? Yes or No: ")
    if choice.lower() == 'yes':
        os.system('cls')
        run_game()
    elif choice.lower() == 'no':
        exit()

def run_game():
    """
    Main function which handles game progression and calls other functions for specific game actions
    
    Parameters
    ----------
    None

    Outputs
    ----------
    Victory statement when a victory condition is met
    Message to indicate a full board when the board is full but no victory condition has been met

    Return values
    ----------
    None
    
    """

    board = [' '] * 9 # Defines a List of size 9 where all elements start as ' ', to be used to store x's and o's
    players = player_choose_symbol() # Asigns the output of player_choose_symbol() to be stored in a tuple variable
    draw_board(board) # Draws intial empty board
    counter = -1 # Counter which will be used to toggle between x and o in players
    while not win_check(board) and not full_board_check(board): # While the board is not full and no victory condition has been met
        counter += 1 # Counter incremented before player choice so that it starts at 0 and so that the victory statements after the while loop has exited display the same symbol as 
                     # the one used by the player who's turn it was when the while loops exits
        player_choice(board, players[counter % 2]) # Call to player_choice() allows the current user to take their turn placing their marker on the board
    # When the while loop exits, check if a victory condition is met. If so, output a victory message for the player who played the winning move.
    # If no victory condition is met then the board must be empty
    if win_check(board):
        print(f"Victory! The {players[counter % 2]}'s win!!!!'") # Victory message
        replay() # Call replay() to ask players if they wish to play another game
    elif full_board_check(board):
        print("The board is full and there are no winners") # Board full message
        replay() # Call replay() to ask players if they wish to play another game

run_game() # Call to run_game() to run the program