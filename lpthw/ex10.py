tabby_cat = "\tI'm tabbed in.\a\a" 
persian_cat = "I'm split\non a line.\a"
backslash_cat = "I'm \\ a \\ %s." % "cat"

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "******************"
print "%r" % "\'"
print "%s" % "\'"