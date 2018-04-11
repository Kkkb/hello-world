# -*- coding: utf-8 -*-
# 题 2
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用

def prime_numbers():
	pn = []
	for n in range(2, 101):
		t = 0
		for s in range(1, n + 1):
			if n % s == 0:
				t += 1
		if t == 2:
			pn.append(n)
	return pn



# 质数，又称素数，指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数