def sum(arr):
	if arr == []:
		return 0
	else:
		return arr.pop(0) + sum(arr)

arr = [1, 2, 3, 4, 5, 6]
print(sum(arr))