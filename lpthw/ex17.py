# -- coding:utf-8 --
# 简化代码，将其写成一行
from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# input = open(from_file)
# indata = open(from_file).read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

# output = open(to_file, 'w')
open(to_file, 'w').write(open(from_file).read())

#print "Alright, all done."

#output.close()
#open(from_file).close()