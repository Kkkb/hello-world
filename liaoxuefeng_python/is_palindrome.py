# -*- coding: utf-8 -*-
'''
回数是指从左向右读和从右向左读都是一样的数，
例如12321，909。请利用filter()筛选出回数
'''

def is_palindrome(n):
	n = str(n)
	for i in range(len(n) // 2):
		if not n[i] == n[-(i + 1)]:
			return False
	return True