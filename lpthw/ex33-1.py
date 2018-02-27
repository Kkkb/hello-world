def while_append(n, p):
	i = 0
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + p
		print "numbers now: ", numbers

numbers = []
while_append(6, 2)

print "The numbers: "

for num in numbers:
	print num