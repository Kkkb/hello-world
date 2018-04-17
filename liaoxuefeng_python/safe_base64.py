# -*- coding:utf-8 -*-

'''
	请写一个能处理去掉=的base64解码函数
'''
import base64

def safe_base64_decode(s):
	add_s = s + b'='
	while not len(add_s) % 4 == 0:
		add_s += b'='
	return base64.b64decode(add_s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')