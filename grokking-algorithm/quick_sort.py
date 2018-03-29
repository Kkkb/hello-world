def myqsort(l):
	if len(l) < 2:
		return l
	else:
		base = l[0]
		small = []
		big = []
		for i in l[1:]:
			if l[0] > i:
				small.append(i)
			else:
				big.append(i)
		return myqsort(small) + [l[0]] + myqsort(big)

l = [2, 1,5,2,75,53,21,96,45,12,423,565,7,43,1,23436,67,45,2,56,32,25]
print(myqsort(l))


def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))