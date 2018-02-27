class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)

one_room = Room('name_one_room', 'description_one_room')

#print one_room.name 
#print one_room.description
#print one_room.paths

#print one_room.go('north')

one_room.add_paths({'east': one_room})
print one_room.paths
print one_room.go('east')