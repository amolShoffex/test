print "You enter dark room with two doors. do you go throgh door 1 or door2"
door =raw_input("> ")

if door=='1':
    print "there is a giant bear here eating a cheese cake.what do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear=raw_input("> ")
    if bear == "1":
        print "the bear eats your face off.  Good Job!"
    elif bear == "2":
        print "the bear eats your legs off.  Good job!"
    else:
        print "Well,doing %s is probably better. Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina." 
    print "1. Blueberries."
    print "2. yellow jacket cloathespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2": 
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "you stumble around and fall on a knife and die.   Good job!"
              
