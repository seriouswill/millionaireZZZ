#IMPORTS        
import time
import random
import sys
import os
import subprocess

#FUNCTIONS      #NOTE: SK: Do we want these in particular

#ASCII FUNCTIONS

def game_over():
    time.sleep(1)
    print(u"""
                  *             )            (                                                                                                               
  \u001b[33;1m (       ( \u001b[0m    (  `         \u001b[33;1m( /\u001b[0m(          \u001b[33;1m  )\ \u001b[0m )                                                                                                            
  \u001b[33;1m )\ \u001b[0m)    )\u001b[33;1m\  \u001b[0m  )\)\u001b[33;1m)(\u001b[0m  (     )\u001b[33;1m\ \u001b[0m()\u001b[33;1m)( \u001b[0m  (  (  (\u001b[33;1m()/\u001b[0m\u001b[33;1m(\u001b[0m                                                                                                            
  \u001b[33m(()/( ((((_)( ((_)()\ )\   ((_)\ )\  )\ )\  /(_))                                                                                                           
  /(_))_)\ _ )\(_()((_((_)    ((_((_)((_((_)(_)) \u001b[0m                                                                                                             
  \u001b[31;1m(_)) __(_)_\(_|  \/  | __|  / _ \ \ / /| __| _ \                                                                                                             
    | (_ |/ _ \ | |\/| | _|  | (_) \ V / | _||   /                                                                                                            
     \___/_/ \_\|_|  |_|___|  \___/ \_/  |___|_|_\                                                                                                            
                                                                                                                                                              
  \u001b[0m""")
    time.sleep(2)

def game_winner_art():
    time.sleep(3)
    print(u"""\u001b[33;1m

                )       )            (                                 (                         (         )       )   (        ____              
        (     ( /(    ( /(   (        )\ )     (        *   )           )\ )     (        *   )   )\ )   ( /(    ( /(   )\ )    |   /              
        )\    )\())   )\())  )\ )    (()/(     )\     ` )  /(      (   (()/(     )\     ` )  /(  (()/(   )\())   )\()) (()/(    |  /               
    (((_)  ((_)\   ((_)\  (()/(     /(_)) ((((_)(    ( )(_))     )\   /(_)) ((((_)(    ( )(_))  /(_)) ((_)\   ((_)\   /(_))   | /                
    )\___    ((_)   _((_)  /(_))_  (_))    )\ _ )\  (_(_())   _ ((_) (_))    )\ _ )\  (_(_())  (_))     ((_)   _((_) (_))     |/                 
    \u001b[37;1m  ((/ __|  / _ \  | \| | (_)) __| | _ \   (_)_\(_) |_   _|  | | | | | |     (_)_\(_) |_   _|  |_ _|   / _ \  | \| | / __|   (                   
       | (__  | (_) | | .` |   | (_ | |   /    / _ \     | |    | |_| | | |__    / _ \     | |     | |   | (_) | | .` | \__ \   )\                  
        \___|  \___/  |_|\_|    \___| |_|_\   /_/ \_\    |_|     \___/  |____|  /_/ \_\    |_|    |___|   \___/  |_|\_| |___/  ((_)                 
                                                                                                                                                    
    \u001b[31;1m     )      )                                                                        )                                      *              ____ 
    ( /(   ( /(                      (            (        *   )            *   )   ( /(                 (          (       (  `            |   / 
    )\())  )\())      (            ( )\   (       )\     ` )  /(          ` )  /(   )\())  (             )\ )       )\      )\))(    (      |  /  
    ((_)\  ((_)\       )\           )((_)  )\   ((((_)(    ( )(_))          ( )(_)) ((_)\   )\           (()/(    ((((_)(   ((_)()\   )\     | /   
    __ ((_)   ((_)   _ ((_)         ((_)_  ((_)   )\ _ )\  (_(_())          (_(_())   _((_) ((_)           /(_))_   )\ _ )\  (_()((_) ((_)    |/    
    \u001b[37;1m\ \ / /  / _ \  | | | |          | _ ) | __|  (_)_\(_) |_   _|          |_   _|  | || | | __|         (_)) __|  (_)_\(_) |  \/  | | __|  (      
     \ V /  | (_) | | |_| |          | _ \ | _|    / _ \     | |              | |    | __ | | _|            | (_ |   / _ \   | |\/| | | _|   )\     
      |_|    \___/   \___/           |___/ |___|  /_/ \_\    |_|              |_|    |_||_| |___|            \___|  /_/ \_\  |_|  |_| |___| ((_)    
                                                                                                                                                    
    \u001b[0m""")

def fifty_art():
    time.sleep(2)
    print(u"""

                        \u001b[34;1m.((((((((((((((((((((((((((((((.                     
                  ((((((((((\u001b[37;1m%@@@@@@@@@@@@@@@@@@@@%\u001b[34m((((((((((                
              (((((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%\u001b[34m(((((((            
          .(((((\u001b[37;1m#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[34m((((((         
        (((((\u001b[37;1m&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#\u001b[34m(((((      
      (((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[34m(((((    
    *((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[34m((((   
    ((((\u001b[37;1m&@@@@#        @@@@     %@@@@@@@@@@@@@@@        @@@@      @@@@@@#\u001b[34m(((. 
  *(((\u001b[37;1m@@@@@@@  @@@@@@@@@*  @@@&  @@@@@  .@@@@@@  @@@@@@@@@  @@@@  #@@@@@#\u001b[34m((( 
  (((\u001b[37;1m#@@@@@@  @@&@@@@@@   @@@@@  #@@@@@@@@@@@@  #@@@@@@@(( .@@@@  @@@@@@\u001b[34m((((
  /(((\u001b[37;1m@@@@@@#        @@@  @@@@@  @@@@@@@@@@@@@         @@  @@@@@  @@@@@@&\u001b[34m(((
  ((((\u001b[37;1m@@@@@@@@@@@@@  @@   @@@@  *@@@@@@@@@@@@@@@@@@@  /@,  @@@@@  @@@@@@@\u001b[34m(((
  (((\u001b[37;1m&@@@@@  @@@@@*  @@   &@@@  @@@@@   @@@@#  @@@@@  @@@  @@@@%  @@@@@@#\u001b[34m(((
  ((((\u001b[37;1m@@@@@@       .@@@@       @@@@@@@##@@@@@,       @@@@@       @@@@@@@\u001b[34m((((
    ((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[34m(((( 
    ((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%\u001b[34m((((  
      *((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[34m((((.   
        (((((\u001b[37;1m&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%\u001b[34m((((/     
          ,(((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%\u001b[34m(((((        
            /((((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&\u001b[34m((((((,          
                ((((((((\u001b[37;1m#@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[34m(((((((((              
                      ((((((((((((((((((((((((((((((((((((                   
  \u001b[0m""")

def audience_art():
    time.sleep(2)
    print(u"""

                        \u001b[34;1m,((((((((((((((((((((((((((((((,                     
                  (((((((((\u001b[37;1m#@@@@@@@@@@@@@@@@@@@@@@\u001b[34;1m((((((((((                
              ,(((((((  \u001b[37;1m @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@, \u001b[34;1m(((((((            
          ((((((,\u001b[37;1m @@@@@@  @@@@@@@@@@@@@&@@@@@@@@@@@@@  ,@@@@@*\u001b[34;1m(((((,        
        (((((\u001b[37;1m@@  @@@@@@@@  @@@@@@@@         @@@@@@@@  @@@@@@@@  @\u001b[34;1m(((((      
      ((((\u001b[37;1m#@@@@  @@@@@@@@  @@@@@@@  @@@@@@@  @@@@@@@  @@@@@@@@  @@@\u001b[34;1m(((((    
    /((((\u001b[37;1m@@@@@@@  @@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@   @@@@@@. ,@@@@@\u001b[34;1m((((,  
    ((((\u001b[37;1m@@@@@@@@@.      ,@@@@@@@@@  @@@@@@@  @@@@@@@@@,       @@@@@@@@&\u001b[34;1m(((( 
  ((((\u001b[37;1m@@@@@@@@   *@@@@@@#   %@@@@@@   @@@,  @@@@@@@/   &@@@@@/   @@@@@@@\u001b[34;1m(((/
  (((\u001b[37;1m%@@@@   ,@@@@@@@@@@@@@@*   @@           %@(   %@@@@@@@@@@@@@.   @@@\u001b[34;1m((((
  /(((\u001b[37;1m@@@&  @@@@@@@@@@@@@@@@@@.   @@@@@@@@@@@(   &@@@@@@@@@@@@@@@@@@  @@&\u001b[34;1m(((
  /(((\u001b[37;1m@@@, #@@@@@@@@@@@@@@@@( *@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@  @@&\u001b[34;1m(((
  (((\u001b[37;1m#@@@  @@@@@@@@@@@@@@@@@  &@@@@@@@@@@@@@@@@@@  %@@@@@@@@@@@@@@@@  @@\u001b[34;1m((((
  /(((\u001b[37;1m@@@  @@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@# ,@@@@@@@@@@@@@@@@  %&\u001b[34;1m(((,
    ((((\u001b[37;1m@  @@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@% *\u001b[34;1m(((, 
    *((((\u001b[37;1m .@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@\u001b[34;1m((((   
      (((((\u001b[37;1m                   @@@@@@@@@@@@@@@@@@@@                 \u001b[34;1m(((((    
        (((((\u001b[37;1m@@@@@@@@@@@@@@                         (@@@@@@@@@@@%\u001b[34;1m(((((      
          .(((((\u001b[37;1m#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[34;1m((((((         
              (((((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&\u001b[34;1m(((((((            
                  ((((((((((\u001b[37;1m%@@@@@@@@@@@@@@@@@@@@#\u001b[34;1m((((((((((                
                        .((((((((((((((((((((((((((((((  


  \u001b[0m""")

def phone_art():
    time.sleep(2)
    print(u"""

                        \u001b[34;1m.((((((((((((((((((((((((((((((.                     
                  ((((((((((\u001b[37;1m%@@@@@@@@@@@@@@@@@@@ @@@@@, *\u001b[34;1m(((                
              (((((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@  \u001b[34;1m(((((            
          .(((((\u001b[37;1m#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@.@@@  @@\u001b[34;1m((((((         
        (((((\u001b[37;1m&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.@@@.@@@@@/  &@@@@#\u001b[34;1m(((((      
      (((((\u001b[37;1m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@.@@@   @@@@@@@@\u001b[34;1m(((((    
    *((((*\u001b[37;1m  .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@.   @@@@@@@@@@\u001b[34;1m((((   
    ((((\u001b[37;1m&@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@( #      #@@@@@@@@@@@#\u001b[34;1m(((. 
  /(((\u001b[37;1m@@@@@  @(. .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@  @@@@@@@@@@@@@#\u001b[34;1m((( 
  (((\u001b[37;1m#@@@@#@@@@)  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@   @@@@@@@@@@@@@@@\u001b[34;1m((((
  /(((\u001b[37;1m@@@@@@@@@* *%/.  @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@   @@@@@@@@@@@@@@@@&\u001b[34;1m(((
  ((((\u001b[37;1m@@@@@@@@@@%@@@@  @@@@@@@@@@@@@@@@@@@@@@@ @@@@@@   &@@@@@@@@@@@@@@@@@\u001b[34;1m(((
  (((\u001b[37;1m&@@@@@@@@@@@@@@  @#.  @@@@@@@@@@@@@@@@@@ @@@@@@   @@@@@@@@@@@@@@@@@@#\u001b[34;1m(((
  ((((\u001b[37;1m@@@@@@@@@@@@@#&@@@  /@@@@@@@@@@@@@@@@@ @@@@@@   @@@@@@@@@@@@@@@@@@@\u001b[34;1m((((
    ((((\u001b[37;1m@@@@@@@@@@@@@@@@(  %*.  %@@@@@@@@@) @@@@@(   @@@@@@@@@@@@@@@@@@@\u001b[34;1m(((( 
    ((((\u001b[37;1m@@@@@@@@@@@@@@@@&@@@@)  @@@@ @@  @@@@@@@    @@@@@@@@@@@@@@@@@@%\u001b[34;1m((((  
      *((((\u001b[37;1m@@@@@@@@@@@@@@@@@@  &#* @@@@@@@  &@@   .@@@@@@@@@@@@@@@@@@\u001b[34;1m((((.   
        (((((\u001b[37;1m@@@@@@@@@@@@@@@@%%@ @@@@.@@@@@@     &@@@@@@@@@@@@@@@@%\u001b[34;1m((((/     
          ,(((((\u001b[37;1m@@@@@@@@@@@@@@@,@@@.@@.@@@@     @@@@@@@@@@@@@@@%\u001b[34;1m(((((        
            /((((((\u001b[37;1m@@@@@@@@@@@@@ @@@@@@@@     @@@@@@@@@@@@@&\u001b[34;1m((((((,          
                ((((((((\u001b[37;1m#@@@@@@@@ @@@@     ,@@@@@@@@@\u001b[34;1m(((((((((              
                      ((((((((((((((*     *\u001b[34;1m(((((((((((((((                   
                            ./((((((((((((((((((/ 


  \u001b[0m""")

#CONTROLS FUNCTIONS

# def main_controls():
    #time.sleep(2)
#     print("""
#      ___________________________________________________________________________
#     |                                                                           |
#     |          "Example string"                                                 |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |                                                                           |
#     |___________________________________________________________________________|
# """)

# potential_answers = [
#     "A",
#     "B",
#     "C",
#     "D"
# ]

# correct_answer1 = "C"
# correct_answer2 = "B"

# def fifty_fifty (correct_answer1, correct_answer2, potential_answers) :
            
#             if correct_answer2 != "":       #if we want this we put the correct answer in corect_answer2 
#                 print(f"The two remaining correct answers are...{correct_answer2} and {correct_answer1}")
#             else:                           # otherwise leave the correct_answer2 as an EMPTY STRING
#                 potential_answers.remove(correct_answer1)
#             # potential_answers.remove(random.randint(0,len(potential_answers)))
#                 fifty_answer = potential_answers[random.randint(0,len(potential_answers)-1)] 
#                 print(f"The two remaining correct answers are...{fifty_answer} and {correct_answer1}")
#                 print(len(potential_answers))

# def phone_a_friend2():
#     print("\"OK! Let's phone a better friend.\"")
#     time.sleep(2)
#     global friend_name
#     friend_name = input("\"So who will it be?\"" )
#     if friend_name == "Jay":
#         time.sleep(2)
#         print("\" Ok. Be that way then. I told you that we would NOT be ringing Jay. Really, it's the best thing for you. You ignored me, so you're on your own. You're not ringing anyone.\"")
#         # return to question 
#     else:
#         print(f"\"You've decided to ring {friend_name}, let's hope they pick up! Remember, you don't need to accept their answer.\"")
#         time.sleep(3)
#         print("The phone rings.")
#         time.sleep(3)
#         print("It rings again")
#         time.sleep(3)
#         print(f"Suddenly, the voice of {friend_name} fills the studio.")
#         time.sleep(2)
#         print("\"Hello?\"")
#         time.sleep(2)
#         print(f"\"Hello {friend_name}! It's Chris Tarrant here, you're on Who Wants To Be A Millionaire! Your friend {player_name} needs your help. You only have 30 seconds. {player_name}, take it away!\"")
#         time.sleep(2)
#         # function to repeat actual question? or just:
#         print("You repeat the question as fast as you can.")
#         time.sleep(3)
#         print(f"\" Hm, so I think my gut feeling is taking me to C. But thinking about it, it might actually be A. Although I guess depending on how you wanted to go about it, you could make a case for D. Actually, I feel pretty good about B. I'd go for B. Or should I trust my gut and go for C? And I do definitely think there's a chance it might be A. You also definitely can't discount D. I think honestly {player_name}, I'm not that sure.\"")
#         # break up a bit?
#         time.sleep(3)
#         print("....")
#         time.sleep(3)
#         print(f"\"And you're all out of time! Thanks a lot {friend_name}, you've been great.\"")
#         time.sleep(2)
#         print(f"\"So, after that great help from {friend_name}, let's hear the question again and get your final answer.\"")
#         # return to question function?
# def phone_a_friend():
#     print("\"OK! You have decided to phone a friend. Think carefully about you want to ring, you only get one shot.\"")
#     time.sleep(2)
#     global friend_name
#     friend_name = input("\"So who do you want to ring?\"")
#     if friend_name == "Jay":
#         print("\" Jay?! Like, Jay from CodeNation Jay?! Why on earth would you want to ring him? I can't see him being any help at all really.\"")
#         time.sleep(2)
#         print("You can't ring Jay. That's me, Chris Tarrant making an executive decision. Let's phone someone else.")
#         phone_a_friend2()
#     else: 
#             print(f"\"You've decided to ring {friend_name}, let's hope they pick up! Remember, you don't need to accept their answer.\"")
#             time.sleep(3)
#             print("The phone rings.")
#             time.sleep(3)
#             print("It rings again")
#             time.sleep(3)
#             print(f"Suddenly, the voice of {friend_name} fills the studio.")
#             time.sleep(2)
#             print("\"Hello?\"")
#             time.sleep(2)
#             print(f"\"Hello {friend_name}! It's Chris Tarrant here, you're on Who Wants To Be A Millionaire! Your friend {player_name} needs your help. You only have 30 seconds. {player_name}, take it away!\"")
#             time.sleep(2)
#             print("You repeat the question as fast as you can.")
#             time.sleep(3)
#             print(f"\" Hm, so I think my gut feeling is taking me to C. But thinking about it, it might actually be A. Although I guess depending on how you wanted to go about it, you could make a case for D. Actually, I feel pretty good about B. I'd go for B. Or should I trust my gut and go for C? And I do definitely think there's a chance it might be A. You also definitely can't discount D. I think honestly {player_name}, I'm not that sure.\"")
#             # break up a bit?
#             time.sleep(3)
#             print("....")
#             time.sleep(3)
#             print(f"\"And you're all out of time! Thanks a lot {friend_name}, you've been great.")
#             time.sleep(2)
#             print(f"\"So, after that great help from {friend_name}, let's hear the question again and get your final answer.\"")
#             # return to question function?


# answers = [
#     ["A"],
#     ["B"],
#     ["C"],
#     ["D"]
# ]

# correct_answer1 = "D"
# potential_answer1 = "A"
# potential_answer2 = "B"
# potential_answer3 = ""
# correct_answer2 = "C"

# def ask_the_audience(potential_answer1, potential_answer2, potential_answer3, correct_answer1, correct_answer2):
#     potential_audience1 = random.randint(5,20)
#     potential_audience2 = random.randint(5,20)
#     correct_audience1 = random.randint(25,50)
#     correct_audience2 = 100 - potential_audience1 - potential_audience2 - correct_audience1 #NOTE d in this case would be the correct answer
#     # print(audience_a, audience_b, audience_c, audience_d)
#     if correct_answer2 != "":
#         if "A" == potential_answer1:    
#             print(f'{potential_answer1}: {potential_audience1}%')
#         elif "A" == potential_answer2:
#             print(f'{potential_answer2}: {potential_audience2}%')   
#         elif "A" == correct_answer1:
#             print(f'{correct_answer1}: {correct_audience1}%')
#         elif "A" == correct_answer2:
#             print(f'{correct_answer2}: {correct_audience2}%')
#         if "B" == potential_answer1:  
#             print(f'{potential_answer1}: {potential_audience1}%')
#         elif "B" == potential_answer2:
#             print(f'{potential_answer2}: {potential_audience2}%')   
#         elif "B" == correct_answer1:
#             print(f'{correct_answer1}: {correct_audience1}%')
#         elif "B" == correct_answer2:
#             print(f'{correct_answer2}: {correct_audience2}%')
#         if "C" == potential_answer1:  
#             print(f'{potential_answer1}: {potential_audience1}%')
#         elif "C" == potential_answer2:
#             print(f'{potential_answer2}: {potential_audience2}%')   
#         elif "C" == correct_answer1:
#             print(f'{correct_answer1}: {correct_audience1}%')
#         elif "C" == correct_answer2:
#             print(f'{correct_answer2}: {correct_audience2}%')
#         if "D" == potential_answer1:  
#             print(f'{potential_answer1}: {potential_audience1}%')
#         elif "D" == potential_answer2:
#             print(f'{potential_answer2}: {potential_audience2}%')   
#         elif "D" == correct_answer1:
#             print(f'{correct_answer1}: {correct_audience1}%')
#         elif "D" == correct_answer2:
#             print(f'{correct_answer2}: {correct_audience2}%')
#     else:     
#         if "A" == potential_answer1:    
#             print(f'{potential_answer1}: {potential_audience1}%')
#         elif "A" == potential_answer2:
#             print(f'{potential_answer2}: {potential_audience2}%')   
#         elif "A" == correct_answer1:
#             print(f'{correct_answer1}: {correct_audience1}%')
#         elif "A" == potential_answer3:
#             print(f'{potential_answer3}: {correct_audience2}%')
#         if "B" == potential_answer1:  
#             print(f'{potential_answer1}: {potential_audience1}%')
#         elif "B" == potential_answer2:
#             print(f'{potential_answer2}: {potential_audience2}%')   
#         elif "B" == correct_answer1:
#             print(f'{correct_answer1}: {correct_audience1}%')
#         elif "B" == potential_answer3:
#             print(f'{potential_answer3}: {correct_audience2}%')
#         if "C" == potential_answer1:  
#             print(f'{potential_answer1}: {potential_audience1}%')
#         elif "C" == potential_answer2:
#             print(f'{potential_answer2}: {potential_audience2}%')   
#         elif "C" == correct_answer1:
#             print(f'{correct_answer1}: {correct_audience1}%')
#         elif "C" == potential_answer3:
#             print(f'{potential_answer3}: {correct_audience2}%')
#         if "D" == potential_answer1:  
#             print(f'{potential_answer1}: {potential_audience1}%')
#         elif "D" == potential_answer2:
#             print(f'{potential_answer2}: {potential_audience2}%')   
#         elif "D" == correct_answer1:
#             print(f'{correct_answer1}: {correct_audience1}%')
#         elif "D" == potential_answer3:
#             print(f'{potential_answer3}: {correct_audience2}%')



# def lifeline():
#     if answer == "L":
#         console_slow_type("""Enter "F" for Fifty / Fifty - This will remove two incorrect answers and leave two remaining right answers. \n 
#     Enter "P" for Phone a Friend - This will give you the option of calling upon your designated expert.
#     Whether they're smart or not is your stupid fault. Isn't it. \n
#     Enter "Z" for Ask the Audience - this will put the question to our room full of Brainiacs.    
#     """)
#     choice = input("Choose a lifeline")
#     if choice == "F":
#         fifty_fifty(correct_answer1, correct_answer2, potential_answers)
#     elif choice == "P":
#         phone_a_friend()
#     elif choice == "Z":
#         ask_the_audience()


def console_slow_type(string_slow):         #NOTE: SK: removed the pip and keyboard imports to make it make sense on any terminal.  
    type_duration = 0.03
    for question_index in string_slow: #goes through the string 
        print(question_index, end='')
        sys.stdout.flush()
        time.sleep(type_duration)



#CORRECT OUTCOMES FUNCTIONS

# def questions_four_correct_a():
# Q4 CORRECT (A) bottle to the head 
# print("""TEXT""")

# def questions_four_correct_b():
# Q4 CORRECT (B) dinosaur 
# print("""TEXT""")

# def questions_seven_correct_b():
# Q7 CORRECT (B) rick and morty
# print("""TEXT""")

# def questions_seven_correct_c():
# Q7 CORRECT (C) radioactivity
# print("""TEXT""")

# def questions_nine_correct_b():
# Q9 CORRECT (B) pokemon
# print("""TEXT""")

# def questions_nine_correct_d():
# Q9 CORRECT (D) paranoia
# print("""TEXT""")

# def questions_ten_correct_a():
# Q10 CORRECT (A) love island
# print("""TEXT""")

# def questions_ten_correct_c():
# Q10 CORRECT (C)	 drug cartel w/jay
# print("""TEXT""")



#INCORRECT OUTCOMES FUNCTIONS

def ready_or_not():
    console_slow_type("""The show runner, obviously unused to such a response remains glazed, save for a twitch in their right eye.
    "OK. Do you need anything? Water? Meat? Anything like that? Red Bull? Brain food, you know?"
    You can see the panic in their eyes as they search yours like a supermarket barcode scanner, so you reply...
    "No... I'm alright for... brain food and red bull.""")
    ready_annoyed1 = input("\n    So you're ready?  [Y/N]  ")
    if ready_annoyed1 == "N":
        console_slow_type("""
        "You don't want to go on? It's just the nerves, you'll be great! You might come out of this."
        That last comment threw you a bit; you look puzzled. To the show runner read; worse."
        "A Millionaire! You might come out of this a millionaire is what I mean and what I said actually."
        You are fairly sure they did not say that the first time, but these TV folk, hey, odd bunch - lots of terminology, who knows."
        Another TV person has come over. You can tell by the clipboard and the headset. And the stench of vacuousness."
        "What's the hold up. He's ready. You're ready aren't you buddy!"
        New TV plonker gives you a thump in the arm.""")
    else:
        story_start_game(question_index, f"Hello and welcome to Who Wantz to be a Millionaire! Today we have {player_name} with us, an aspiring developer, hoping to win big! Let's begin with an easy one! ", chances)
    ready_annoyed2 = input("\n  You MUST be ready...? [Y/N]  ")
    if ready_annoyed2 == "N":
        console_slow_type("""
        The first, and more lowly of this crew hangs their head and closes their eyes.
        The second, newer, and more frightening of the two moves in close to you.
        "You are ready" TV plod no.2 says "You know how I know?"
        "No, how?" you say.
        "Look up there at that sign." He point high up to your left, and as you follow his finger with your eyes, his clipboard comes striking down out of the dark rendering you unconscious.
        "Bloood...bloody hell"" you stammer out as your eyes open and you realise you are slumped on a stool, schlocked and blinded by incredibly bright lights.
        """)

def green_room_wrong ():
    console_slow_type("""
    "I'm so sorry that was the..." you wait for Chris to pull his signature switcheroo."
    "WRONG answer!"
    What!?""")
    time.sleep(2)
    console_slow_type("""
    But, b-b-but he never does that, he always does the switcheroo, the bloody Tarrant switcheroo." 
    "Stop saying the word switcheroo, you think. It isn't helping."
    "Some producers rush over. You look to Chris but he apparently is no longer engaging with you and is staring out into the audience, whilst chewing three of his fingers"
    ""Look."" Some producer has swivelled you round on your swivel stool. It swivels, that is new.
    "Come with us back to the green room, freshen up, look alive and let's give it another run yeah?"
    But the cameras!? The, the viewers at home!" At this, one of the gaggle of TV folk chuckle.
    
    """)
    time.sleep(2)
    console_slow_type("""
    
    You are a bit unsure of the whole set up but decide they probably know what's what.
    "Not live. Come on, shit-for-brains."
    And so you follow the rather charming television producer back to the green room
    After a can of 7-up (that feels pretty heavy on the 7-up) and a swift muller corner, a show runner comes to get you and drags you back to the tunnel.
    This bloody tunnel, you think. It's like a maze.

    """)
    time.sleep(2)
    response = input("Are you ready to start again? [Y/N]   ")
    if response == "Y" or response == "y" or response == "yes" or response == "Yes":
        console_slow_type("""Great! Come with me then.""")
        time.sleep(2)
        console_slow_type("""You follow the show runner back to the stool. """)
        player_name = input('What was your name again?     ').capitalize()
        story_start_game(question_index, f"\nGreat! So, {player_name}, let's begin!", chances)
    elif response == "N" or response == "n" or response =="no":
        console_slow_type(""""Oh for faaaa..." The show runny looks away in disgust. "You want to go down this road?""")
        time.sleep(2)
        
        
    player_name = input("\n'What is your name?'   ").capitalize()
    print(f"'Hello {player_name}, hope you are ready this time.'")
    story_start_game(question_index, f"\nSo, {player_name} let's begin!", chances)

def chris_sanity_decline(chances):

    chances -= 1
    if (chances == 3):
        
        console_slow_type("""\n\t\t\tChris looks at you much in the same way a child looks at an anthill.
                        You nervously await the response.
                        "That's ok, it can get quite nervy here in the studio with so much, so, so much at stake."
                        He grins and looks towards the cameras.
                        From behind you someone in the audience groan "Steeeeaaaaakk!"
                        Chris asks some clipboard wielding producers "Are we OK to go again or is this one...?" 
                        He drags his indequestion_index finger across his throat. \n
                        The producer waves their hand around to indicate Chris to ask again."OK!" So... \n""")
    elif (chances == 2):

        console_slow_type("""\n\t\t\tBAM! Chris has thumped his terminal. 
                        "For pitys sake. Look what you've made me do. Haha, Sorry everyone, lights are very hot in here today." 
                        You peer over and see that Chris has hit the facade of his screen, equestion_indexposing every so slightly, what he had on his screen. 
                        It doesn't look like start_game, like the start_game on your screen. It looked bodies. Porn?
                        "Look at me." 
                        Chris' voice commands your gaze.
                        "You have four buttons on your side there. A, B, C and fucking D."
                        "Do you know how many times I've done this show?"                                  
                        You shake your head.
                        "Too many."
                        "Do you know how many times someone has CORRECTLY chosen an answer that wasn/'t one of the multiple choice start_game?"
                        You answer the man honestly. "Is it zero."
                        Chris looks at you with pure bile.
                        "Is that your final answer? Becuase it better be, or I will make it the final question you ever answer."
                        Something in voice tells you this pompous clown may actually mean it. He definitely means it. 
                        "I'll ask again. One more time. For the cheap seats....""")


    else:

        console_slow_type("""The crowd cheered for you, but it turns out your were just as wrong and dead as they were! \n
        
        \n""")
        sys.exit(0)

    return chances

def die_become_z():
    console_slow_type(""" 
    "Chris sucks air in through his unnaturally pearly teeth.
    "The audience are baying for blood."
    "You look deep into Tarrants eyes and see... joy?
    "You said --letter--- that is the... WRONG answer!!""
    "His face lights up."
    "From behind you, you hear the sharp creak of metal unhinging, and a viscious crackling as the bars holding the now frenzied mob come down."
    "Your locked gaze starts to rise, following Chris's eyes up as his stool begins to rise, raising him up and up into the studio rafters where he immediately met by more show runners who shroud him in robes and drinks."
    ""BLLEEEUAGHHH!!!!""
    "You look back down, house lights up, and to your horror, as they begin to approach you, you see the audience are in fact..."
    "THE UNDEAD."
    ""Oh fuck.""
    "You glance around - all exits full of the snarling and braying undead." 
    ""Oh fuuuuuckkkk!""
    "Limbless corpses surround you. There is no escape." 
    ""Chris! Chris, help, help me please for fuck's sake!" you yell!"
    You look up and see Chris has a vantage point over the entire proceedings. He has a cigar on the go. 
    "Wanker.
    "As they hoard begin to supplant every inch of space around you, you aim the entirety of your lifes anger skyward and scream.
    ""Chris Tarrant You WANKERRRRRRR!"
    "You died. But..."
    "As though time at has passed you begin to grunt and bleeeuugh."
    "A tazer wielding show runner approaches you."
    "You grunt more heartily now you see their pulsing, delicious neck. God, you're hungry did you not have a snack in the Green Room?"
    ""STICK HIM WITH THE OTHERS THEN", you hear pumped out over the tannoy."
    ""Grubnt, Blueghs, GRUNTHY GRUNCH." you say."
    "You didn't mean to say that, but that's what came out. what's happening? All you can think about is lashing out and biting at the show runner who is herding you into the audience cage."
    "BLAH!" You think to yourself. "Blat must be it. I'm a zombie.""
    "And you'd be right. You are the recently reanimated corpse of your former self."
    "But look on the bright side, you dumbly think as you watch a fresh faced new contestent be ushered onto the stool ahead of you..."
    "They look tasty."
        
    """)

# def questions_four_incorrect():
# Q4 INCORRECT (C/D) dead by chris sacrifice 
# print("""TEXT""")

# def questions_seven_incorrect_a():
# Q7 INCORRECT (A) trump mob
# print("""TEXT""")

# def questions_seven_incorrect_d():
# Q7 INCORRECT (D) necromancy
# print("""TEXT""")

# def questions_nine_incorrect_a():
# Q9 INCORRECT (A) bag of jays
# print("""TEXT""")

# def questions_nine_incorrect_c():
# Q9 INCORRECT (C) terry crews
# print("""TEXT""")

# def questions_ten_incorrect_b():
# Q10 INCORRECT (B) ad break
# print("""TEXT""")

# def questions_ten_incorrect_d():
# Q10 INCORRECT (D)	 python error curse
# print("""TEXT""")



#PLAYTHROUGH FUNCTIONS

def story_start_game(question_index, opening_string, chances):
    question_list = questions_and_answers[question_index] #gets 1S list from out list of lists
    question = question_list[0] #gets the question from the list
    console_slow_type(opening_string + ", " + question) #we print the name and question to the terminal
    correct_answer1 = question_list[-1]  #gets the last item from the list which is the correct answer always
    correct_answer2 = question_list[-2] 
    console_slow_type(f'{question_list[1]}, {question_list[2]}, {question_list[3]}, or {question_list[4]}') #prints options 
    answer = input('\nWhich one do you pick?   A, B, C, or D?  ').capitalize() #gets input 
    if (answer == correct_answer1):
        question_index += 1 
        print("'Is that your final answer?' You nod. 'Ok, let's see if it is the right answer...And it is! Congratulations! Let's move onto the next round.'") #NOTE: SK: This also prints for storyline questions - possible fix is to make text generic enough to fit all correct answer outcomes
        if (question_index == 4): #NOTE: SK: changed the ==numbers to the corresponding storyline questions as it was infact reading from 1 not from 0!! LOL
            time.sleep(2)
            print("Q4 CORRECT ANSWER_1 OUTCOME")
            time.sleep(2)
            story_start_game(question_index, "You got through Q4, Next...", chances)
        elif (question_index == 7):
            #story_start_game2()
            time.sleep(2)
            print("Q7 CORRECT ANSWER_1 OUTCOME")
            time.sleep(2)
            story_start_game(question_index, "You got through Q7, Next...", chances)
        elif (question_index == 9):
            #story_question3()
            time.sleep(2)
            print("Q9 CORRECT ANSWER_1 OUTCOME")
            time.sleep(2)
            story_start_game(question_index, "You got through Q9, Next...", chances)
        elif (question_index == 10):
            #story_question4()
            time.sleep(3)
            print("Q10 CORRECT ANSWER_1 OUTCOME")
            game_winner_art()
            sys.exit(0)
        else:
            story_start_game(question_index, "Next...", chances) #asks the question again #NOTE: SK: need to make text more FUN 
    elif (answer == correct_answer2):
        question_index += 1 
        print(f"Congratulations {player_name}, that was correct!", "PLOT SCENARIO") #NOTE: SK: This also prints for storyline questions - possible fix is to make text generic enough to fit all correct answer outcomes
        if (question_index == 4): #NOTE: SK: changed the ==numbers to the corresponding storyline questions as it was infact reading from 1 not from 0!! LOL
            #story line question occur on question 4, 7, 9, 10
            time.sleep(2)
            print("Q4 CORRECT ANSWER_2 OUTCOME")
            time.sleep(2)
            story_start_game(question_index, "You got through Q4, Next...", chances)
        elif (question_index == 7):
            #story_start_game2()
            time.sleep(2)
            print("Q7 CORRECT ANSWER_2 OUTCOME")
            time.sleep(2)
            story_start_game(question_index, "You got through Q7, Next...", chances)
        elif (question_index == 9):
            #story_question3()
            time.sleep(2)
            print("Q9 CORRECT ANSWER_2 OUTCOME")
            time.sleep(2)
            story_start_game(question_index, "You got through Q9, Next...", chances)
        elif (question_index == 10):
            #story_question4()
            time.sleep(3)
            print("Q10 CORRECT ANSWER_2 OUTCOME")
            time.sleep(2)
            game_winner_art()
            sys.exit(0)
        else:
            story_start_game(question_index, "Next...", chances) #asks the question again #NOTE: SK: need to make text more FUN 
    elif (answer == "Q"): #checks if player presses q 
        
        quit_check = input("\n You have pressed Q and choosen to equestion_indexit the game, are you sure you want to quit? (Y/N)   ").capitalize() #checks if the plays wants to quit
        if  (quit_check == "Y"): 
            console_slow_type("\n See ya loser!", 0.02) 
            game_over()
            sys.exit(0) #quits program
        else:
            story_start_game(question_index, f"\nHello and welcome to Who Wantz to be a Millionaire! Today we have {player_name} with us, an aspiring developer, hoping to win big! Let's continue with the question.", chances)
    elif (answer != "A" and answer != "B" and answer != "C" and answer != "D" and answer != "Q" and answer != "P" and answer != "F" and answer != "H" and answer != "J"): #if an unprotected value is entered 
        chances = chris_sanity_decline(chances) #calls function to take away a chance and print to terminal
    
    elif (answer != correct_answer1) and (question_index <= 3): #if the wrong answer is given
        green_room_wrong()
    
    elif (answer != correct_answer1) and ((question_index == 5) or (question_index == 6) or (question_index == 8)):
        print("Zombie outcome")
        die_become_z()
        time.sleep(2)
        game_over()
        sys.exit(0)
        #NOTE: SK: As there are different wrong outcomes for every storyline Q, I think we need a load of ifelse statements for what happens then. 


def intro():                #NOTE: SK: incoporated the dialogue into the intro function, as well as the ascii art for the game title, I didn't think it needed a function. 
    global player_name
    time.sleep(2)
    print(u"""\n\t\t\t \u001b[33m
                    
                                )    )                        )           )              )                              \u001b[37;1m*    \u001b[33m(   (    (    \u001b[37;1m(      \u001b[33m )   \u001b[37;1m  )        \u001b[33m(\u001b[0m   (        
                    (  \u001b[33;1m(     \u001b[37;1m( /\u001b[33m( ( /(     \u001b[37;1m(  (      \u001b[33m(     ( /\u001b[37;1m(  *   \u001b[33;1m) ( /(     \u001b[37;1m*   ) ( \u001b[33;1m/(       (           (        (  \u001b[37;1m`   )\u001b[33;1m\ ))\ \u001b[37;1m) )\ ) \u001b[33;1m)\ \u001b[37;1m) ( /(  (\u001b[33;1m /(  \u001b[37;1m(     \u001b[33;1m)\ ))\ )     
                    )\)\u001b[37;1m)(   \u001b[33;1m'\u001b[37;1m\()))\u001b[33;1m\())    )\))(   \u001b[37;1m' \u001b[33;1m)\    )\()` )  /( )\())  \u001b[37;1m` \u001b[33;1m)  /( )\())    ( )\ (        )\       )\))( (()/((\u001b[37;1m)/((()/((()/\u001b[33;1m( )\()) )\()) )\   (()/(\u001b[37;1m()\u001b[33;1m/((    
                    ((_)()\ )\u001b[37;1m((_)\(\u001b[33;1m(_)\    ((_)()\ ((((_)( ((\u001b[37;1m_)\ (\u001b[33;1m) )\u001b[37;1m(_\u001b[33;1m)((_)\    ( )(_)((_\u001b[37;1m)\     \u001b[33;1m)((_))\    ((((_)(    ((_)(\u001b[37;1m)\ /\u001b[33;1m(_)/\u001b[37;1m(\u001b[33;1m_))/(_))/(_)((_)\ \u001b[37;1m((_)(\u001b[33;1m(((_)(  /(_)/(_))\   
                    _(())\_)()_((_) ((_)   _(())\_)()\ _ )\ _((_(_(_()) _((_)  (_(_())  ((_)   ((_)_((_)    )\ _ )\   (_()((_(_))(_)) (_)) (_))   ((_) _((_)\ _ )\(_))(_))((_)  
                    \u001b[31;1m\ \((_)/ | || |/ _ \   \ \((_)/ (_)_\(_| \| |_   _||_  /   |_   _| / _ \    | _ | __|   (_)_\(_)  |  \/  |_ _| |  | |  |_ _| / _ \| \| (_)_\(_|_ _| _ | __| 
                     \ \/\/ /| __ | (_) |   \ \/\/ / / _ \ | .` | | |   / /      | |  | (_) |   | _ | _|     / _ \    | |\/| || || |__| |__ | | | (_) | .` |/ _ \  | ||   | _|  
                      \_/\_/ |_||_|\___/     \_/\_/ /_/ \_\|_|\_| |_|  /___|     |_|   \___/    |___|___|   /_/ \_\   |_|  |_|___|____|____|___| \___/|_|\_/_/ \_\|___|_|_|___|\u001b[0m
                    
                    \n""")
    time.sleep(2)
    console_slow_type("A dark tunnel. cold. dark, very dark.")
    console_slow_type("Someone touches your hand, you recoil, fear and sweat running out of you in equal measure.")
    console_slow_type("\n'HEY!'")
    player_name = input("'Hey you. What's your name?'   ")
    console_slow_type(f"""\n'Hi {player_name}!'
        'Sorry - its a little crazy here these days'""")
    console_slow_type("""
        "'Are you ready?'    """)
    time.sleep(1)
    ready1 = input("[Y/N]   ") 
    if (ready1 == "Y"):
        console_slow_type("""'Great follow me'...
        The stranger take your hand and leads you through the dark, turning left, then right, you hear the oncoming throng of.... something. 
        Then suddenly, the stranger turns you right and...""")
        console_slow_type(f"""Dazzling lights, blind you. From all directions cheers and yell - \n You glance around you trying to take it all in, but before you can make sense of it all...
        \n'PLEASE WELCOME - {player_name}!!!'""")
        console_slow_type("""\nA man in his 50's, white hair, smug grin is sat at a stool that simultaneously looks too tall and too small for him.
        Music swells around you - lasers, greeen and red swing around the room causing hush amongst what you now see is .. an audience!""")
        console_slow_type("""
        You look back to the man in the chair. You're nerves subside. It's millionaire. You fucking got this.
        The man in the chair becons you forward.""")
    if ready1 == "N":
        console_slow_type("Err...")
        ready_or_not()
    elif ready1 != "Y" and ready1 != "N":
        console_slow_type("""'God, can't you make a decision!?' One of the producers mutters...\n Type again    """)
        time.sleep(2)
    beckon_forward = input ("\nGo? [Y/N]  ")
    if beckon_forward == "N":
        console_slow_type("The producer shunts you in the back cascading you forward towards the centre of the room.")
    elif beckon_forward != "Y":
        console_slow_type("""'God, can't you make a decision!?' One of the producers mutters...\n Type again""")
    elif beckon_forward == "Y":
        console_slow_type(f"""
        You move closer to the empty chair opposite to man and see now, the man is none other than ITV's Chris Tarrant
        'H-Hi Chris." You manage to stammer out.'""")
        time.sleep(1)
        console_slow_type(f"""
        'Hello! Let's give {player_name} a warm welcome everyone!'
        You glance around the audience. they are stony quiet. The occasional Groan escapes one of them. A few are wearing MAGA hats. 
        Did I do something wrong?""")
        time.sleep(1)
        console_slow_type("""
        'A Warm welcome I said!'
        At Chris's commmand, they begin to holler and shout.""")
        time.sleep(1)
        console_slow_type("""
        Out of the corner of your eye you notice one of the runners throw something into the crowd.""")
        time.sleep(1)
        console_slow_type(f"""
        You look to where it landed and see the audience clamber for it. Is that...
        'SO!'
        Your eyes wheel back to Chris...
        '{player_name}, I undertsand you're a, wow, you're a python developer, is that right?!'""")
        job_desc = input("\nis that right? [Y/N]  ")
        if job_desc == "N":
            console_slow_type("""
        'Oh, sorry! Why don't we just crack on with the start_game, and you can fill me in as we go. Lots iof contestants to get through today.'
        \n...get through?
        \n'Err sure, no worries Chris. Thank you.'""")
        else:
            console_slow_type("""
        'Wow. So what's that, like, 8 hours a day in the reptile enclosure!' 
        Chris' shit eating grin shines bright, even under the hot lights of the studio.
        Groans and moans from the audience.""")
            time.sleep(1)
            console_slow_type("""
        'HA. haha, no it's um - rather, I'm actually um, a software, well, dev-'
        'I KNOW.' Tarrant buts in abruptly. Then through a gritted smile he says...""")
            time.sleep(1)
            console_slow_type(""" 
        'play nicely now mate, let's not let things get out of hand...' he leans in 'for both of our sakes.'""")
            time.sleep(2)
            console_slow_type("\nMillionaire music and lasers swirl through the air, giving the previous moment no time to gain any footing your mind.")


questions_and_answers = [
    ['\nQuestion 1: How many players should a team have on the pitch at the start of a football game? ', 'A: 10', 'B: 5', 'C: 11','D: 15', 'C'],
    ['\nQuestion 2: Which Williams sister has won more Grand Slam titles? ', 'A: Serena', 'B: Venus','C: Jessica','D: Janice', 'A'],
    ['\nQuestion 3: Which racer holds the record for the most Grand Priquestion_index wins? ','A: Lewis Hamilton', 'B: Michael Schumacher', 'C: Daniel Ricciardo','D: Kimi Raikkonen', 'B' ],
    ['\nQuestion 4: Which language is considered romantic by the United Nations? ','A: Spanish','B: French', 'C: Russian', 'D: Chinese', 'A','B'],
    ['\nQuestion 5: What part of the atom has no electric charge? ', 'A: Proton','B: Electron','C: Neutron','D: Megatron','C'],
    ['\nQuestion 6: What is meteorology the study of? ','A: The Weather', 'B: Meteors', 'C: Astroturf','D: Dinosaurs','A'],
    ['\nQuestion 7: Which IMDB Top 250 film has the highest rating to date of 9.2/10? ','A: Inside Out','B: The Godfather','C: The Shawshank Redemption','D: Up','B','C'],
    ['\nQuestion 8: Which natural disaster is measured with a Richter scale? ','A: Tsunamis','B: Earthquakes','C: Hurricanes','D: Tornados','B'],
    ['\nQuestion 9: What is an evolution form of the creature Geodude from the popular cartoon, Pokémon? ','A: Gurdurr', 'B: Graveler','C: Golett','D: Golem','B','D'],
    ['\nQuestion 10: Which musical artist has achieved the all-time record of 5 Billboard #1 singles from one album? ', 'A: Michael Jackson', 'B: Rod Stewart', 'C: Katy Perry','D: Prince', 'A','C']
]




#GLOBAL VARIABLES
x = 0
question_index = 0 
chances = 3

#FUNCTION CALLS - GAME PLAYTHROUGH
intro()
time.sleep(2)
story_start_game(question_index, f"\nSo, {player_name}, excited? Let's start you with an easy one!", chances)