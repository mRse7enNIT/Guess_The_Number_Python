
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import math
import random
range = 100
no_of_guess = 0
secret_number = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global range
    global no_of_guess
    print "\nNew game. Range is from 0 to " ,range
    if range == 100:
        no_of_guess = 7
    elif range ==1000:
        no_of_guess = 10
    print "Number of remaining guesses is " ,no_of_guess
    secret_number = random.randrange(0, range)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
     global range
     range = 1000
     new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    print "\nGuess was ", guess 
    global no_of_guess
    no_of_guess = no_of_guess - 1
    
    if no_of_guess >=0:
        
        if int(guess) > secret_number :
            print "Lower!"
            print 'Number of remaining guesses is' ,no_of_guess
        elif int(guess) < secret_number :
            print "Higher!"
            print 'Number of remaining guesses is' ,no_of_guess
        elif int(guess) == secret_number :
            print "Correct!"
            new_game()
    else:
        print "Out of guesses"
        new_game()
    
# create frame
f = simplegui.create_frame("guess the number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100,100)
f.add_button("Range is [0,1000)", range1000,100)
f.add_input('Enter a guess', input_guess, 200)
f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
