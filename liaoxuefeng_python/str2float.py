# -*- coding: utf-8 -*-
'''
利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456
'''

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, \
		  '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return DIGITS[s]

	str1, str2 = s.split('.')

	def a_str2float(str):
		return reduce(lambda x, y: x * 10 + y, map(char2num, str))

	return a_str2float(str1) + a_str2float(str2) * .1 ** len(str2) 