import time

def opening_game ():
    print("A dark tunnel. cold. dark, very dark.")
    time.sleep(2)
    print("Someone touches your hand, you recoil, fear and sweat running out of you in equal measure.")
    time.sleep(2)
    print("'HEY!'")
    time.sleep(2)
    player_name = input("'Hey you. What's your name?'")
    print(f""""Hi {player_name}!"
"Sorry - its a little crazy here these days""")
    time.sleep(3)
    print("""
"Are you ready?""")
    time.sleep(3)
    ready1 = input("[Y/N]") 
    if (ready1 == "Y"):
        print("""
"Great follow me"...
The stranger take your hand and leads you through the dark, turning left, then right, you hear the oncoming throng of.... something. 
Then suddenly, the stranger turns you right and...""")
    time.sleep(3)
    print(f"""Dazzling lights, blind you. From all directions cheers and yell - You glance around you trying to take it all in, but before you can make sense of it all...
"PLEASE WELCOME - {player_name}!!!""")
    time.sleep(3)
    print("""A man in his 50's, white hair, smug grin is sat at a stool that simultaneously looks too tall and too small for him.
Music swells around you - lasers, greeen and red swing around the room causing hush amongst what you now see is .. an audience!""")
    time.sleep(3)
    print("""
You look back to the man in the chair. You're nerves subside. It's millionaire. You fucking got this.
The man in the chair becons you forward.""")
    if ready1 == "N":
        print("Err...")
    elif ready1 != "Y" and ready1 != "N":
        print(""""God, can't you make a decision!?" One of the producers mutters...\n Type again""")
        #ready_or_not func
    time.sleep(3)
    beckon_forward = input ("Go? [Y/N]")
    if beckon_forward == "N":
        print("The producer shunts you in the back cascading you forward towards the centre of the room.")
    elif beckon_forward != "Y":
        print(""""God, can't you make a decision!?" One of the producers mutters...\n Type again""")
    elif beckon_forward == "Y":
        print(f"""
You move closer to the empty chair opposite to Man and see now, the man is none other than ITV's Chris Tarrant
"H-Hi Chris." You manage to stammer out.""")
    time.sleep(2)
    print("""
"Hello! Let's give name a warm welcome everyone!"
You glance around the audience. they are stony quiet. The occasional Groan escapes one of them. A few are wearing MAGA hats. 
Did I do something wrong?""")
    time.sleep(3)
    print("""
"A Warm welcome I said"!
At Chris's commmand, they begin to holler and shout.""")
    time.sleep(3)
    print("""
Out of the corner of your eye you notice one of the runners throw something into the crowd.""")
    time.sleep(3)
    print(f"""
You look to where it landed and see the audience clamber for it. Is that...
"SO!"
Your eyes wheel back to Chris...
"{player_name}, I undertsand you're a, wow, you're a python developer, is that right?!""")

    job_desc = input("is that right? [Y/N]")
    
    if job_desc == "N":
        print("""
"Oh, sorry! Why don't we just crack on with the questions, and you can fill me in as we go. Lots iof contestants to get through today."
get through?
"Err sure, no worries Chris. Thank you.""")
    else:
        print("""
"Wow. So what's that, like, 8 hours a day in the reptile enclosure!" 
Chris' shit eating grin shines bright, even under the hot lights of the studio.
Groans and moans from the audience.""")
    time.sleep(3)
    print("""
"HA. haha, no it's um - rather, I'm actually um, a software, well, dev-"
"I KNOW." Tarrant buts in abruptly. Then through a gritted smile he says...""")
    time.sleep(3)
    print(""" 
"play nicely now mate, let's not let things get out of hand..." he leans in "for both of our sakes.""")
    time.sleep(6)
    print("Millionaire music and lasers swirl through the air, giving the previous moment no time to gain any footing your mind.")

#on to q1 etc

opening_game()
