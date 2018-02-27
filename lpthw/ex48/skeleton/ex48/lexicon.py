def scan(stuff):
	sentence = [('direction', 'north'),
			    ('direction', 'south'),
			    ('direction', 'east'),
			    ('verb', 'go'),
			    ('verb', 'kill'),
			    ('verb', 'eat'),
			    ('stop', 'the'),
			    ('stop', 'in'),
			    ('stop', 'of'),
			    ('noun', 'bear'),
			    ('noun', 'princess')]

	return_sentence = []
	words = stuff.split()

	for i in range(0, len(words)):
		for tup in sentence:
			if words[i] in tup:
				return_sentence.append(tup)
				break
			elif convert_number(words[i]):
				if not ('number', convert_number(words[i])) in return_sentence:
					return_sentence.append(('number', convert_number(words[i])))
					break
			elif tup == sentence[-1]:
					return_sentence.append(('error', words[i]))				
	return return_sentence
	
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None