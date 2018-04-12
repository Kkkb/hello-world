# -*- coding: utf-8 -*-
# 以下函数允许计算两个数的乘积，请稍加改造，
# 变成可接收一个或多个数并计算乘积：

def product(*args):
	result = 1
	for a in args:
		result *= a 
	return result