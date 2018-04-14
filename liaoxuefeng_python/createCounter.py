# -*- coding: utf-8 -*-
'''
利用闭包返回一个计数器函数，
每次调用它返回递增整数
1.内部函数一般无法修改外部函数的参数
2.想要修改需要声明 nonlocal
3.内部函数可以修改外部list中的元素
'''
def createCounter():
	s = [0]
	def counter():
		s[0] += 1
		print(s[0])
	return counter