def bubble_sort(L):
	for j in range(len(L)):
		for i in range(len(L) - 1 - j):
			print(j,i+1)
			if L[i] > L[i + 1]:
				L[i], L[i + 1] = L[i + 1], L[i]
	return L

if __name__ == '__main__':
	print([2, 5, 6, 8, 3, 9, 1, 4, 7, 10])
	print(bubble_sort([2, 5, 6, 8, 3, 9, 1, 4, 7, 10]))