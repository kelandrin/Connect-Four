import connectfour
from connectfour import InvalidMoveError

def welcome_banner() -> None:
    print("Welcome to Connect four!")

def explain_rules() -> None:
    print("The goal of the game is to connect 4 of your pieces either vertically, horizontally, or diagonally.")
    print("You will alternate turns by dropping a piece into one of the columns.")
    print("Option to 'pop' one of your pieces out if your piece is at the bottom row.")
    print("This will drop that column down one row")
    print("First player to have 4 pieces connected wins!" + "\n")
    _continue()

def _continue():
    if type(input('Press enter to continue: ')) == str:
        pass


def display_current_board(gamestate: 'Gamestate'):
    print("Current board:")
    _print_column_headers(connectfour.BOARD_COLUMNS)
    _print_row(gamestate)

def _print_column_headers(col:int):
    for i in range(col):
        print(i + 1, '  ', end = '')
    print("\n")

def _print_row(gamestate: 'Gamestate'):
    row = 0
    while True:
        if row != connectfour.BOARD_ROWS:
            for col in gamestate.board:
                _assign_board_spot_a_character(col,row)
            print("\n")
            row += 1
        else:
            break

def _assign_board_spot_a_character(col:int, row:int):
    if col[row] == 0:
        print('.' + '   ', end='')
    elif col[row] == 1:
        print('R' + '   ', end='')
    elif col[row] == 2:
        print('Y' + '   ', end='')

def print_whose_turn(gamestate:'Gamestate'):
    players_turn = _find_whose_turn(gamestate)
    print(f"It is now {players_turn}'s turn")

def _find_whose_turn(gamestate: 'Gamestate')-> str:
    if gamestate.turn == connectfour.RED:
        return 'RED'
    elif gamestate.turn == connectfour.YELLOW:
        return 'YELLOW'

def prompt_turn()-> str:
    while True:
        turn_choice_letter = input("Type 'd' to drop or 'p' to pop: ")
        if _is_turn_valid(turn_choice_letter) == True:
            turn_choice = _translate_turn_choice(turn_choice_letter)
            return turn_choice

def _is_turn_valid(turn_choice_letter:str)-> bool:
    if turn_choice_letter == 'd' or turn_choice_letter == 'drop':
        return True
    elif turn_choice_letter == 'p' or turn_choice_letter == 'pop':
        return True
    else:
        print('Invalid Choice')

def _translate_turn_choice(turn_choice:str)->str:
    if turn_choice == 'd' or turn_choice == 'drop':
        return 'DROP'
    elif turn_choice == 'p' or turn_choice == 'pop':
        return 'POP'

def choose_column(turn_choice:str)->int:
    while True:
        try:
            column_choice = int(input(f"Choose which column you would like to {turn_choice}: ")) - 1
            if connectfour._require_valid_column_number(column_choice) == None:
                return column_choice
        except ValueError:
            print('Invalid Column Choice, you must choose a number between 1 and',connectfour.BOARD_COLUMNS)

def execute_turn(gamestate: 'Gamestate', turn_choice:str, column_choice:int)-> 'Gamestate':
    if turn_choice == 'DROP':
        gamestate = connectfour.drop(gamestate,column_choice)
    elif turn_choice == 'POP':
        try:
            gamestate = connectfour.pop(gamestate,column_choice)
        except InvalidMoveError:
            print('Invalid Move: can only pop YOUR pieces from the bottom row')
    return gamestate

def winner_message(winner:str):
    print(winner, "has won!")
    print('Congratulations!')
