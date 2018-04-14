# -*- coding: utf-8-*-
'''
请利用@property给一个Screen对象加上width和height属性，
以及一个只读属性resolution
'''

class Screen(object):
	def __init__(self, width=None, height=None):
		self.__width = width
		self.__height = height

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		if isinstance(value, int):
			self.__width = value
		else:
			raise ValueError('Must be int')
	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		if isinstance(value, int):
			self.__height = value
		else:
			raise ValueError('Must be int')
	
	@property
	def resolution(self):
		self.__resolution = self.__width * self.__height
		return self.__resolution

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)