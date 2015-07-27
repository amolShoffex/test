def add(a,b):
    print "Adding %d + %d" %(a,b)
    return a+b

def sub(a,b):
    print "Subracting %d - %d" %(a,b)
    return a-b

def mul(a,b):
    print "Multiplying %d * %d" %(a,b)
    return a*b
    
def div(a,b):
    print "Dividing %d /%d " %(a,b)   
    return a/b
print "Let's do some math with just function"

age=add(30,5)
height=sub(78,4)
weight=mul(90,2)
iq=div(100,2)

print "Age:%d, height:%d, weight:%d, IQ:%d" %(age,height,weight,iq)

print "Here is Puzzle."   

what=add(age,sub(height,mul(weight,div(iq,2))))

print "Thats becomes",what,"Can you do it by hand?"
      
