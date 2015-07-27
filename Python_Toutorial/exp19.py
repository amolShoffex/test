def cheese_and_cracker(cheese_count,boxes_of_crackers):
    print "You have %d cheeses" %(cheese_count)
    print "you have %d boxes_of_crackers" %(boxes_of_crackers)
    print "Man Thats enough for this party"
    print "Get a blanket.\n"

print "we can just give the function no.directly"
cheese_and_cracker(20,30)  
  
print "OR we can use variable from script"
cheese_count=50
boxes_of_crackers=100
cheese_and_cracker(cheese_count,boxes_of_crackers)    

print "even you can do math inside"
cheese_and_cracker(12+10,10+10)

print "we can combine cariable and math"
cheese_and_cracker(cheese_count+10,boxes_of_crackers+10)
