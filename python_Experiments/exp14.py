from sys import argv
script,u_name=argv
prompt='> '
print "Hi %s,I'm the %s script" %(u_name,script)
print "I'd like to Ask you a few Questions:"
print "Do you Like me %s" %u_name
likes=raw_input(prompt)
print "where do you live %s" %u_name
lives=raw_input(prompt)
print "What kind of computer do you have"
comp=raw_input(prompt)
print """
Alright,so you said %r about talking me
you live in %r.Not sure where that is,
and you have a %r type computer. nice
""" %(likes,lives,comp)
