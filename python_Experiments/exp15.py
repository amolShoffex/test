from sys import argv
script,filename=argv
text=open(filename)
print "Here is the file name %s" %filename
print text.read()

print "type file name again:%s" %filename

text_again=open(filename)
print text_again.read()

