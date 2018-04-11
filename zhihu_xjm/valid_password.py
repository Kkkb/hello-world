# -*- coding: utf-8 -*-
# 题 1
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库

# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10

def valid_password(pwd):
	if not (2 <= len(pwd) <= 10):
		return False

	if not pwd[0].isalpha():
		return False

	for p in pwd[1:-1]:
		if not (p.isalnum() or p == "_"):
			return False

	if not pwd[-1].isalnum():
		return False

	return True

# 字符串方法isalpha, isalnum
# 参考https://docs.python.org/3.3/library/stdtypes.html#string-methods