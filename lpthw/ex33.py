#i = 0
numbers = []
# n = 6

def while_append(n, p):
	i = 0
#	numbers = []
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += p
		print "numbers now: ", numbers

while_append(6, 1)

print "The numbers: "

for num in numbers:
	print num

print '**************'
while_append(88)