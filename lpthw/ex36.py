#coding=utf-8
# 剪刀石头布 scissors-rock-paper  y-g-o
import random
from sys import argv
#computer_guess = ['y', 'g', 'o']
#ucg("y or g or o \n> ")
#if user_guess == "y":
script, name = argv

def result(user_guess, computer_guess):
	'''剪刀石头布规则'''
	uy = (user_guess == 'y')
	cy = (computer_guess == 'y')
	ug = (user_guess == 'g')
	cg = (computer_guess == 'g')
	uo = (user_guess == 'o')
	co = (computer_guess == 'o')

	if uy and cy:
		print "y-y  > win win"
	elif ug and cg:
		print "g-g  > win win"
	elif uo and co:
		print "o-o  > win win"
	elif uy and cg:
		print "y-g  > you fail"
	elif uy and co:
		print "y-o  > you win"
	elif ug and cy:
		print "g-y  > you win"
	elif ug and co:
		print "g-o  > you fail"
	elif uo and cy:
		print "o-y  > you fail"	
	elif user_guess == 'o' and computer_guess == 'g':
		print "o-g  > you win"
	else:
		print "Please type y or g or o"

	print "\n"

print "Hi! %r" % name
while True:
	computer_guess = random.choice(['y', 'g', 'o'])
	user_guess = raw_input("y or g or o : ")
	result(user_guess, computer_guess)