# -*- coding: utf-8 -*-
# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式

def cap_string(str):
	s_list = str.split(' ')
	new_s_list = [s.capitalize() for s in s_list]
	return ' '.join(new_s_list)