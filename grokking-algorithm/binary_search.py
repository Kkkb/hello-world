a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
guess = 1.1

def sequential_search(guess, a_list):
	times = 0
	for i in a_list:
		times += 1
		if i == guess:
			print("{}---{} == {}".format(times, i, guess))
			break
		else:
			print("{}---{} != {}".format(times, i, guess))

#sequential_search(guess, a_list)
def my_binary_search(guess, a_list):	
	times = 0
	while True:
		times += 1
		print("{}---".format(times))
		high = len(a_list) - 1
		if a_list[high//2] == guess:
			print("win")
			break
		elif a_list[high//2] < guess:
			a_list = a_list[(high//2 + 1):]
		else:
			a_list = a_list[:(high//2 - 1)]

#my_binary_search(guess, a_list)

def binary_search(list, item):
	low = 0
	high = len(list) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = list[mid]
		if guess == item:
			return mid
		if guess < item:
			low = mid + 1
		else:
			high = mid - 1
	return None

f_list = [1, 3, 5, 7, 9]
print(binary_search(f_list, 3))
print(binary_search(f_list, -1))