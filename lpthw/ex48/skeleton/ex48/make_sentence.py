from ex48 import lexicon
class ParserError(Exception):
	pass

class Sentence(object):

	def __init__(self, subject, verb, object):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]

	def peek(self, word_list):
		if word_list:
			word = word_list[0]
			return word[0]
		else:
			return None

	def match(self, word_list, expecting):
		if word_list:
			word = word_list.pop(0)

			if word[0] == expecting:
				return word
			else:
				return None
		else:
			return None

	def skip(self, word_list, word_type):
		while self.peek(word_list) == word_type:
			self.match(word_list, word_type)

	def parse_verb(self, word_list):
		self.skip(word_list, 'stop')

		if self.peek(word_list) == 'verb':
			return self.match(word_list, 'verb')
		else:
			raise ParserError("Expected a verb next.")

	def parse_object(self, word_list):
		self.skip(word_list, 'stop')
		next = self.peek(word_list)

		if next == 'noun':
			return self.match(word_list, 'noun')
		if next == 'direction':
			return self.match(word_list, 'direction')
		else:
			raise ParserError("Expected a noun or direction next.")

	def parse_subject(self, word_list, subj):
		verb = self.parse_verb(word_list)
		obj = self.parse_object(word_list)

		return Sentence(subj, verb, obj)

	def parse_sentence(self, word_list):
		self.skip(word_list, 'stop')

		start = self.peek(word_list)

		if start == 'noun':
			subj = self.match(word_list, 'noun')
			return self.parse_subject(word_list, subj)
		elif start == 'verb':
			# assume the subject is the player then
			return self.parse_subject(word_list, ('noun','player'))
		else:
			raise ParserError("Must start with subject, object, or verb not: %s" % start)