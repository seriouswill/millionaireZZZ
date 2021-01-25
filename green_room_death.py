import time

def green_room_wrong ():
    console_slow_type("""
    "I'm so sorry that was the..." you wait for Chris to pull his signature switcheroo."
    "WRONG answer!"
    What!?""")
    time.sleep(2)
    console_slow_type("""But, b-b-but he never does that, he always does the switcheroo, the bloody Tarrant switcheroo." 
    "Stop saying the word switcheroo, you think. It isn't helping."
    "Some producers rush over. You look to Chris but he apparently is no longer engaging with you and is staring out into the audience, whilst chewing three of his fingers"
    ""Look."" Some producer has swivelled you round on your swivel stool. It swivels, that is new.
    "Come with us back to the green room, freshen up, look alive and let's give it another run yeah?"
    But the cameras!? The, the viewers at home!" At this, one of the gaggle of TV folk chuckle.""")
    time.sleep(2)
    console_slow_type("""You are a bit unsure of the whole set up but decide they probably know what's what.
    "Not live. Come on, shit-for-brains."
    And so you follow the rather charming television producer back to the green room
    After a can of 7-up (that feels pretty heavy on the 7-up) and a swift muller corner, a show runner comes to get you and drags you back to the tunnel.
    This bloody tunnel, you think. It's like a maze.
    """)
    time.sleep(4)

    response = input("Are you ready to start again? [Y/N]")
    if response == "Y" or response == "y" or response == "yes" or response == "Yes":
        console_slow_type("""Great! Come with me then.""")
        time.sleep(2)
        #function for querstion 1
        console_slow_type("""You follow the show runner back to the stool. """)
    elif response == "N" or response == "n" or response =="no":
        console_slow_type(""""Oh for faaaa..." The show runny looks away in disgust. "You want to go down this road?""")
        time.sleep(2)
        #ready_or_not function

green_room_wrong()