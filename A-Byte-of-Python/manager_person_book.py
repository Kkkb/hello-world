import pickle

#people_dict = {}


def save_object(people_dict):
	f = open('people.txt', 'wb')
	pickle.dump(people_dict, f)
	f.close()

def load_object():
	f = open('people.txt', 'rb')
	people_dict = pickle.load(f)

def list_all():
	items = people_dict.items()
	for a, b in items:
		print("name:{}, wechat:{}, phone:{}".format(b, a.wechat, a.phone))

class People(object):
	def __init__(self, name, wechat=None, phone=None):
		self.name = name
		self.wechat = wechat
		self.phone = phone
		people_dict[self] = self.name
		save_object(people_dict)

try:
	f = open('people.txt', 'rb')
	people_dict = pickle.load(f)
	f.close()
except FileNotFoundError:
	people_dict = {}
	print("Nice to meet you first time!")


'''test

a = people('king')
print(a.name)

b = people(name='bob')
print(b.name)
'''
'''
if __name__ == '__main__':
	main()
'''