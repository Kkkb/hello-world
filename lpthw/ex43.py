# -*- coding: utf-8 -*-
from random import randint 

class PlayerRoom(object):
	def __init__(self):
		self.player_name = "kkkb"

	def set_name(self):
		self.player_name = raw_input("Your name: ")
#		while  isinstance(self.player_name, int):
#			self.player_name = raw_input("Enter your name again: ")
		#name = player_name
		return self.player_name	
#	def get_name(self):
#		return self.player_name

	def print_name(self):
		print "Hi, %s,let's play a game!" % self.player_name

	def go_player_room(self):
		a_player = PlayerRoom()
		a_player.set_name()
		a_player.print_name()
		return 'DiceRoom'

#a = PlayerRoom()
#a.go_player_room()
#print a.player_name
'''PlayerRoom Test
a_player = PlayerRoom()
a_player.set_name()
a_player.print_name()
'''
#a_player.set_name(1)
#a_player.print_name()

class DiceRoom(object):
	'''
	a game played with dice. Guess the number.
	'''
	def __init__(self):
		self.computer_guess_number = 0
		self.user_guess_number = 0
		self.score = 0

	def computer_guess(self):
		self.computer_guess_number = randint(1, 6)
#		print "cg is: ", self.computer_guess_number
		return self.computer_guess_number

	def player_guess(self):
		self.user_guess_number = int(raw_input("Choose the number between 1 and 6: "))
		return self.user_guess_number

	def player_guess_again(self):
		self.user_guess_number = int(raw_input())
		return self.user_guess_number

	def result(self):
#		print "Here is result"
		if self.computer_guess_number == self.user_guess_number:
			self.score += 1
			print "Correct!"
			print "Your score: %d" % self.score
		else:
			self.score -= 1
			print "Not correct.Try again: ",
			self.player_guess_again()
			self.result()


		if self.score > 0:
			return 'WinRoom'
		else:
			return 'EndRoom'
'''
dice = DiceRoom()
dice.computer_guess()
dice.player_guess()
dice.result()
'''

class EndRoom(object):
	def __init__(self):
		self.say_bye = ["Nice to meet you!",
					"See you!",
					"Bye bye",
					"EXIT",
					"No time"]

	def exit_room(self):
		print self.say_bye[randint(0, len(self.say_bye) - 1)]
		exit(0)

#e = EndRoom()
#e.exit_room()

class WinRoom(object):
	def __init__(self, player_name):
		self.say_win = {0 : "You win...",
						1 : "Great...",
						2 : "Wonderful...",
						3 : "Beautiful...",
						4 : "Nice...",
						5 : "Good job..."}
		self.player_name = player_name

	def win_room(self):
		print self.player_name, self.say_win[randint(0, len(self.say_win) - 1)]
		exit(0)

#w = WinRoom()
#w.win_room()