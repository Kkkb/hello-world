# study from ex15.py

from sys import argv

script, file_name = argv

txt = open(file_name)

print "Here is your file %r: " % file_name
print txt.read()

file_again = raw_input("Please type the file again: ")

txt_again = open(file_again)

print "Here is your file %r: " % file_again
print txt_again.read()

txt.close()
txt_again.close()