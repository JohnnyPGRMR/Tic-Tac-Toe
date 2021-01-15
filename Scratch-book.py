es = ' '
seperator = ' | '
vals = [es,es,es,es,es,es,es,es,es]
board_key = [1,2,3,4,5,6,7,8,9]

def clear_screen():
    print('\n'*100)

def draw_board(seperator,vals):
    mvb = ' '*10
    line_between = '*'*14
    # First level of the board.
    print('\n'*2)
    print(mvb, vals[6],seperator,vals[7],seperator,vals[8])
    # Add a line seperating the levels   
    print(mvb,line_between)
    # Third level of the board.
    print(mvb,vals[3],seperator,vals[4],seperator,vals[5])
    # Add a line seperating the levels   
    print(mvb,line_between)
    print(mvb,vals[0],seperator,vals[1],seperator,vals[2])
    print('\n'*2)

def x_or_o():
    '''This function returns a tuple value of player1 and player2 for desired letters.'''
    # Initializing the variables to make typing easier below, currently equivalent to blank values.
    valid_letters = ['X','O'] 
    player1_letter = ' '
    player2_letter = ' '
    pass_condition = False
    while pass_condition == False:
        player1_letter = input('Player 1, please input your desired letter (X or O): ')
        # Check if the letter is a valid input.
        if valid_letters[0] in player1_letter.upper():
            pass_condition = True
            player2_letter = valid_letters[1]
            return player1_letter, player2_letter

        elif valid_letters[1] in player1_letter.upper():
            pass_condition = True
            player2_letter = valid_letters[0]
            return player1_letter, player2_letter

        else:
            print('Sorry, wrong value!!!!')
            pass


def user_choice():
    '''
    User inputs a number (0-10) and we return this
    in integer form.
    No paramter is passed when calling this function.
    '''
    choice = 'WRONG'
    within_range = False

    # while the choice is not a digit, keep asking for input.
    while choice.isdigit() == False or within_range == False:

        choice = input("Please input a number (1-9): ")

        # Error Message Check
        if choice.isdigit() == False:
            clear_screen()
            print("Sorry, but you did not enter an integer!  Please try again.")
        if choice.isdigit() == True:
            if int(choice) in range(1,10):
                within_range = True
            else:
                print("Sorry, but the number you entered is not valid, please input a number (1-9)")
                within_range = False


    return int(choice)

########### Need to write a function that would allow players to make a move on the board. ##############
def play_game(player1_letter,player2_letter,board_key,vals):
    # Setting a condition for ending the game.
    end_game = False
    # available_moves = board_key
    move = 100  # Assigned a random value outside of acceptable moves list.
    player_turn = 1     # Initializing value to the first move.

    while end_game == False:
        if es in vals:
            end_game = False
        else:
            end_game = True
            
        while player_turn == 1:
            move = user_choice()
            # Check to see if the move has already been made.
            if move not in vals:
                # Inserting value picked by player into the executed move list.
                vals[move - 1] = player1_letter
                player_turn = 2
                draw_board(seperator,vals)
            else:
                print("I'm sorry, but you've already made that move.")
            
        while player_turn == 2:
        # Check to see fi the move has already been made.
            move = user_choice()

            ######### Problem area in code...........................
            if vals[move - 1] == player1_letter or vals[move - 1] == player2_letter:
            # Inserting value picked by player into the executed move list.
                vals[move - 1] = player2_letter
                player_turn = 1
                draw_board(seperator,vals)
            else:
                print("I'm sorry, but you've already made that move.")

play_game('X','O',board_key,vals)