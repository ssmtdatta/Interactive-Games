"""
Tested on CodeSkulptor
www.codeskulptor.org

"Guess the number" is a two player game, where the first 
player thinks of a secret number in some known range while
the second player attempts to guess the number. After each
guess, the first player answers either 'Higher', 'Lower' 
or 'Correct' depending on whether the secret number is 
higher, lower or equal to the guess. The second player is 
allowed a limited number of guesses, more guesses for a 
wider range and fewer for a smaller range.
"""

import simplegui
import random

secret_num = None
usr_guess = None
max_guess = None


# helper function to start and restart the game     
def new_game(): 
    global secret_num, usr_guess
    secret_num = None
    usr_guess = None
    print "\n" + "... GUESS THE NUMBER ..."
    print "Select a range for the secret number,"
    print "then enter your guess in the box and hit return."
    
    
def guessWork():  
    global max_guess
    
    if secret_num == None:
        print "\n" + "Since you didn't select a range,"
        print "the range of 1 to 100 is selected by default."
        print "You can start over by selecting a range."
        range100()
        
    print "\n" + "Your guess is " + str(usr_guess)
    
    max_guess = max_guess - 1
    
    if max_guess == 0 and secret_num != usr_guess:
        print "No more guesses allowed."
        print "The secret number was " + str(secret_num) + ". Game over." + "\n"
        new_game() 
        
    else:
        if secret_num > usr_guess:
            print "Higher"
            print "Enter a new guess. " + str(max_guess) + " guess(es) remaining."
        elif secret_num < usr_guess:
            print "Lower"
            print "Enter a new guess. " + str(max_guess) + " guess(es) remaining."
        else:
            print "The secret number was " + str(secret_num)
            print "Correct guess." + " Game over." + "\n"
            new_game() 
         
    
# define event handlers for control panel
def range100():
    global secret_num, max_guess
    max_guess = 7
    secret_num = random.randrange(1,100)
    print "\n" + "... GAME BEGINS ..."
    print "A secret number between 1 and 100 has been picked." 
    print "Guess that number. You are allowed " + str(max_guess) + " guesses."
   
    
def range1000(): 
    global secret_num, max_guess
    max_guess = 10
    secret_num = random.randrange(1,1000)
    print "\n" + "... GAME BEGINS ..."
    print "A secret number between 1 and 1000 has been picked."
    print "Guess that number. You are allowed " + str(max_guess) + " guesses."
    
    
def input_guess(inp):
    global usr_guess
    if str.isdigit(inp):
        usr_guess = int(inp)
        guessWork()
    else:
        print "\n" + "Must enter a number and hit return. Try again."
        
        
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("1 to 100", range100, 200)
frame.add_button("1 to 1000", range1000, 200)
inp = frame.add_input("Enter Your Guess", input_guess, 200)

# start frame
frame.start()

# call new_game 
new_game()