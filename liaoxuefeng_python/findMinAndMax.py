# -*- coding: utf-8 -*-
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
	try:
		Min = L[0]
		Max = L[-1]
		for n in L:
			if n < Min:
				Min = n
			if n > Max:
				Max = n
		return (Min, Max)
	except:
		return (None, None)