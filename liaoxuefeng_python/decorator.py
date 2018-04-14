# -*-coding: utf-8 -*-
'''
请设计一个decorator，
它可作用于任何函数上，
并打印该函数的执行时间
'''

import time, functools, types

def metric(fn):
	def wrapper(*args, **kw):
		start = time.time()
		result = fn(*args, **kw)
		elapsed = time.time() - start
		print('%s executed in %s ms' % (fn.__name__, elapsed))
		return fn(*args, **kw)
	return wrapper
'''
@metric
def fast(x, y):
	time.sleep(0.0012)
	return x + y

@metric
def slow(x, y, z):
	time.sleep(0.1234)
	return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
print(f,s)
'''

def begin_end_call(fn):
	def wrapper(*args, **kw):
		print("begin call")
		fn(*args, **kw)
		print("end call")
		return fn
	return wrapper
'''
@begin_end_call
def foo():
	print("I'm foo")

foo()
'''

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	if isinstance(text, types.FunctionType):
		func, text = text, ''
		return decorator(func)
	else:
		return decorator
'''
@log('executed')
def foo():
	print("I'm foo")

foo()
'''