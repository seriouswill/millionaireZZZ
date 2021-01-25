# if the player inputs a command that is other than A B C or D, and is locked to a lifeline, it will implement the lifeline

#lifeline input specific

#do the lifeline function 
    #return the lifeline answer - specific

#import libraries etc at top

import random

#delete the lifeline from being an option

# i.e. 50/50 is "F"
#       Phone a friend is "P"
#       Ask the audience is "Z"

#if user types lifeline at any point they will be given the instructions for calling them.

# def help():
#     console_slow_type("""Enter "F" for Fifty / Fifty - This will remove two incorrect answers and leave two remaining right answers. \n 
#     Enter "P" for Phone a Friend - This will give you the option of calling upon your designated expert.
#     Whether they're smart or not is your stupid fault. Isn't it. \n
#     Enter "Z" for Ask the Audience - this will put the question to our room full of Brainiacs.    
#     To hear this again, type 'help'.""")
    
# def lifeline():
#     if answer == "L":
#         console_slow_type("""Enter "F" for Fifty / Fifty - This will remove two incorrect answers and leave two remaining right answers. \n 
#     Enter "P" for Phone a Friend - This will give you the option of calling upon your designated expert.
#     Whether they're smart or not is your stupid fault. Isn't it. \n
#     Enter "Z" for Ask the Audience - this will put the question to our room full of Brainiacs.    
#     """)
#     choice = input("Choose a lifeline")
#     if choice == "F":
#         fifty_fifty()
#     elif choice == "P":
#         phone_a_friend()
#     elif choice == "Z":
#         ask_the_audience()
#if the user types lifeline - if input is "lifeline", the function lifeline will execute.

                                        #----|||----#

#------- user enters "F":

potential_answers = [
    "A",
    "B",
    "C",
    "D"
]

correct_answer1 = "C"
correct_answer2 = "B"

def fifty_fifty (correct_answer1, correct_answer2, potential_answers) :
            
            if correct_answer2 != "":       #if we want this we put the correct answer in corect_answer2 
                console_slow_type(f"The two remaining correct answers are...{correct_answer2} and {correct_answer1}")
            else:                           # otherwise leave the correct_answer2 as an EMPTY STRING
                potential_answers.remove(correct_answer1)
            # potential_answers.remove(random.randint(0,len(potential_answers)))
                fifty_answer = potential_answers[random.randint(0,len(potential_answers)-1)] 
                console_slow_type(f"The two remaining correct answers are...{fifty_answer} and {correct_answer1}")
                console_slow_type(len(potential_answers))
            


            # if correct_answer == "A" and "B" or "A" and "C" or "A"
            




            
#remove the right answer from potential,  select one wrong answer,and one right answer  
# correct_answer == potential_answers[]
# potential_answers.index("A","B","C","D")
            #how do we turn the list item into the number that it is in the list.
            #if we remove two, then print remaining?
    
fifty_fifty(correct_answer1, correct_answer2, potential_answers)

# if answer = input("F"):
#     fifty_fifty(correct_answer, potential_answers)
# elif answer = input("P"):
#     #phone function
# elif answer = input("Z"):
