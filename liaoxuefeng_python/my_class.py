# -*- coding: utf-8 -*-
'''
请把下面的Student对象的gender字段对外隐藏起来，
用get_gender()和set_gender()代替，并检查参数有效性
'''
class Student(object):

	def __init__(self, name, gender):
		self.name = name
		self.__gender = gender

	def get_gender(self):
		return self.__gender

	def set_gender(self, gender):
		if (gender == 'male') or (gender == 'female'):
			self.__gender = gender
		else:
			raise ValueError('bad gender')

bart = Student('Bart', 'male')
print(bart.get_gender())
bart.set_gender('female')