
def rc(arr):
	if arr == []:
		return 0
	else:
		arr.pop()
		return 1 + rc(arr)

print(rc([1,2,3,4,5]))