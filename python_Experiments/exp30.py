people = 30
cars =40
trucks=15

if cars>people:
    print "we should take the cars"
elif cars < people:
    print "We should not take the cars."
else:
    print "We cant decide."
    
if trucks>cars:
    print "That too many trucks."
elif trucks < cars:
    print "May be we could take the trucks"
else:
    print "We still cant decide."
    
if people > trucks:
    print "Alright,let's just take the trucks"
else:
    print "Fine,let's stay home then."                        
