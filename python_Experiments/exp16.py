from sys import argv
script,filename=argv
print "We'r going to erase %r file:" %filename
print "if you dont want that hit CTR-C(^C)"
print "if you want hit RETURN"
raw_input("?")
print "opening the file"
target=open(filename,'w')
print "Truncating the file GoodBye.."
target.truncate()
print "Now I'm going to ask you for three lines:"
line1=raw_input("line1: ")
line2=raw_input("line2: ")
line3=raw_input("line3: ")
print "I'm going to write this to the file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
print "And finally close it:"
target.close()
