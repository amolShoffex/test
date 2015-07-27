from sys import argv
from os.path import exists
script,new_file,old_file=argv
print "Coping from %s to %s" %(old_file,new_file)
infile=open(old_file,'r')
indata=infile.read()

print "input file is %d of long" %len(indata)
out_file=open(new_file,'w')
out_file.write(indata)

print "Alright All done.."
infile.close()
out_file.close()
