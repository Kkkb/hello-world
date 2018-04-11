# -*- coding: utf-8 -*-
# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式

def cap_string(str):
	cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', \
		   'H', 'I', 'J', 'K', 'L', 'M', 'N', \
		   'O', 'P', 'Q', 'R', 'S', 'T', 'U', \
		   'V', 'W', 'X', 'Y', 'Z']
	low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', \
		   'h', 'i', 'j', 'k', 'l', 'm', 'n', \
		   'o', 'p', 'q', 'r', 's', 't', 'u', \
		   'v', 'w', 'x', 'y', 'z']

	if str[0] in cap:
		s = str[0]
	else:
		s = cap[low.index(str[0])]
	
	for i in str[1:]:
		if i in low:
			s += i
		else:
			s += low[cap.index(i)]
	return s