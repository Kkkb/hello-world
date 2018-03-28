def findSmalllest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

#old_list = [2, 1, 4, 3, 6, 5]
def my_select_sort(old_list):
	new_list = []
	while len(old_list) > 0:
		smallest_index = findSmalllest(old_list)
		new_list.append(old_list[smallest_index])
		old_list.pop(smallest_index)
	return new_list

def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmalllest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print(selectionSort([5, 3, 6, 2, 10]))
print(my_select_sort([5, 3, 6, 2, 10]))
'''
s_list = [2, 6, 1, 4, 3, 5]
min = s_list[0]
for i in s_list:
	if min > i:
		min = i

print(min)
'''