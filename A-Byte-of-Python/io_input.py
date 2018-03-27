
import re

def ignore(f):
	def inner(innertext):
		text = re.sub('[, ?.]', '', innertext)
		text = re.sub('[R]', 'r', text)
		return f(text)
	return inner
#forbidden = (!, ?, ' ', ., ,,)

def reverse(text):
	return text[::-1]

@ignore
def is_palindrome(text):
#	text = re.sub('[, ?.]', '', something)
	return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
	print("Yes, it is a palindrome")
else:
	print("No, it is not a palindrome")



''' test decorator
def wrapper(f):
	def inner(something):
		print("I'm inner")
		return f(something)
	return inner

@wrapper
def foo(something):
	print("I'm foo {}".format(something))


def foo():
	print("I'm foo")
foo = wrapper(foo)


foo('kb')
'''