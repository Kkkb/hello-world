# -*- coding: utf-8 -*-
# 利用切片操作，实现一个trim()函数，
# 去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
	before_blank = 0
	for i in s:
		if i == ' ':
			before_blank += 1
		else:
			break
	
	after_blank = 0
	for n in range(1, len(s) + 1):
		if s[-n] == ' ':
			after_blank -= 1
		else:
			break

	start = before_blank
	if after_blank == 0:
		end = None
	else:
		end = after_blank

	return s[start : end]

def ttrim(s):
	while s[:1] == ' ':
		s = s[1:]
	while s[-2:-1] == ' ':
		s = s[:-2]
	return s