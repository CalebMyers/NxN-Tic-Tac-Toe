#*******************************************************************
#
#  Program:     Project 3 -- 4x4 Tic-Tac-Toe
#
#  Author:      Caleb Myers
#  Email:       cm346613@ohio.edu
#
#  Class:       CS 3560 (Chelberg)
#
#  Description: This is a two player game of tic-tac-toe on a NxN
#               board (N is selected by the user). 
#               At any point the game can be saved, when 
#               a game is started the user is asked if they would
#               like to load a game, they can do this by entering 
#               the file name. To play, each player enters the 
#               number representing the space they would like to 
#               take. Other commands the user can enter are:
#               'p' (prints current game board), 'h' (prints the 
#               board with numbers), 's' (saves game), 'r' (player
#               resigns, this counts as a loss), 'q' (quit immediately
#               without saving)
#
#  Date:        February 26, 2017
#
#*******************************************************************
import games
import player
import re
import string


#*******************************************************************
#
#  Function:   play
#
#  Purpose:    top level function that plays a game of 4x4
#              tic-tac-toe
#
#  Parameters: none
#
#  Member/Global Variables: current_game  - tic-tac-toe class object
#                           players       - list of player class objects
#                           end_game      - bool variable in while loop
#                                          that dictates when game is
#                                          ended
#                           current_player - player class object
#                           user_input     - input from the user
#
#  Pre Conditions:  none
#
#  Post Conditions: game of 4x4 tic-tac-toe is played
#
#  Calls:  function get_game
#          function raw_input
#          string member function strip
#          function is_int
#          function play_next_move
#          function save
#          tic-tac-toe member function print_board
#          tic-tac-toe member function print_help
#          function game_over
#
#*******************************************************************
def play():
    print 'Welcome to NxN Tic-Tac-Toe!'
    print 'This game will keep track of your games won and games tied.'
    print 'To keep track of these, when a game is finished save it and'
    print 'when you play your next game load that file.'
    current_game = get_game()
    players = current_game.players
    end_game = False
    while not end_game:
        current_player = players[current_game.move_count % 2]
        print "It's", current_player.name + "'s", 'turn (' + current_player.marker + ')'
        user_input = raw_input()
        user_input = user_input.strip()
        if is_int(user_input):
            end_game = play_next_move(user_input, current_game, current_player)
        elif user_input.lower() == 's':
            save(current_game)
        elif user_input.lower() == 'p':
            current_game.print_board()
        elif user_input.lower() == 'h':
            current_game.print_help()
        elif user_input.lower() == 'q':
            end_game = True
        elif user_input.lower() == 'r':
            end_game = game_over(current_game)
        else:
            print 'Invalid entry, please try again'
            

#*******************************************************************
#
#  Function:   player_next_move
#
#  Purpose:    plays users next move if valid, if not valid displays
#              message              
#
#  Parameters: user_input     - input from the user
#              current_game   - tic-tac-toe class object
#              current_player - player class object
#
#  Member/Global Variables: none
#
#  Pre Conditions:  parameters have valid values
#
#  Post Conditions: plays users next move if valid, if not valid displays
#                   message 
#
#  Calls:  function int
#          tic-tac-toe member function legal_move
#          tic-tac-toe member function move
#          tic-tac-toe member function who_won
#          function game_over
#
#*******************************************************************
def play_next_move(user_input, current_game, current_player):
    user_input = int(user_input)
    if current_game.legal_move(user_input):
        current_game.move(user_input, current_player.marker)
        if current_game.who_won() != '#' or current_game.draw():
            return game_over(current_game)
    else:
        print 'Invalid entry, please try again'
        print "You can print the current game board by entering 'p'"


#*******************************************************************
#
#  Function:   is_int
#
#  Purpose:    see if string is an integer
#
#  Parameters: user_input - input from the user
#
#  Member/Global Variables: none
#
#  Pre Conditions:  user_input is a string
#
#  Post Conditions: true is returned if user_input is the string
#                   of an integer, false is returned if not
#
#  Calls: function int
#
#*******************************************************************
def is_int(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False
    

#*******************************************************************
#
#  Function:   get_game
#
#  Purpose:    returns a tic_tac_toe class object
#
#  Parameters: none
#
#  Member/Global Variables: user_input - input from the user
#
#  Pre Conditions: none
#
#  Post Conditions: a tic_tac_toe class object is returned
#
#  Calls: function get_y_or_n
#         function load()
#         function get_game
#
#*******************************************************************
def get_game():
    user_input = get_y_or_n('Would you like to load a saved game?')
    if user_input == 'y':
        return load()
    elif user_input == 'n':
        return games.Tic_Tac_Toe()
 

#*******************************************************************
#
#  Function:   game_over
#
#  Purpose:    prints who won, each players wins and ties. Asks if
#              the game should be saved and then asks if the users
#              would like to play again
#
#  Parameters: current_game - tic_tac_toe class object
#
#  Member/Global Variables: players    - list of player class objects
#                           winner     - player class object
#                           user_input - input from the user
#
#  Pre Conditions: game is won or drawn
#
#  Post Conditions: prints winner, asks if game should be saved and 
#                   if the users want to play again
#
#  Calls:  function print_scores
#          tic_tac_toe member function new_board
#          function save
#          function play
#
#*******************************************************************
def game_over(current_game):
    players = current_game.players
    if current_game.draw():
        print "It's a draw!"
        players[0].games_tied += 1
        players[1].games_tied += 1
    else:
        winner = current_game.players[(current_game.move_count - 1) % 2]
        print winner.name, 'won!'
        winner.games_won += 1
    print_scores(players)
    current_game.board = current_game.new_board()
    current_game.move_count = 0
    user_input = get_y_or_n('Would you like to save this game?')
    if user_input == 'y':
        save(current_game)
    user_input = get_y_or_n('Would you like to play another game?')
    if user_input == 'y':
        play()
    return True

#*******************************************************************
#
#  Function:   print_scores
#
#  Purpose:    prints each players wins and ties
#
#  Parameters: players - list of player class objects
#
#  Member/Global Variables: none
#
#  Pre Conditions:  the game has ended
#
#  Post Conditions: each players wins and ties are printed
#
#  Calls: none
#
#*******************************************************************
def print_scores(players):
    print 'Games Won:'
    print players[0].name + ': ',
    print players[0].games_won
    print players[1].name + ': ',
    print players[1].games_won
    print 'Games Tied:'
    print players[0].name + ': ',
    print players[0].games_tied
    print players[1].name + ': ',
    print players[1].games_tied


#*******************************************************************
#
#  Function:   get_y_or_n
#
#  Purpose:    returns 'y' or 'n' based on users input
#
#  Parameters: question - a question to ask the user, string type
#
#  Member/Global Variables: user_input - input from the user
#
#  Pre Conditions: none
#
#  Post Conditions: 'y' or 'n' is returned
#
#  Calls:  functinon strip
#          function lower
#          get_y_or_n
#
#*******************************************************************
def get_y_or_n(question):
    user_input = raw_input(question + '(Enter y or n)\n')
    user_input = user_input.strip()
    user_input = user_input.lower()
    if user_input == 'y':
        return 'y'
    elif user_input == 'n':
        return 'n'
    else:
        print 'Invalid entry, please try again'
        get_y_or_n(question)


#*******************************************************************
#
#  Function:   save
#
#  Purpose:    saves current game into a file
#
#  Parameters: current_game - tic_tac_toe class object
#
#  Member/Global Variables: file_name - name of file for game to be 
#                                       saved in
#                           output_file - output variable
#
#  Pre Conditions:  user chose to save game
#
#  Post Conditions: game is saved to a file
#
#  Calls:  function open
#          function write
#
#*******************************************************************
  # adding board Size
def save(current_game):
    p1 = current_game.players[0]
    p2 = current_game.players[1]
    file_name = raw_input("Enter the file to save the game in\n")
    output_file = open(file_name, 'w')
    output_file.write('player#' + p1.name + '#' + str(p1.games_won) + '#' + str(p1.games_tied) + '#\n' )
    output_file.write('player#' + p2.name + '#' + str(p2.games_won) + '#' + str(p2.games_tied) + '#\n' )
    output_file.write('board#')
    for i in current_game.board:
        output_file.write(i + '#')
    output_file.write('\n')
    output_file.write('movecount#' + str(current_game.move_count) + '#\n')
    output_file.write('boardsize#' + str(current_game.board_size) + '#')
    output_file.close()

  





#*******************************************************************
#
#  Function:   load
#
#  Purpose:    loads in a previously saved game
#
#  Parameters: none
#
#  Member/Global Variables: file_name   - name of file to be read
#                           file_opened - bool to tell if file was
#                                         opened successfully
#                           input_file  - input variable
#                           lines       - lines from input file
#                           p1          - player class object
#                           p2          - player class object
#                           players     - list of player class objetcs
#                           board       - array of board contents
#                           move_count  - number of moves
#
#  Pre Conditions:  user chose to load a saved game
#
#  Post Conditions: previously saved game is loaded
#
#  Calls:  function get_input_file
#          function open
#          function readlines
#          function read_player
#          function read_board
#          read_move_count
#
#*******************************************************************
def load():
    input_file = get_input_file()
    lines = input_file.readlines()
    input_file.close()
    p1 = read_player(lines[0], 'X')
    p2 = read_player(lines[1], 'O')
    players = [p1, p2]
    board = read_board(lines[2])
    move_count = read_move_count(lines[3])
    board_size = read_board_size(lines[4])
    return games.Tic_Tac_Toe(int(move_count), board, players, board_size)

#*******************************************************************
#
#  Function:   get_input_file
#
#  Purpose:    returns a file being read in
#
#  Parameters: none
#
#  Member/Global Variables: file_name   - name of the file
#                           file_opened - bool representing if the 
#                                         file was opened
#                           input_file  - file being read in
#
#  Pre Conditions:    user chose to load in a game
#
#  Post Conditions:   input file is opened and returned
#
#  Calls:  function raw_input
#          function open
#
#*******************************************************************
def get_input_file():
    file_name = raw_input('Enter the name of the file to load\n')
    file_opened = False
    while not file_opened:
        try:
            input_file = open(file_name, 'r')
            file_opened = True
        except IOError:
            print 'Invalid entry, please try again'
            file_name = raw_input('Enter the name of the file to load\n')
    return input_file


#*******************************************************************
#
#  Function:   read_player1
#
#  Purpose:    reads in player info and returns a player class object
#              with that info
#
#  Parameters: line   - line from the input file
#              marker - marker for that player
#
#  Member/Global Variables: player_re    - regex to find player  info
#                           player_list - list of player info
#                           p            - player class object
#
#  Pre Conditions:  user chose to load a game
#
#  Post Conditions: player class object is returned
#
#  Calls:  function findall
#          class constructor Player1
#          class constructor Player2
#
#*******************************************************************    
def read_player(line, marker):
    player_re = 'player([#\w]*)'
    player_list = re.findall(player_re, line)[0].split('#')[1:4]
    if marker == 'X':
        p = player.Player1(player_list[0],int(player_list[1]), int(player_list[2]))
    else:
        p = player.Player2(player_list[0],int(player_list[1]), int(player_list[2]))
    return p



#*******************************************************************
#
#  Function:   read_board
#
#  Purpose:    reads in board
#
#  Parameters: line - line from the input file
#
#  Member/Global Variables: board_re   - regex to find board
#                           board_list - list of the board elements
#
#  Pre Conditions:  user chose to load a game
#
#  Post Conditions: board is returned
#
#  Calls:  function findall
#
#*******************************************************************  
def read_board(line):
    board_re = 'board([#\w\s]*)'
    board_list = re.findall(board_re, line)[0].split('#')[1:]
    return board_list


#*******************************************************************
#
#  Function:   read_move_count
#
#  Purpose:    reads in move count
#
#  Parameters: line - line from the input file
#
#  Member/Global Variables: move_count_re - regex to find player move_count
#                           move_count    - number of moves made in game
#
#  Pre Conditions:  user chose to load a game
#
#  Post Conditions: move count is returned
#
#  Calls:  function findall
#          function int
#
#*******************************************************************  
def read_move_count(line):
    move_count_re = 'movecount([#\w]*)'
    move_count = re.findall(move_count_re, line)[0].replace('#','')
    return int(move_count)


def read_board_size(line):
    board_size_re = 'boardsize([#\w]*)'
    board_size = re.findall(board_size_re, line)[0].replace('#','')
    return int(board_size)
    
    
play() # calls top level play function
