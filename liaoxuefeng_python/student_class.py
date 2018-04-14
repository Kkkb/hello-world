# -*- coding: utf-8-*-
'''
为了统计学生人数，可以给Student类增加一个类属性
每创建一个实例，该属性自动增加
'''
class Student(object):
	count = 0

	def __init__(self, name):
		self.name = name
		Student.count += 1

print(Student.count==0)
bart = Student('Bart')
print(Student.count==1)
lisa = Student('Bart')
print(Student.count==2)