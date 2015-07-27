the_count=[1,2,3,4,5]
fruits =['apple','orange','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print "Theis is count %d" % number
    
for fruit in fruits:
    print "A fruits of the type %s" % fruit
    
for i in change:
    print "I got %r " % i
    
elements =[]

for i in range(0,6):
    print "Adding %d to the list." %i
    elements.append(i)
    
for i in elements:
    print "Elements was: %d" %i
                
