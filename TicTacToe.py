#*******************************************************************
#
#  Program:     Project 4 -- NxN Tic-Tac-Toe
#
#  Author:      Caleb Myers
#  Email:       cm346613@ohio.edu
#
#  Class:       CS 3560 (Chelberg)
#
#  Description: This is the Tic_tac_toe class file for prog3.
#
#  Date:        February 26, 2017
#
#*******************************************************************
import player
import sys
from random import randint
class Tic_Tac_Toe:

#*******************************************************************
#
#  Function:   __init__
#
#  Purpose:    constructor for Tic_tac_toe class
#
#  Parameters: move_count - number of moves made in game
#              board      - list of markers and empty spaces on game
#                           board
#              players    - list of game players (player class objects)
#
#  Member/Global Variables: none
#
#  Pre Conditions: Tic_tac_toe object is assigned
#
#  Post Conditions: Tic_tac_toe object is returned
#
#  Calls:  member function new_board
#          member function get_players
#
#*******************************************************************
    # added board_size
    def __init__(self, move_count = 0, board = None, players = None, board_size = None):
        self.move_count = move_count
        if board_size != None:
            self.board_size = board_size
        else:
            self.board_size = self.get_board_size()
        self.num_spaces = self.board_size * self.board_size
        if board != None:
            self.board = board
        else:
            self.board = self.new_board()
        if players != None:
            self.players = players
        else:
            self.players = self.get_players()
       


# adding get_board_size()
    def get_board_size(self):
        try:
            board_size = input('Enter the size you would like the board to be:\n')
        except NameError:
            print 'Invalid Entry: Board size must be a number'
            print 'Please try again'
            return self.get_board_size()
        if board_size < 2:
            print 'Invalid Size: Board size has a mininum of 2'
            print 'Please try agian'
            return self.get_board_size()
        else:
            return board_size
      
        


#*******************************************************************
#
#  Function:   new_board
#
#  Purpose:    creates an empty board
#
#  Parameters: none
#
#  Member/Global Variables: new_board - list to hold spaces
#
#  Pre Conditions: a new game is started
#
#  Post Conditions: an empty board is returned
#
#  Calls: function range
#
#*******************************************************************
 # added board_size()
    def new_board(self):
        new_board = []
        for i in range(self.num_spaces):
            new_board.append(' ')
        return new_board

#*******************************************************************
#
#  Function:   get_players
#
#  Purpose:    create and return a list of player objects
#
#  Parameters: none
#
#  Member/Global Variables: name1 - player one's name
#                           name2 - player two's name
#
#  Pre Conditions: a new game is started
#
#  Post Conditions: list of player objects is returned
#
#  Calls:  raw_input
#          player class constructor Player1
#          player class constructor Player2
#
#*******************************************************************    
    def get_players(self):
        name1 = raw_input("Enter player one's name\n")
        name2 = raw_input("Enter player two's name\n")
        random_num = randint(0,1)
        if random_num == 0:
            print name1, 'will use the marker X and will go first'
            print name2, 'will use the marker O and will go second'
            p1 = player.Player1(name1)
            p2 = player.Player2(name2)
        else:
            print name2, 'will use the marker X and will go first'
            print name1, 'will use the marker O and will go second'
            p1 = player.Player1(name2)
            p2 = player.Player2(name1)
        players = [p1, p2]
        return players
            

#*******************************************************************
#
#  Function:   print_board
#
#  Purpose:    prints the current game board
#
#  Parameters: none
#
#  Member/Global Variables: newline - holds the numbers where
#                                     a newline will be output
#                                     in for loop
#                           board   - current game board
#
#  Pre Conditions: user enters p
#
#  Post Conditions: current game board is printed
#
#  Calls: function range
#
#*******************************************************************     
  # adding board_size
    def print_board(self):
        index = 0
        for i in range(self.num_spaces):
            index += 1
            sys.stdout.write('  ')
            sys.stdout.write(self.board[i])
            if index != self.board_size:
                sys.stdout.write(' |')
            else:
                index = 0
                print
                if i != self.num_spaces - 1:
                    print '-' * (self.board_size * 5 - 1)

        

#*******************************************************************
#
#  Function:   print_help
#
#  Purpose:    prints the help board
#
#  Parameters: none
#
#  Member/Global Variables: none
#
#  Pre Conditions: user enters h
#
#  Post Conditions: help board is printed
#
#  Calls: function range
#
#*******************************************************************
  #adding board_size
    def print_help(self):
        index = 0
        for i in range(self.num_spaces):
            index += 1
            if i < 10:
                sys.stdout.write('  ')
            elif i < 100:
                sys.stdout.write(' ')
            sys.stdout.write(str(i))   
            if index != self.board_size:
                sys.stdout.write(' |')
            else:
                index = 0
                print
                if i != self.num_spaces - 1:
                    print '-' * (self.board_size * 5 - 1)

#*******************************************************************
#
#  Function:   move
#
#  Purpose:    place user marker on board and increment move count
#
#  Parameters: board_space - location on game board
#              marker      - current players marker
#
#  Member/Global Variables: none
#
#  Pre Conditions: user enters a valid move
#
#  Post Conditions: user's marker is placed on board, move_count is
#                   incremented
#
#  Calls: none
#
#*******************************************************************
    def move(self, board_space, marker):
        self.board[board_space] = marker
        self.move_count += 1

#*******************************************************************
#
#  Function:    open_board_space
#
#  Purpose:     checks if board space is open
#
#  Parameters:  board_space - location on game board
#
#  Member/Global Variables: none
#
#  Pre Conditions: user enters a move
#
#  Post Conditions: true is returned if space is open, false is returned
#                   if space is occupied
#
#  Calls: none
#
#*******************************************************************
    def open_board_space(self,board_space):
        return self.board[board_space] == ' '

#*******************************************************************
#
#  Function:   move_in_range
#
#  Purpose:    check if user move is in the valid range (0-15)
#
#  Parameters: board_space - location on game board
#
#  Member/Global Variables: none
#
#  Pre Conditions: user enters a move
#
#  Post Conditions: true is returned if move is in range, false if not
#
#  Calls: none
#
#*******************************************************************
    # added num_spaces
    def move_in_range(self, board_space):
        return board_space >= 0 and board_space <= self.num_spaces
  
#*******************************************************************
#
#  Function:   legal_move
#
#  Purpose:    checks if move is leagal 
#
#  Parameters: board_space - location on game board
#
#  Member/Global Variables: none
#
#  Pre Conditions: user enters a move
#
#  Post Conditions: true is returned if move is legal, false if not
#
#  Calls: member function move_in_range
#         member function open_board_space
#
#*******************************************************************
    def legal_move(self, board_space):
        return self.move_in_range(board_space) and self.open_board_space(board_space)

#*******************************************************************
#
#  Function:   check_row
#
#  Purpose:    checks row to see if anyone has won game
#
#  Parameters: index - number of starting element of a row
#
#  Member/Global Variables: marker - marker on game board at index
#
#  Pre Conditions: a move was made
#
#  Post Conditions: if a row contains four of the same markers that
#                   marker is returned, a '#' is returned if not
#
#  Calls: function range
#
#*******************************************************************
 # added board_size
    def check_row(self,index):
        marker = self.board[index]
        if marker == ' ': return '#'
        for i in range(self.board_size - 1):
          index += 1
          if self.board[index] != marker:
              return '#'
        return marker

#*******************************************************************
#
#  Function:   check_column
#
#  Purpose:    checks column to see if anyone has won game
#
#  Parameters: index - number of starting element of a column
#
#  Member/Global Variables: marker - marker on game board at index
#
#  Pre Conditions: a move was made
#
#  Post Conditions: if a column contains four of the same markers that
#                   marker is returned, a '#' is returned if not
#
#  Calls: function range
#
#*******************************************************************
   # added board size
    def check_column(self, index):
        marker = self.board[index]
        if marker == ' ': return '#'
        for i in range(self.board_size - 1):
          index += self.board_size
          if self.board[index] != marker:
              return '#'
        return marker

#*******************************************************************
#
#  Function:   check_rising_diagonal
#
#  Purpose:    checks rising diagonal to see if anyone has won game
#
#  Parameters: none
#
#  Member/Global Variables: marker - marker on game board at index
#                           index  - number of starting element of 
#                                    the diagonal
#
#  Pre Conditions: a move was made
#
#  Post Conditions: if a diagonal contains four of the same markers that
#                   marker is returned, a '#' is returned if not
#
#  Calls: function range
#
#*******************************************************************
   # added stuff
    def check_rising_diagonal(self):
        index = self.num_spaces - self.board_size
        marker = self.board[index]
        if marker == ' ': return '#'
        for i in range(self.board_size - 1):
          index -= (self.board_size - 1)
          if self.board[index] != marker:
              return '#'
        return marker


#*******************************************************************
#
#  Function:   check_falling_diagonal
#
#  Purpose:    checks falling diagonal to see if anyone has won game
#
#  Parameters: none
#
#  Member/Global Variables: marker - marker on game board at index
#                           index  - number of starting element of 
#                                    the diagonal
#
#  Pre Conditions: a move was made
#
#  Post Conditions: if a diagonal contains four of the same markers that
#                   marker is returned, a '#' is returned if not
#
#  Calls: function range
#
#*******************************************************************
   # added stuff
    def check_falling_diagonal(self):
        index = 0
        marker = self.board[index]
        if marker == ' ': return '#'
        for i in range(self.board_size - 1):
          index += (self.board_size + 1)
          if self.board[index] != marker:
              return '#'
        return marker

#*******************************************************************
#
#  Function:   who_won
#
#  Purpose:    see if game has been won
#
#  Parameters: none
#
#  Member/Global Variables: marker_list - list to hold markers
#
#  Pre Conditions: a move was made
#
#  Post Conditions: if a player has won there marker will be returned,
#                   if not a '#' will be returned
#
#  Calls: function range
#         function append
#
#*******************************************************************
   # added stuff
    def who_won(self):
        marker_list = []
        for i in range(self.board_size):
            marker_list.append(self.check_column(i))
        it = 0
        for i in range(self.board_size):
            marker_list.append(self.check_row(it))
            it += self.board_size
        marker_list.append(self.check_rising_diagonal())
        marker_list.append(self.check_falling_diagonal())
        for i in marker_list:
            if i != '#':
                return i
        return '#'

#*******************************************************************
#
#  Function:   draw
#
#  Purpose:    checks to see if game is a draw
#
#  Parameters: none
# 
#  Member/Global Variables: move_count - number of moves in game
#
#  Pre Conditions: move was made
#
#  Post Conditions: true is returned if game is a draw, false if not
#
#  Calls: none
#
#*******************************************************************
  # added stuff
    def draw(self):
        if self.move_count == self.num_spaces:
            return True
        return False
