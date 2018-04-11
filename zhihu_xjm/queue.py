# -*- coding: utf-8 -*-
# 题 5
# 写一个 Queue 类，它有两个方法，用法如下
'''
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3

'''

class Queue(object):
	def __init__(self):
		self.q = []

	def enqueue(self, number):
		self.q.append(number)

	def dequeue(self):
		return self.q.pop(0)

if __name__ == '__main__':
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)

	print(q.dequeue())
	print(q.dequeue())
	print(q.dequeue())