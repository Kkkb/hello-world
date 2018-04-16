# -*- coding: utf-8 -*-
'''
	请尝试写一个验证Email地址的正则表达式。
	版本一应该可以验证出类似的Email：
	someone@gmail.com
	bill.gates@microsoft.com
'''

import re

def is_valid_email(addr):
	if re.match(r'[a-z\.]+@[a-z]+.com', addr):
		return True
	else:
		return False
'''
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
'''

def name_of_email(addr):
	if re.match(r'<', addr):
		m = re.match(r'<([a-zA-z\s]+)>\s[a-z]+@[a-z]+\.[org|com]', addr)
	else:
		m = re.match(r'([a-z]+)@[a-z]+\.[org|com]', addr)
	if m:
		return m.group(1)
	return None

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')