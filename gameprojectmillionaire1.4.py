# -*- coding: utf-8 -*-
#IMPORTS        
import time
import random
import sys
# import os
# import subprocess

#FUNCTIONS      

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

def game_controls():
    print(u"""
    \u001b[37;1mGAME CONTROLS:

    Enter \u001b[34;1mY \u001b[37;1mor \u001b[34;1mN \u001b[37;1mwhen prompted. 
    Enter \u001b[34;1mA\u001b[37;1m, \u001b[34;1mB\u001b[37;1m, \u001b[34;1mC\u001b[37;1m, or \u001b[34;1mD \u001b[37;1mwhen answering the questions.
    Enter \u001b[34;1mL \u001b[37;1minstead of answer to use a lifeline. 
    Enter \u001b[34;1mQ \u001b[37;1minstead of answer to quit game. 
    \u001b[0m""")


def console_slow_type(string_slow):
    type_duration = 0.03
    for question_index in string_slow: #goes through the string 
        print(question_index, end='')
        sys.stdout.flush()
        time.sleep(type_duration)



#CORRECT OUTCOMES FUNCTIONS

def questions_four_correct_1():
    console_slow_type("""
    A pregnant pause.
    Chris is so full of pregnant pauses he could repopulate the Earth.""")
    time.sleep(1)
    console_slow_type("""
    'Is.... The right answer!!!' He bellows.
    You're bloody happy about that! Way to go! 
    You do a little fist pump that is horrifically untethered from the sensibility of the British public and will no doubt be cut in the edit.""")
    time.sleep(2)
    console_slow_type("""
    PANG!!!
    Ow! what was that?! You feel woozy, look down and see someone has thrown a... glass bottle at your head!
    You feel the warm trickle of blood creep down your brow.
    Christ! Someone threw a....""")
    time.sleep(2)
    console_slow_type("""As you gaze back up to the Tarrant, you see he is simply shaking his head.
    You look around you, expectant that someone will rush to you aid.
    But no. The entire crew. The producers. Even the audience.
    Are shaking their heads.""")
    time.sleep(2)
    console_slow_type("""'First Warning. Last Warning.' says Chris.
    'S-s-sorry.' you utter across to your superior. Then like a popped water balloon, "S-sorry everyone", you gush to the entire studio.""")
    time.sleep(1)
    console_slow_type("""
    You wipe the blood from your eye, and see two producers holding bottles, one metal, one glass above their heads manacingly."
    'Got it.' You're on the same page now. No american showboating.""")
    time.sleep(1)
    console_slow_type("""
    Stoic and mild shy bitterness. That's the way.
    British television has existed on atop these pilllars for over 6 decades. Old bulldog, new trick and all that.""")
    time.sleep(1)
    console_slow_type("""
    "Right! Next one is more difficult, let's see how you get on."" says Chris.\n
    As he's setting up the next question you see a show runner wheel on what looks to be a giant trolley.\n
    The trolley is covered by a white sheet, and is stained - being currently stained by looks an incredible amount like blood.""")
    time.sleep(1)
    console_slow_type("""But before you have time to eye it up any further you are snapped back to the matter at hand...\n
    "OK! So, onto the next one, then. Doing rather well aren't you. Do you feel good Do you?"\n
    "um... I guess? I guess I do." you say weakly.\n
    "Yesss," Chris hisses "Goooood."...""")

def questions_seven_correct_1():
    console_slow_type("""'Let's find out if that is the correct answer' Chris calls out to the audience.
    There are some groans and even some growling emitted from the audience. You can't quite make out whether that was a bit of skin that just fell off that audience member's face, or maybe some leftover salami? Yes, salami, definitely not skin.
    You patiently sit through Chris's gab about what happens if it's wrong, knowing full well that isn't the case here. The answer was so obvious!
    Suddenly a poorly constructed space cruiser crashes through the roof of the studio and into the audience, who are dismembered, limbs flying out in every direction... but still alive?
    You watch in horror, while an old man in a labcoat and a teenage boy climb out of the space craft
    'Seriously Morty, a dimension where all TV show audience members are zombies? How *blueeerghp* predictable. Doofus Rick could have come up with a better adventure, and he eats literal shit, Morty. SHIT!'
    The pair clean themselves off, the old man points a space-gun of some kind at the ship, both jump back into the craft and speed out of the gaping hole in the roof.
    'Umm, aaanyway, as I was about to say, B was the right answer! Congratulations and let's move on to the next round!'""")

def questions_seven_correct_2():
    console_slow_type(""""'Let's find out if that is the correct answer' Chris calls out to the audience.
    There are some groans and even some growling from the audience.
    You notice some audience members are emitting a faint green glow out of their eyes.
    Life used to be so simple before the BOOM BOOM that turned half the population into green goop.
    You wonder what 2022 will have in store as you see Chris smiling at you."
    'Congratulations, C was the right answer! This means you are moving on to the next round!'
    Chris's teeth exhibit a greenish tinge... 
    """)

def questions_nine_correct_1():
    console_slow_type("""'Is this your final answer?'
    You nod. Of course the answer is B.
    You didn't withstand years of bullying at school for playing Pokémon to get it wrong now!
    You didn't dress as Pikachu 3 halloweens in a row to not know the basic evolution forms of a Gen I Pokémon!
    You didn't become the president of the Pokémon society to-
    'Amazing! You have made it to the FINAL ROUND because that answer was right!' Chris exclaims
    You downplay the triumps as the audience cheers and claps for your acheivement. Who knew Pokémon knowledge could be worth £500k one day?! 
    """)

def questions_nine_correct_2():
    console_slow_type("""'Is this your final answer?'
    You nod. You know full well the answer is D.
    Hmm. But then again, it could have been B...or C...
    Or even A!
    Yes, genius, that's how multiple-choice questions work! It could have been any of those options!
    And you had to go and choose bloody B! B?!
    Oh god, it defeinitely wasn't the right option. Look at Chris's face. That stupid, smirking face.
    He knows he's about to crush all of your hopes and dreams and he's just making you wait for it. Await your own demise!
    £500K down the drain because you got a bit to co-
    'Incredible! That was the right answer, which means you have made it to the FINAL ROUND!' Chris claps his hands in amazement
    Pfft. Knew it was the right answer all along!
    """)

def questions_ten_correct_1():
    console_slow_type(f""" 'OK so {player_name}, this is the big one. This question is for a million pounds. So feel free to take a little more time if you need it. Is that your final answer?' """)
    time.sleep(2)
    console_slow_type(""" 'Your final, final answer?' """)
    time.sleep(2)
    console_slow_type(f"""'OK. You’ve done so well tonight. We’ve loved having you here {player_name}. You managed to make it all the way to the final question, and you’re so close to leaving with a million pounds.' Chris pauses and takes a deep breath. The tension in the air is palpable, you feel your heart begin to race.""")
    time.sleep(3)
    console_slow_type(f""" '{player_name}, I’m sorry to say…' Oh no. Oh no. Surely not? I was sure that was right. """)
    time.sleep(3)
    console_slow_type(f""" 'That your life is never going to be the same again! {player_name}, congratulations! You’ve just won a million pounds!' """)
    console_slow_type(f"""The switcheroo! He did the bloody switcheroo! You barely have time to comprehend what just happened before Chris pulls you out of your chair and shakes your hand a little too aggressively.
    'Thank you for watching Who Wants to be a Millionaire! Congratulations again to {player_name} who is now a millionaire! Will someone new do it again next time? Join us then to find out!'
    The camera stops rolling and the sickeningly bright lights begin to dim.. Chris releases your hand and walks away without another word. You see him furiously washing his hands moments later. Hm, bit weird… """)
    console_slow_type(f""" 'Excuse me {player_name}, could you please come with me?' A producer appears by your side. Still in a state of shock, you follow them into a small and slightly stuffy room.
    'Congratulations! Now, we need to discuss your winnings.' """)
    console_type_slow(""" You freeze for a minute, but it’ probably just administrative stuff. Maybe it’ll be paid in installments?
    'Ok, so times are a little hard at ITV right now. I mean, we don’t really expect anyone to that much to be honest. And no one even really cares about quiz shows anymore, I mean, why did you even bother coming on?'
    Before you have a chance to explain that you were forcibly dragged here, the producer continues… """)
    time.sleep(3)
    console_slow_type("""'Ok so, we can’t really give you a million pounds. But we’ve got something even better!'""")
    console_slow_type("""'Your interest piques. Even better?'
    'So, you know Love Island right? Everyone knows Love Island. So, instead of giving you a million pounds, we’ll give you a guaranteed spot on Love Island next year. Sounds good, right?'""")
    console_slow_type("""'Um, I mean. I’m not sure I’d be the right fit for Love Island to be honest. I think I’d rather the money, or maybe some of the money?'""")
    console_slow_type("""'Come on, surely you’ve got the gist of this by now. You don’t really have a choice here. You’re going on Love Island. It’ll be great! Think of all the teeth whitening deals you’ll get when you’re done, you’ll probably make way more than a million!'""")
    console_slow_type("""Before you have a chance to even formulate a response, you’re lifted out of your seat and dragged out the room. A swimming costume and a plane ticket to Spain are shoved in your hands. I mean, maybe this won’t be too bad? The teeth whitening deals are pretty goood…
    """)

def questions_ten_correct_2():
    console_slow_type("""
    'CONGRATULATIONS' 
    Chris shouts loudly.
    The lights are blinding you.
    Confetti is shot from the floor around you as balloons fall around the desk.
    The crowd scream for you as Chris vanishes behind a screen of glitter and plastic.
    A strange ordeal but at least you've won a million.
    Right?
    Right?
    Amidst the confusion you haven't seen the stage door open.
    You see several green and black bodies barrelling towards you.
    Something matte black and metallic stands out in the sea of shining confetti.
    Suddenly...
    Darkness
    Silence, all but the occasional water droplet echoes across the room.
    And a pounding headache.
    Opening your eyes you see a dark room, and a man sat across from you.
    Fucking Jay. 
    Casually sat next to YOUR comically sized million dollar cheque.
    And a large burlap sack.
    He's stolen your cheque, and explains he'll return it upon completion of a 'simple task'.
    To run this sack across the border and deliver it to a well dressed man in Miami.
    Can't hurt, there's a million in it for you. 
    You grab the sack and head for the door.
    Blinded by the Mexican sun, finally a chance to check what's in the weighty bag.
    Gummy worms.
    Those blue and pink fucking gummy worms.
    """)


#INCORRECT OUTCOMES FUNCTIONS

def ready_or_not():
    console_slow_type("""The show runner, obviously unused to such a response remains glazed, save for a twitch in their right eye.
    'OK. Do you need anything? Water? Meat? Anything like that? Red Bull? Brain food, you know?'
    You can see the panic in their eyes as they search yours like a supermarket barcode scanner, so you reply...
    'No... I'm alright for... brain food and red bull.'""")
    ready_annoyed1 = input("\n    So you're ready?  [Y/N]  ").capitalize()
    if ready_annoyed1 == "N":
        console_slow_type("""
        'You don't want to go on? It's just the nerves, you'll be great! You might come out of this.'
        That last comment threw you a bit; you look puzzled. To the show runner read; worse."
        'A Millionaire! You might come out of this a millionaire is what I mean and what I said actually.'
        You are fairly sure they did not say that the first time, but these TV folk, hey, odd bunch - lots of terminology, who knows.
        Another TV person has come over. You can tell by the clipboard and the headset. And the stench of vacuousness.
        'What's the hold up. He's ready. You're ready aren't you buddy!'
        New TV plonker gives you a thump in the arm.""")
    else:
        story_start_game(question_index, f"'Hello and welcome to Who Wantz to be a Millionaire! Today we have {player_name} with us, an aspiring developer, hoping to win big! Let's begin with an easy one!' ", chances)
    ready_annoyed2 = input("\n  You MUST be ready...? [Y/N]  ").capitalize()
    if ready_annoyed2 == "N":
        console_slow_type("""
        The first, and more lowly of this crew hangs their head and closes their eyes.
        The second, newer, and more frightening of the two moves in close to you.
        'You are ready' TV plod no.2 says 'You know how I know?'
        'No, how?' you say.
        'Look up there at that sign.' He point high up to your left, and as you follow his finger with your eyes, his clipboard comes striking down out of the dark rendering you unconscious.
        'Bloood...bloody hell' you stammer out as your eyes open and you realise you are slumped on a stool, schlocked and blinded by incredibly bright lights.
        """)
    else:
        story_start_game(question_index, f"'Hello and welcome to Who Wantz to be a Millionaire! Today we have {player_name} with us, an aspiring developer, hoping to win big! Let's begin with an easy one!'",chances)

def green_room_wrong ():
    console_slow_type("""
    'I'm so sorry that was the..." you wait for Chris to pull his signature switcheroo.'
    'WRONG answer!'
    What!?""")
    time.sleep(2)
    console_slow_type("""
    But, b-b-but he never does that, he always does the switcheroo, the bloody Tarrant switcheroo.
    Stop saying the word switcheroo, you think. It isn't helping.
    Some producers rush over. You look to Chris but he apparently is no longer engaging with you and is staring out into the audience, whilst chewing three of his fingers
    'Look.' Some producer has swivelled you round on your swivel stool. It swivels, that is new.
    'Come with us back to the green room, freshen up, look alive and let's give it another run yeah?'
    'But the cameras!? The, the viewers at home!' At this, one of the gaggle of TV folk chuckle.
    
    """)
    time.sleep(2)
    console_slow_type("""
    
    You are a bit unsure of the whole set up but decide they probably know what's what.
    Not live. Come on, shit-for-brains.
    And so you follow the rather charming television producer back to the green room
    After a can of 7-up (that feels pretty heavy on the 7-up) and a swift muller corner, a show runner comes to get you and drags you back to the tunnel.
    This bloody tunnel, you think. It's like a maze.

    """)
    time.sleep(2)
    response = input("'Are you ready to start again?' [Y/N]   ").capitalize()
    if response == "Y" or response == "y" or response == "yes" or response == "Yes":
        console_slow_type("""'Great! Come with me then.'""")
        time.sleep(2)
        console_slow_type("""You follow the show runner back to the stool. """)
        player_name = input('What was your name again?     ').capitalize()
        story_start_game(question_index, f"\n'Great! So, {player_name}, let's begin!'", chances)
    elif response == "N" or response == "n" or response =="no":
        console_slow_type("""'Oh for faaaa...' The show runny looks away in disgust. 'You want to go down this road?'""")
        time.sleep(2)
        
        
        
    player_name = input("\n'What is your name?'   ").capitalize()
    print(f"'Hello {player_name}, hope you are ready this time.'")
    story_start_game(question_index, f"\nSo, {player_name} let's begin!", chances)

def chris_sanity_decline(chances):

    chances -= 1
    if (chances == 3):
        
        console_slow_type("""\n\t\t\tChris looks at you much in the same way a child looks at an anthill.
                        You nervously await the response.
                        'That's ok, it can get quite nervy here in the studio with so much, so, so much at stake.'
                        He grins and looks towards the cameras.
                        From behind you someone in the audience groan 'Steeeeaaaaakk!'
                        Chris asks some clipboard wielding producers 'Are we OK to go again or is this one...?'
                        He drags his finger across his throat. \n
                        The producer waves their hand around to indicate Chris to ask again.'OK! So...'\n""")
    elif (chances == 2):

        console_slow_type("""\n\t\t\tBAM! Chris has thumped his terminal. 
                        'For pitys sake. Look what you've made me do. Haha, Sorry everyone, lights are very hot in here today.' 
                        You peer over and see that Chris has hit the facade of his screen, exposing every so slightly, what he had on his screen. 
                        It doesn't look like the game, like the game on your screen. It looked like bodies. Porn?
                        'Look at me.' 
                        Chris' voice commands your gaze.
                        'You have four buttons on your side there. A, B, C and fucking D.'
                        'Do you know how many times I've done this show?'                                  
                        You shake your head.
                        'Too many.'
                        'Do you know how many times someone has CORRECTLY chosen an answer that wasn't one of the multiple choice game?'
                        You answer the man honestly. 'Is it zero.'
                        Chris looks at you with pure bile.
                        'Is that your final answer? Becuase it better be, or I will make it the final question you ever answer.'
                        Something in voice tells you this pompous clown may actually mean it. He definitely means it. 
                        'I'll ask again. One more time. For the cheap seats... Is it A, B, C, or D?'""")
    elif (chances == 1):
        console_slow_type ("""\n Chris starts laughing.
                        It is pretty funny. Your answer. 
                        He's laughing more now.
                        You start to chuckle as well.
                        It's caught on the audience are giggling.
                        Within seconds the entire is bubbling along with the laughter, its infectious as hell.
                        Chris has fallen off his stool, he's on his knees!
                        'AAAAHHHAHAHA I CAN'T' Chris bellows.
                        He crawls, over to you, and as he rises, he wipes the very tears from his eyes and puts his hand on your shoulder, he shouts:
                        '--this one, ladies and gentlemen! Aren't you all excited to eat him afterwards?'
                        Chris moves round and sits at his stool.
                        Huh, bit of a gaff there Chris, you think. They'll probably catch it in the edit. 
                        'Meets!', Tarrant injects. 'I of course mean meats. Meets and meats.'
                        Worryingly, the idea of meeting you, or at least the mention of it has put some of the crowd in an absolute furor - will you be a star you think?
                        'So just to double check, your final answer is ----' """)

    else:

        console_slow_type("""The crowd cheered for you, but it turns out your were just as wrong and dead as they were! \n
        
        \n""")
        game_over()
        sys.exit(0)

    return chances

def die_become_z():
    console_slow_type(f""" 
    Chris sucks air in through his unnaturally pearly teeth.
    The audience are baying for blood.
    You look deep into Tarrants eyes and see... joy?
    'Let's see if your answer was correct, and that is the... WRONG answer!!'
    His face lights up.
    From behind you, you hear the sharp creak of metal unhinging, and a viscious crackling as the bars holding the now frenzied mob come down.
    Your locked gaze starts to rise, following Chris's eyes up as his stool begins to rise, raising him up and up into the studio rafters where he immediately met by more show runners who shroud him in robes and drinks.'
    'BLLEEEUAGHHH!!!!'
    You look back down, house lights up, and to your horror, as they begin to approach you, you see the audience are in fact...
    THE UNDEAD.
    'Oh fuck.'
    You glance around - all exits full of the snarling and braying undead.
    'Oh fuuuuuckkkk!'
    'Limbless corpses surround you. There is no escape.' 
    'Chris! Chris, help, help me please for fuck's sake!' you yell!
    You look up and see Chris has a vantage point over the entire proceedings. He has a cigar on the go. 
    Wanker.
    As they hoard begin to supplant every inch of space around you, you aim the entirety of your lifes anger skyward and scream.
    'Chris Tarrant You WANKERRRRRRR!'
    You died. But...
    As though time at has passed you begin to grunt and bleeeuugh.
    A tazer wielding show runner approaches you.
    You grunt more heartily now you see their pulsing, delicious neck. God, you're hungry did you not have a snack in the Green Room?
    'STICK HIM WITH THE OTHERS THEN", you hear pumped out over the tannoy.
    'Grubnt, Blueghs, GRUNTHY GRUNCH.' you say.
    You didn't mean to say that, but that's what came out. what's happening? All you can think about is lashing out and biting at the show runner who is herding you into the audience cage.
    'BLAH!' You think to yourself. Blat must be it. I'm a zombie.
    And you'd be right. You are the recently reanimated corpse of your former self.
    But look on the bright side, you dumbly think as you watch a fresh faced new contestent be ushered onto the stool ahead of you...
    They look tasty.
    """)

def questions_four_incorrect():
    console_slow_type("""'You gave us the answer and, that is the... WRONG answer!!'
    His face lights up.
    'No it isn't!' you say.
    Chris freezes.
    'That's the right bloody answer.' You say. Someone coughs.
    Chris is unmoved."
    'Isn't it!?' you holler into the studio. Silence, and then a single cough.
    You lean smugly back on your in your stool and peer at Tarrant over your nose, full to the brim with blind utter confidence."
    'How did you know...' chris seethes out.
    Your smug smile wanes a little.
    'Well. You just know don't you! It's obvious.' Uh-oh. He's onto you.
    Chris begins to regain some of his former guile, and glances to his left. A lowly show runner has come forward, head bowed holding out in front of them a... staff!
    Chris takes the staff and begins to rise.
    'It would be better for you. For you BOTH. If you come clean now.' Chris is now grinning like a maniac. Both? Shit. """)
    time.sleep(1)
    console_slow_type("""'EGO SUM NUMMORUM REX ET EGO PRAECIPIO TIBI!' Tarrant screams.""")
    time.sleep(2)
    console_slow_type("""You feel compelled by his words. As your arm beings to rise and finger extend, you see his staff begin to glow, green and sparks fly from its tip.
    'I-I-I...' you stammer, unable to speak nor stop your arm, hand and index finger from indicating the extact position of your acomplice!
    Your expert plan. Entirely of your own design, has fallen completely fucking flat.""")
    time.sleep(2)
    console_slow_type("""'QUOD VOBIS MENDAX!' Bellows chris, as upon the floor holes appear, portals more like, and fiery grimaced skeletons climb through.""")
    console_slow_type("""'Wh-wh-whaaat!' you stutter..!
    'I said, die you cheater!' hisses Chris Tarrant, his eyes aglow with sadistic delight.
    The skeletons have split into two groups, one moving towards Barry - your acomplice, and by day, your plumber...
    ... the other advancing hurriedly towards you.
    You cannot move.
    Paralysed, you can do nothing but stare as each of the skeletons claws chunks from your fresh and tosses it into the audience.""")
    time.sleep(2)
    console_slow_type("""'I AM THE ITV MESSIAH AND NO-ONE CAN STOP MEEEE!' yells Chris.""")
    time.sleep(2)
    console_slow_type("""Mercifully, one of the skeletons hits an main artery in your leg, and soon everything fades to black.
    The last thing you see is the Chris Tarrant, wreathed in green flame floating over your butchered corpse, caressing the smooth bone of his skeleton children.
    Oh well.
    """)

def questions_seven_incorrect():
    console_slow_type(""" Chris looks up at you, his eyes slightly narrowed. He has that familiar smug smirk on his face. 
    \n "You've been doing really well so far. This question was for £150k, we're getting pretty close to a million now." 
    Chris takes a very, very long pause. \n \"And I can tell you....\" \n "That you will not be getting any closer. That was the... INCORRECT answer." 
    "I'm sorry, you've been a great sport!\" Chris gives you one last patronising grin. \n 
    "And thank you for watching Who Wants to Be a Millionaire! Join us next time to see if our next contestant can get any further!"\n 
    The sickeningly bright lights around you begin to dim. You sink into your chair, so overwhelmed with disappointment. 
    You don't notice the audience groaning and staggering out of their seats. Eventually, you begin to stand up. \n 
    "Hey! Where'd you think you're going! \n It was Chris. \n 
    "Um, well I've lost right? So I thought I just left..." \n 
    "Ha! You can't just leave, you've seen too much. Sit back down and stay right there." \n 
    You involuntarily fall back into your chair, you almost feel frozen. Maybe it's to do with the weird self-imposed sense of superiority Chris has… \n 
    But wait, seen too much?! What's he talking about?! This is just a quiz show, right?! A family friendly quiz show?! \n
    Before you can ask anymore questions, Chris is chaperoned away by a group of runners. \n
    Suddenly, what felt like a TV studio begins to feel very weird. Dark, cold and very quiet. Still, you feel unable to move, in case you disappoint Chris. \n 
    You start to hear a thudding sound, it's coming from the fire exit doors. Weird, you hadn't noticed them before. \n 
    The thudding continues, it's getting louder and louder. Maybe everyone will burst back in? \n
    You weren't wrong after all and this is just some strange pranked version they're trying out… \n 
    Eventually, the doors fly open. The light from outside blurs your vision slightly, but you can see Chris! You were right! \n 
    But wait, is he wearing a MAGA hat? And screaming 'Stop the count'?! And that audience definitely seems much bigger, and more alive than it did previously… \n 
    You realise there must be thousands, or hundreds of thousands of people flooding into the studio. You can see some police, maybe they're here to help? Oh actually, maybe not… \n 
    You realise there is no way out as the huge crowd begin to surround you. With your final breath, you scream.. \n "Chris Tarrant You WANKERRRRRRR!" \n You died.""")

def questions_nine_incorrect():
    console_slow_type(""""'Are you absolutely positive that that is your final answer?'
    You nod, somewhat unsure now. Oh god, what if it's the wrong answer...
    Suspensful music plays through the studio...""")
    time.sleep(3)
    console_slow_type("""'We will find out after this break!'""")
    time.sleep(2)
    console_slow_type("""The music plays once more and the producers start walking on stage, handing papers to Chris, who looks bored with their content.
    You feel a slight tug on your right leg.
    A two-foot tall, bearded individual is standing by your side. You notice something shimmering on their back, almost like a pair of wings... Reading the confusion in your face, they reach into the pocket of their sparkling tulle skirt and pull out a small pouch.""")
    time.sleep(1)
    console_slow_type("""'Alright, mardy bum. I was just avin' a mooch round the studio and could tell yous not avin' a sound time.'""")
    time.sleep(2)
    console_slow_type("""You look around the studio, hoping to see if anyone else has noticed this, erm, person, but to no avail. Is this a stress-induced hallucination?""")
    time.sleep(1)
    console_slow_type("""'I was 'opin to get a brew 'ere before I 'ead out, but noones offered me one! The cheek of it!' he huffs and gestures around the studio, but again, noone reacts""")
    console_slow_type("""'Ere, 'ave some of these, you'll be buzzin in no time. Even Chris 'avin a strop won't get in the way!'""")
    console_slow_type("""He hands you the pouch, you open it and drop the contents into your palm, which turn out to be a few small multicoloured sweets, resembling skittles." 
    'Ah, me own creation that. You won't find anything like it in the world'
    Still unsure of whether this is really happening, you take the pouch. You look at the little embroidery at the top, which simply says 'JAY'. Maybe that was their name?
    By the time you look up, Jay, or whoever they were, had dissappeared. You're still wondering what just happened...well, it has been a very odd life since the 2020s, so anything's possible at this rate!""")
    time.sleep(1)
    console_slow_type(f"""An assistant comes over to you with a bottle of water.
    'Hi, {player_name}, you're doing great, but I noticed you were starting to look a bit nervous towards the end there and... Oh!'
    They look down at the sweets in your hand.
    'Are those calming pills? Everyone here uses meds to deal with Chris's tantrums.'
    You've heard of calming pills before, this must be a bit like that, right?
    You take a few, it'll be fine. Let's hope that answer was corr-""")
    time.sleep(2)
    console_slow_type("""'And we are back on in 3, 2, 1'""")
    console_slow_type(f"""'Welcome back, ladies and gentlement, to Who Wants to be a Millionaire. Here we have {player_name}, an aspiring developer, who is currently on Question 9, which, if answered correctly, will result in a whopping win of £500k!'
    You begin to feel sweat running down your face. You feel warm. These pills aren't doing anything!
    'So, you chose option {answer} before the break, let's see if it is correct...'
    'Aaand I'm sorry, but the answer you chose is WRONG! You won't be moving on to the next round.'
    'Thank you for watching Who Wants to Be a Millionaire! Join us next time to see if our next contestant can get any further!'""")
    time.sleep(1)
    console_slow_type("""The music, now muffled in your ears, sounds again and the bright lights start to strobe all around you...
    You watch as Chris, wobbly in his appearance, begins to walk off stage distorting into the lights.
    As the heat in your face intensifies, you feel numb and limp in the rest of your body. You cannot get out of your chair.
    'What the fuck was in those sweets?!' you scream, as you try to lift your paralysed arms to feel your face.
    With the heat no longer barable, you hear a high pitch ringing in your head, as everything arounds you begins to spin.""")
    time.sleep(2)
    console_slow_type("""And then, darkness.""")
    time.sleep(2)
    console_slow_type("""A horrified producer looks on, as chunks of your brain, along with a bunch of bright coloured sweets, go flying all over the stage. They wipe some of it from their face.""")
    time.sleep(2)
    console_slow_type("""'My god, their head just exploded?!'""")

def questions_ten_correct3():
    console_slow_type("""'The answer is...'
    Dew dew dewwww noise.
    'We'll find out after the break!' exclaims Chris to camera 2.
    'Awwww, you love doing that' you say over the podiums as a director calls cut.
    'Do I? Do I love that, do I? I love it, when I say that we will find something out after an ad break. I love that?'
    You wait and process this uncharacteristic response from Chris Tarrant.
    Adverts run on a  moniter nearby.
    'Yeahhh.' You say, without about as much conviction as a goat facing a tiger.
    Clanging behind you. There's somehing going on behind the scenes, but the house lights aren't up - which is odd on an ad break, but then...
    'OI! Tarrant!'
    It's only bloody Jeremy Clarkson, marching through swathes of black clad television crew. You look to Chris.
    'Oh shit" he says.' He looks terrified.
    What the shit is this, Chris, you kfc bargain bucket of dicks!?"
    'Jeremy, just hold on...'
    A producer tries to stand directly in his path to their wonderboy Tarrant.
    Well we know how well that went down on Top Gear.
    Jeremy lands a devestating right hook on the jaw of the producer, who sprawls across the studio floor.
    'Keep them coming, ITV, I came just came to eat meat and punch producers, and I am allll out of meat!'
    This, rather terrifying interlude has you questioning whether you really ought to just get up out of the chair, and let these two titans of the small screen hash it out.
    'But before you can, Chris grabs your arm.'
    'Be cool,' Chris hisses 'There's a shiv taped to the bottom of your stool, when I give the signal, put it in my hand.'
    He moves away, toward the oncoming Clarkson, all fury and thinly-veiled neo conservative imperialism.
    What fucking signal though, you think as you search desperately for this... shiv?! Why is there a shiv taped to the stool!
    You find it, and yank it from it's duct tape hold.
    'Jeremy, cool down, let's chat.' Tarrant has his soothing voice on.
    You notice Chris's right hand has drifted behind him his palm open facing towards you. Is this the signal?
    Clarkson is swinging away at runners, producers and directors like a Silverback, batting away a family of mongooses.
    The entire studio floor is littered with bloody and unconscious television crew.
    'Tarraaaannnnnnnt!' Shouts Jeremy.
    You glance back to Chris's hand and see he is opening and closing it, grabbing behind him at thin air - That has to be the signal!
    You jummp up and with the skill of a relay race runner palm off the crude shiv - a blade strapped to a hollow microphone - into Tarrant's hand!
    The gap between the two hosts has closed considerably and just as Clakson is winding up to strike, Chris fires the blade into his gut.
    Blood spills out of the giant racist with each sharp intrusion Chris makes.
    'AARRgh, noooo, not like thiiiiiisss.'
    Jeremy is dying. Chris walks backwards away from him and drops the blade.
    From the wings, in swoops James May and Richard Hammond. Hammond is weeping. May seems to have wet himself.
    'Bezos will have your head for this Tarrant' Richard Hammond wails!
    Tarrant seems unfazed as even more TV crew pulls the dead and unconscious away.
    May and Hammond carry off Clarkson/'s bloody corpse down the very tunnel from where you entered into this Lovecraftian nightmare.
    A sharp sound draws your attention to the monitor displaying the adverts.
    A Public Service Annoucment is being broadcast by Amazon, across all channels, and all devices. Everywhere.
    Jeff Bezos appears on screen. His cyborg arms spin in fury.
    'Calling all contractors. The price on the head of Chris Tarrant has now risen to $14,000,000.'
    'I AM BEZOS. AND I HAVE SPOKEN.'
    You look to Chris, who is unconvincingly shrugging.
    '30 seconds until we're back!' You hear from behind you.
    'I thought this wasn't live!?' you say.
    Chris looks back at you, now covered in Clarkson blood, he looks like Nosferatu.
    Some of it is, some isn't - no-one really knows. Not really.
    As you sit blankly considering the events that have unfolded, you wonder if you are actually in a coma, and if, like you hope, you'll be woken by friends and family before too long.""")

def questions_ten_correct4():
    console_slow_type(f"""
    'OK, so you've just answered a question that might win you a million pounds. You've been doing so well today, but this is the make or break question.'
    'And I can tell you...' 
    'That you gave me....' 
    'The wrong answer.'
    'I'm so sorry {player_name} but it's game over today. You've been fantastic, thanks so much!'
    'And that's all for tonight ladies and gents! I've been Chris Tarrant and this has been Who Wants To Be A Millionaire! Join us next week to see if our next contestant can become a millionaire!'
    The sickeningly bright lights around you begin to dim. You take a few minutes, the dissapointment crushing you.
    A producer appears by your side.
    '{player_name}, I'm sorry, you did great tonight. It's such a shame you won't be leaving with anything. If you could just follow me, I'll lead you out.'
    You follow the producer down a long and spiralling corridor. 
    'You said you were a Python developer, right?' 
    'Right.'
    'Interesting, you use lots of colons there don't you?'
    'Um, yeah I guess colons come up a lot...'  
    'That's really interesting, I love colons. Probably my favourite bit of punctuation. It would be a shame if they disappeared, wouldn't it?'  
    Why won't they shut up about colons? This whole day has been so weird. 
    'Anyway! This is you. Thanks a lot {player_name}, hopefully I'll see you again soon.' 
    
    THE NEXT DAY  
    
    The whole day yesterday felt like such a strange dream. It's hard to believe it was even real. 
    Given all the strange stuff Chris was telling you throughout the day, you're almost surprised to come out unscathed. Weird. 
    But anyways, it's back to the day job now. You fire up your laptop and begin to get cracking on some code you've been working on. 
    You're working on a function, when you notice your colon key has disspeared 
    What?! The colon key? How on earth are you going to do anything without the colon key?!! Nothing will ever work! You're doomed! 
    Suddenly, the bizzare conversation you had with the producer comes back to you. No...surely not 
    You try again, trying every possible way to get a fucking colon up. Eventually, a message appears on your terminal 
    'Hello {player_name}, it's me, Chris Tarrant here.'
    'We loved having you on the show yesterday, but you didn't expect to just leave without us changing in your life in some way did you?' 
    'I must inform you, you have been cursed. You will never be able to use your colon key again.' 
    What??!! But surely they can't do this, how did they even do this?! 
    'It's probably time to think about a career change, don't you think? Anyway {player_name}, it's been great. See you soon.'  
    'CHIRS FUCKING TARRANT. COME BACK. COME BAAAAAACK!!!'  You scream at your computer, but realise it's futile. 
    The disappointment of losing a chance to have million pounds feels like nothing compared to losing your beloved colon. You realise that your life will definitely never be the same again. 
    """)


#PLAYTHROUGH FUNCTIONS

def story_start_game(question_index, opening_string, chances):
    question_list = questions_and_answers[question_index] #gets 1S list from out list of lists
    question = question_list[0] #gets the question from the list
    console_slow_type(opening_string + ", " + question) #we print the name and question to the terminal
    correct_answer1 = question_list[-1]  #(from right to left, Last option in list, usually the correct answer
    correct_answer2 = question_list[-2]  #Second last
    correct_answer3 = question_list[-3]  #Third last 
    correct_answer4 = question_list[-4]  #Fourth last list 
    console_slow_type(f'{question_list[1]}, {question_list[2]}, {question_list[3]}, or {question_list[4]}') #prints options 
    answer = input("""\n'  Which one do you pick?   A, B, C, or D?'  """).capitalize() #gets input
    def fifty_fifty ():
        fifty_art()
        print(f"'The two remaining correct answers are...{question_list[-1]} and {question_list[-2]}'")

    
    def ask_the_audience (correct_answer3,correct_answer4,correct_answer1,correct_answer2):
        audience_art()
        potential_audience1 = random.randint(5,20)
        potential_audience2 = random.randint(5,20)
        correct_audience1 = random.randint(25,50)
        correct_audience2 = 100 - potential_audience1 - potential_audience2 - correct_audience1
        
    
        if "A" == correct_answer3:
            print(f'{correct_answer3}: {potential_audience1}%')
        elif "A" == correct_answer4:
            print(f'{correct_answer4}: {potential_audience2}%') 
        elif "A" == correct_answer1:
            print(f'{correct_answer1}: {correct_audience1}%')
        elif "A" == correct_answer2:
            print(f'{correct_answer2}: {correct_audience2}%')
        if "B" == correct_answer3:
            print(f'{correct_answer3}: {potential_audience1}%')
        elif "B" == correct_answer4:
            print(f'{correct_answer4}: {potential_audience2}%')
        elif "B" == correct_answer1:
            print(f'{correct_answer1}: {correct_audience1}%')
        elif "B" == correct_answer2:
            print(f'{correct_answer2}: {correct_audience2}%')
        if "C" == correct_answer3:
            print(f'{correct_answer3}: {potential_audience1}%')
        elif "C" == correct_answer4:
            print(f'{correct_answer4}: {potential_audience2}%')
        elif "C" == correct_answer1:
            print(f'{correct_answer1}: {correct_audience1}%')
        elif "C" == correct_answer2:
            print(f'{correct_answer2}: {correct_audience2}%')
        if "D" == correct_answer3:
            print(f'{correct_answer3}: {potential_audience1}%')
        elif "D" == correct_answer4:
            print(f'{correct_answer4}: {potential_audience2}%')
        elif "D" == correct_answer1:
            print(f'{correct_answer1}: {correct_audience1}%')
        elif "D" == correct_answer2:
            print(f'{correct_answer2}: {correct_audience2}%')

    
    def phone_a_friend2():
        print("'OK! Let's phone a better friend.'")
        time.sleep(2)
        global friend_name
        friend_name = input("'So who will it be?' ").capitalize()
        if friend_name == "Jay":
            time.sleep(2)
            print("' Ok. Be that way then. I told you that we would NOT be ringing Jay. Really, it's the best thing for you. You ignored me, so you're on your own. You're not ringing anyone.'")
            # return to question 
        else:
            print(f"'You've decided to ring {friend_name}, let's hope they pick up! Remember, you don't need to accept their answer.'")
            time.sleep(3)
            print("The phone rings.")
            time.sleep(3)
            print("It rings again")
            time.sleep(3)
            print(f"Suddenly, the voice of {friend_name} fills the studio.")
            time.sleep(2)
            print("'Hello?'")
            time.sleep(2)
            print(f"""'Hello {friend_name}! It's Chris Tarrant here, you're on Who Wants To Be A Millionaire! Your friend {player_name} needs your help. You only have 30 seconds. {player_name}, take it away!'""")
            time.sleep(2)
            print("You repeat the question as fast as you can.")
            time.sleep(3)
            print(f"""'Hm, so I think my gut feeling is taking me to C. But thinking about it, it might actually be A. Although I guess depending on how you wanted to go about it, you could make a case for D. Actually, I feel pretty good about B. I'd go for B. Or should I trust my gut and go for C? And I do definitely think there's a chance it might be A. You also definitely can't discount D. I think honestly {player_name}, I'm not that sure.'""")
            time.sleep(3)
            print("....")
            time.sleep(3)
            print(f"'And you're all out of time! Thanks a lot {friend_name}, you've been great.'")
            time.sleep(2)
            print(f"""'So, after that great help from {friend_name}, let's hear the question again and get your final answer.'""")
            
    def phone_a_friend():
        phone_art()
        print("'OK! You have decided to phone a friend. Think carefully about you want to ring, you only get one shot.'")
        time.sleep(2)
        global friend_name
        friend_name = input("'So who do you want to ring?'").capitalize()
        if friend_name == "Jay":
            print("' Jay?! Like, Jay from CodeNation Jay?! Why on earth would you want to ring him? I can't see him being any help at all really.'")
            time.sleep(2)
            print("You can't ring Jay. That's me, Chris Tarrant making an executive decision. Let's phone someone else.")
            phone_a_friend2()
        else: 
                print(f"""'You've decided to ring {friend_name}, let's hope they pick up! Remember, you don't need to accept their answer.'""")
                time.sleep(3)
                print("The phone rings.")
                time.sleep(3)
                print("It rings again")
                time.sleep(3)
                print(f"Suddenly, the voice of {friend_name} fills the studio.")
                time.sleep(2)
                print("'Hello?'")
                time.sleep(2)
                print(f"'Hello {friend_name}! It's Chris Tarrant here, you're on Who Wants To Be A Millionaire! Your friend {player_name} needs your help. You only have 30 seconds. {player_name}, take it away!'""")
                time.sleep(2)
                print("You repeat the question as fast as you can.")
                time.sleep(3)
                print(f"""' Hm, so I think my gut feeling is taking me to C. But thinking about it, it might actually be A. Although I guess depending on how you wanted to go about it, you could make a case for D. Actually, I feel pretty good about B. I'd go for B. Or should I trust my gut and go for C? And I do definitely think there's a chance it might be A. You also definitely can't discount D. I think honestly {player_name}, I'm not that sure.'""")
                time.sleep(3)
                print("....")
                time.sleep(3)
                print(f"""'And you're all out of time! Thanks a lot {friend_name}, you've been great.'""")
                time.sleep(2)
                print(f"""'So, after that great help from {friend_name}, let's hear the question again and get your final answer.'""")

    
    if (answer == correct_answer1):
        question_index += 1
        print("'Is that your final answer?' You nod. 'Ok, let's see if it is the right answer...'") 
        
        if (question_index == 4): 
            time.sleep(2)
            questions_four_correct_1()
            time.sleep(2)
            story_start_game(question_index, "\nYou got through Q4, Next...", chances)
        elif (question_index == 7):
            time.sleep(2)
            questions_seven_correct_1()
            time.sleep(2)
            story_start_game(question_index, "\nYou got through Q7, doing well so far...", chances)
        elif (question_index == 9):
            time.sleep(2)
            questions_nine_correct_1()
            time.sleep(2)
            story_start_game(question_index, "\nYou got through Q9, last one...", chances)
        elif (question_index == 10):
            time.sleep(3)
            questions_ten_correct_1()
            game_winner_art()
            sys.exit(0)
        else:
            story_start_game(question_index, "\nIt was correct! Next questions please...", chances)
                
    if (answer == correct_answer2):
        question_index += 1
        print(f"'So, {player_name}, let's see if it is the right answer...") 
        if (question_index == 4): 
            time.sleep(2)
            questions_four_correct_1()
            time.sleep(2)
            story_start_game(question_index, "\nYou got through Q4, Next...", chances)
        elif (question_index == 7):
            time.sleep(2)
            questions_seven_correct_2()
            time.sleep(2)
            story_start_game(question_index, "\nYou got through Q7, doing well so far...", chances)
        elif (question_index == 9):
            time.sleep(2)
            questions_nine_correct_2()
            time.sleep(2)
            story_start_game(question_index, "\nYou got through Q9, last one...", chances)
        elif (question_index == 10):
            time.sleep(3)
            questions_ten_correct_2()
            time.sleep(2)
            game_winner_art()
            sys.exit(0)
        elif (question_index == 1):
            green_room_wrong()
        else:
            story_start_game(question_index, "\nIt was correct! Next questions please...", chances)
            
    elif (answer == "Q"): #checks if player presses q 
        
        quit_check = input("\n You have pressed Q and choosen to equestion_indexit the game, are you sure you want to quit? (Y/N)   ").capitalize() #checks if the plays wants to quit
        if  (quit_check == "Y"): 
            console_slow_type("\n Chris pulls that surprised face he loves so much, folds his arms and leans back on his stool. 'No-one is keeping you here...' ", 0.02) 
            game_over()
            sys.exit(0) #quits program
        else:
            story_start_game(question_index, f"\nHello and welcome to Who Wantz to be a Millionaire! Today we have {player_name} with us, an aspiring developer, hoping to win big! Let's continue with the question.", chances)

    elif (answer == "L"):
            console_slow_type("""
            Enter "F" for Fifty / Fifty - This will remove two incorrect answers and leave two remaining right answers. \n 
            Enter "P" for Phone a Friend - This will give you the option of calling upon your designated expert.
            Whether they're smart or not is your stupid fault. Isn't it. \n
            Enter "Z" for Ask the Audience - this will put the question to our room full of Brainiacs.    
            """)
            choice = input("Choose a lifeline: ").capitalize()
            if choice == "F":
                fifty_fifty()
                story_start_game(question_index, f"\nOk, {player_name}, you have your two possible answers. Which one do you choose?", chances)
            elif choice == "P":
                phone_a_friend()
                story_start_game(question_index, f"\nOk, {player_name}, hope your friend was useful. Which one do you choose?", chances)
            elif choice == "Z":
                ask_the_audience(correct_answer3,correct_answer4,correct_answer1,correct_answer2)
                story_start_game(question_index, f"\nOk, {player_name}, this is what our wonderful studio audience thinks. Which one do you choose?", chances)
            

    elif (answer != "A" and answer != "B" and answer != "C" and answer != "D" and answer != "Q" and answer != "P" and answer != "F" and answer != "H" and answer != "J"): 
        chances = chris_sanity_decline(chances)
        story_start_game(question_index, "\n'So, now that you figured out how to use the only buttons in front of you, let's continue!'", chances) 
    
    elif (answer != correct_answer1) and (question_index < 4): 
        green_room_wrong()

    elif (answer != correct_answer1) and (question_index == 4): 
        questions_four_incorrect()
        time.sleep(2)
        game_over()
        sys.exit(0)
    
    elif (answer != correct_answer1) or (answer != correct_answer2) and (question_index == 7): 
        questions_seven_incorrect()
        time.sleep(2)
        game_over()
        sys.exit(0)
    
    elif (answer != correct_answer1) or (answer != correct_answer2) and (question_index == 9): 
        questions_nine_incorrect()
        time.sleep(2)
        game_over()
        sys.exit(0)
    
    elif (answer == correct_answer3) and (question_index == 10): 
        questions_ten_correct3()
        time.sleep(2)
        game_over()
        sys.exit(0)
    
    elif (answer == correct_answer4) and (question_index == 10): 
        questions_ten_correct4()
        time.sleep(2)
        game_over()
        sys.exit(0)
    
    elif (answer != correct_answer1) and (question_index == 5) or (answer != correct_answer1) and (question_index == 6) or (answer != correct_answer1) and (question_index == 8):
        die_become_z()
        time.sleep(2)
        game_over()
        sys.exit(0)

def intro():
    global player_name
    time.sleep(2)
    print(u"""\u001b[33m

             )    )                        )           )              )                              \u001b[37;1m*    \u001b[33m(   (    (    \u001b[37;1m(      \u001b[33m )   \u001b[37;1m  )        \u001b[33m(\u001b[0m   (        
 (  \u001b[33;1m(     \u001b[37;1m( /\u001b[33m( ( /(     \u001b[37;1m(  (      \u001b[33m(     ( /\u001b[37;1m(  *   \u001b[33;1m) ( /(     \u001b[37;1m*   ) ( \u001b[33;1m/(       (           (        (  \u001b[37;1m`   )\u001b[33;1m\ ))\ \u001b[37;1m) )\ ) \u001b[33;1m)\ \u001b[37;1m) ( /(  (\u001b[33;1m /(  \u001b[37;1m(     \u001b[33;1m)\ ))\ )     
 )\)\u001b[37;1m)(   \u001b[33;1m'\u001b[37;1m\()))\u001b[33;1m\())    )\))(   \u001b[37;1m' \u001b[33;1m)\    )\()` )  /( )\())  \u001b[37;1m` \u001b[33;1m)  /( )\())    ( )\ (        )\       )\))( (()/((\u001b[37;1m)/((()/((()/\u001b[33;1m( )\()) )\()) )\   (()/(\u001b[37;1m()\u001b[33;1m/((    
((_)()\ )\u001b[37;1m((_)\(\u001b[33;1m(_)\    ((_)()\ ((((_)( ((\u001b[37;1m_)\ (\u001b[33;1m) )\u001b[37;1m(_\u001b[33;1m)((_)\    ( )(_)((_\u001b[37;1m)\     \u001b[33;1m)((_))\    ((((_)(    ((_)(\u001b[37;1m)\ /\u001b[33;1m(_)/\u001b[37;1m(\u001b[33;1m_))/(_))/(_)((_)\ \u001b[37;1m((_)(\u001b[33;1m(((_)(  /(_)/(_))\   
_(())\_)()_((_) ((_)   _(())\_)()\ _ )\ _((_(_(_()) _((_)  (_(_())  ((_)   ((_)_((_)    )\ _ )\   (_()((_(_))(_)) (_)) (_))   ((_) _((_)\ _ )\(_))(_))((_)  
\u001b[31;1m\ \((_)/ | || |/ _ \   \ \((_)/ (_)_\(_| \| |_   _||_  /   |_   _| / _ \    | _ | __|   (_)_\(_)  |  \/  |_ _| |  | |  |_ _| / _ \| \| (_)_\(_|_ _| _ | __| 
 \ \/\/ /| __ | (_) |   \ \/\/ / / _ \ | .` | | |   / /      | |  | (_) |   | _ | _|     / _ \    | |\/| || || |__| |__ | | | (_) | .` |/ _ \  | ||   | _|  
  \_/\_/ |_||_|\___/     \_/\_/ /_/ \_\|_|\_| |_|  /___|     |_|   \___/    |___|___|   /_/ \_\   |_|  |_|___|____|____|___| \___/|_|\_/_/ \_\|___|_|_|___| 

\u001b[0m""")
    time.sleep(2)
    game_controls()
    time.sleep(2)
    console_slow_type("A dark tunnel. cold. dark, very dark.")
    console_slow_type("Someone touches your hand, you recoil, fear and sweat running out of you in equal measure.")
    console_slow_type("\n'HEY!'")
    player_name = input("'Hey you. What's your name?'   ").capitalize()
    console_slow_type(f"""\n'Hi {player_name}!'
        'Sorry - its a little crazy here these days'""")
    console_slow_type("""
        "'Are you ready?'    """)
    time.sleep(1)
    ready1 = input("[Y/N]   ").capitalize()
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
        The man in the chair beckons you forward.""")
    elif ready1 == "N":
        console_slow_type("'Err...'")
        ready_or_not()
    elif ready1 != "Y" or ready1 != "N":
        console_slow_type("""'God, can't you make a decision!?' One of the producers mutters...\n Type again    """)
        time.sleep(2)
    beckon_forward = input ("\nGo? [Y/N]  ").capitalize()
    if beckon_forward == "N":
        console_slow_type("The producer shunts you in the back cascading you forward towards the centre of the room.")
    elif beckon_forward != "Y" and beckon_forward != "N":
        console_slow_type("""'God, can't you make a decision!?' One of the producers mutters...\n Type again""")
    elif beckon_forward == "Y":
        console_slow_type(f"""
        You move closer to the empty chair opposite to man and see now, the man is none other than ITV's Chris Tarrant
        'H-Hi Chris.' You manage to stammer out.""")
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
        job_desc = input("\n'is that right?' [Y/N]  ").capitalize()
        if job_desc == "N":
            console_slow_type("""
        'Oh, sorry! Why don't we just crack on with the start_game, and you can fill me in as we go. Lots of contestants to get through today.'
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
    ['\nQuestion 1: How many players should a team have on the pitch at the start of a football game? ', 'A: 10', 'B: 5', 'C: 11','D: 15','B','D', 'A','C'],
    ['\nQuestion 2: Which Williams sister has won more Grand Slam titles? ', 'A: Serena', 'B: Venus','C: Jessica','D: Janice','C','D', 'B', 'A'],
    ['\nQuestion 3: Which racer holds the record for the most Grand Prix wins? ','A: Lewis Hamilton', 'B: Michael Schumacher', 'C: Daniel Ricciardo','D: Kimi Raikkonen','C', 'D', 'B','A'],
    ['\nQuestion 4: Which language is considered romantic by the United Nations? ','A: Spanish','B: French', 'C: Russian', 'D: Chinese','C','D', 'B','A'],
    ['\nQuestion 5: What part of the atom has no electric charge? ', 'A: Proton','B: Electron','C: Neutron','D: Megatron','A','B', 'D','C'],
    ['\nQuestion 6: What is meteorology the study of? ','A: The Weather', 'B: Meteors', 'C: Astroturf','D: Dinosaurs','D','C','B','A'],
    ['\nQuestion 7: Which IMDB Top 250 film has the highest rating to date of 9.2/10? ','A: Inside Out','B: The Godfather','C: The Shawshank Redemption','D: Up','D','A', 'C','B'],
    ['\nQuestion 8: Which natural disaster is measured with a Richter scale? ','A: Tsunamis','B: Earthquakes','C: Hurricanes','D: Tornados','D','C','A','B'],
    ['\nQuestion 9: What is an evolution form of the creature Geodude from the popular cartoon, Pokémon? ','A: Gurdurr', 'B: Graveler','C: Golett','D: Golem','A','C','D','B'],
    ['\nQuestion 10: Which musical artist has achieved the all-time record of 5 Billboard #1 singles from one album? ', 'A: Michael Jackson', 'B: Rod Stewart', 'C: Katy Perry','D: Prince', 'D','C','B','A' ]
]


#GLOBAL VARIABLES
x = 0
question_index = 0
chances = 4

#FUNCTION CALLS - GAME PLAYTHROUGH
intro()
time.sleep(2)
story_start_game(question_index, f"\n'So, {player_name}, excited? Good. Let's start you with an easy one!'", chances)