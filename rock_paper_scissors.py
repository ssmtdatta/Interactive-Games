"""
Tested on CodeSkulptor
www.codeskulptor.org

Game: Rock-Paper-Scissors-Lizard-Spock 
Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows
five choices. Each choice wins against two other choices, loses against two other choices
and ties against itself. 

Scissors cut Paper covers Rock crushes Lizard poisons Spock smashes Scissors 
decapitates Lizard eats Paper

The key idea of this program is to equate the strings
"rock", "paper", "scissors", "lizard", "Spock" to numbers as follows and then set us
logical statements to determine who wins.
0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors 
"""


import random

def name_to_number(name):
    """
    Associate each element of the game with a number.
    """
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        exit("That is an invalid choice. The player must choose from rock, Spock, paper, lizard and scissors.")   
    return number


def number_to_name(number):
    """
    Convert the names of elements of the game to their 
    designated number.
    """
    if number == 0:
        name = "rock"
    if number == 1:
        name = "Spock"
    if number == 2:
        name = "paper"
    if number == 3:
        name = "lizard"
    if number == 4:
        name = "scissors"
    return name
    
    
def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print " "
    
    # print out the message for the player's choice
    print "The player's choice is", player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "The computer's choice is", comp_choice
    
    # compute difference of comp_number and player_number modulo five
    diff = player_number - comp_number
    
    # use if/elif/else to determine winner, print winner message
    if diff < 0:
        diff = diff%5
    if diff >= 1 and diff <= 2:
        print "Player wins!"
    elif diff >= 3 and diff <= 4:
        print "Computer wins!"
    else:
        print "It's a tie."

    



