# -*- coding: utf-8 -*-
'''
	对中文进行JSON序列化时，
	json.dumps()提供了一个ensure_ascii参数，
	观察该参数对结果的影响
'''

import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)

if __name__ == '__main__':
	s2 = json.dumps(obj)
	print(s, s2)
