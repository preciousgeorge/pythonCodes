import random
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors



#diction of choices
global_dict = {0 : 'rock', 1 : 'spock', 2 :  'paper' ,
               3 : 'lizard', 4 : 'scissors'}


# helper functions

# convert name to number 
def name_to_number(name):
    name_to_lower = name.lower()
   
    global global_dict
    length = len(global_dict)
    for i in range(length):  
        if name_to_lower == global_dict[i]:
            return i
    
#convert number to name    
def number_to_name(number):
    #return a string 
    global global_dict
    return global_dict[number]
    
    
#rpsls function, checks user choice angainst a random 
#computer choice to show winner
def rpsls(player_choice): 

    # print a blank line to separate consecutive games
    print " "

    # print out the message for the player's choice
    
    print "Player chooses ",player_choice

    # convert the player's choice to player_number using the function name_to_number()
    
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    
    comp_number = random.randrange(5)
    # convert comp_number to comp_choice using the function number_to_name()
    
    comp_choice = number_to_name(comp_number) 
    # print out the message for computer's choice
    
    print "The Computer chooses ",comp_choice

    # compute difference of comp_number and player_number modulo five
    
    diff = (player_number - comp_number) % 5 
    # use if/elif/else to determine winner, print winner message
    if diff == 0:
        print "It's a tie, play again"
    elif diff == 1 or diff == 2:
        print "Player Wins"
    else:
        print "Computer Wins"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



# always remember to check your completed program against the grading rubric


