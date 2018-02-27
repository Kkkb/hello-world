animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

# The animal at 1. ------ 'python'
print "The 2ed animal is at 1 and is a %r" % animals[1]
print "The animal at 1 is the 2ed animal and is a %r\n" % animals[1]

# The 3rd animal. ------ 'peacock'
print "The 3rd animal is at 2 and is a %r" % animals[2]
print "The animal at 2 is the 3rd animal and is a %r\n" % animals[2]

# The 1st animal. ------ 'bear'
print "The 1st animal is at 0 and is a %r" % animals[0]
print "The animal at 0 is the 1st animal and is a %r\n" % animals[0]

# The animal at 3. ------ 'kangaroo'
print "The 4th animal is at 3 and is a %r" % animals[3]
print "The animal at 3 is the 4th animal and is a %r\n" % animals[3]

# The 5th animal. ------ 'whale'
print "The 5th animal is at 4 and is a %r" % animals[4]
print "The animal at 4 is the 5th animal and is a %r\n" % animals[4]

# The animal at 2. ------ 'peacock'
print "The 3rd animal is at 2 and is a %r" % animals[2]
print "The animal at 2 is the 3rd animal and is a %r\n" % animals[2]

# The 6th animal. ------ 'platypus'
print "The 6th animal is at 5 and is a %r" % animals[5]
print "The animal at 5 is the 6th animal and is a %r\n" % animals[5]

# The animal at 4. ------ 'whale'
print "The 5th animal is at 4 and is a %r" % animals[4]
print "The animal at 4 is the 5th animal and is a %r\n" % animals[4]

print "---------------"
n = ['First', 'Second', 'Third', 'Forth', 'Fiveth', 'Sixth']
for i in range(0, 6):
	print "n[%d] = %s" %(i, n[i])
	#i += 1