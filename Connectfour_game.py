import connectfour
import overlap

def main():
    overlap.welcome_banner()
    overlap.explain_rules()
    gamestate = connectfour.new_game()
    while True:
        overlap.display_current_board(gamestate)
        overlap.print_whose_turn(gamestate)
        gamestate = run_turn(gamestate)

def run_turn(gamestate: 'Gamestate')-> tuple:
    turn_choice = overlap.prompt_turn()
    column = overlap.choose_column(turn_choice)
    gamestate = overlap.execute_turn(gamestate,turn_choice,column)
    if connectfour.winner(gamestate) != 0:
        overlap.display_current_board(gamestate)
        _winner_end_of_game(gamestate)
        quit()
    return gamestate

def _winner_end_of_game(gamestate: 'Gamestate')-> int:
    if connectfour.winner(gamestate) == 1:
        overlap.winner_message('RED')
    elif connectfour.winner(gamestate) == 2:
        overlap.winner_message('Yellow')

if __name__ == "__main__":
    main()
