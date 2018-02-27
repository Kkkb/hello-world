import ex43

class KGame(object):
	def __init__(self, go):
		self.go = go

	def play(self):
		next = self.go

		while True:
			print "/n****************"
			room = getattr(self, next)
			next = room()
			
a = ex43.PlayerRoom()
a.go_player_room()

dice = ex43.DiceRoom()
dice.computer_guess()
dice.player_guess()
dice.result()

w = ex43.WinRoom('kkkb')
w.win_room()

e = ex43.EndRoom()
e.end_room()

#k = KGame(PlayerRoom)
#k.play()