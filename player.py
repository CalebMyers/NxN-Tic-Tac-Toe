#*******************************************************************
#
#  Program:     Project 3 -- 4x4 Tic-Tac-Toe
#
#  Author:      Caleb Myers
#  Email:       cm346613@ohio.edu
#
#  Class:       CS 3560 (Chelberg)
#
#  Description: This is the Player class file for prog3.
#
#  Date:        February 26, 2017
#
#*******************************************************************
class Player:

#*******************************************************************
#
#  Function:   __init__
#
#  Purpose:    this is the Player class constructor
#
#  Parameters: name - player name
#              games_won - games won by player
#              games_tied - games tied by player
#
#  Member/Global Variables: none
#
#  Pre Conditions: a Player object is assinged
#
#  Post Conditions: a Player object is returned
#
#  Calls: none
#
#*******************************************************************
    def __init__(self, name, games_won = 0, games_tied = 0):
        self.name = name
        self.games_won = games_won
        self.games_tied = games_tied

class Player1(Player):
    marker = 'X'

class Player2(Player):
    marker = 'O'
