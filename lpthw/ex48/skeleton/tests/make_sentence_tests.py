from nose.tools import *
from ex48 import make_sentence

def test_sentence():
	subject = ('noun', 'player')
	verb = 	('verb', 'go')
	object = ('direction', 'north')
	sentence = make_sentence.Sentence(subject, verb, object)
	
	assert_equal(sentence.subject, subject[1])
	assert_equal(sentence.verb, verb[1])
	assert_equal(sentence.object, object[1])

def test_peek():
	subject = ('noun', 'player')
	verb = 	('verb', 'go')
	object = ('direction', 'north')
	sentence = make_sentence.Sentence(subject, verb, object)
	
	word_list = make_sentence.lexicon.scan("kill the princess")
	assert_equal(sentence.peek(word_list), 'verb')
	word_list = []
	assert_equal(sentence.peek(word_list), None)

def test_match():
	subject = ('noun', 'player')
	verb = ('verb', 'go')
	object = ('direction', 'north')
	sentence = make_sentence.Sentence(subject, verb, object)

	word_list = make_sentence.lexicon.scan("eat the bear")
	assert_equal(sentence.match(word_list, 'verb'), ('verb', 'eat'))
	assert_equal(word_list, [('stop', 'the'), ('noun', 'bear')])
	assert_equal(sentence.match(word_list, 'noun'), None)
	word_list = []
	assert_equal(sentence.match(word_list, 'noun'), None)

def test_skip():
	subject = ('noun', 'player')
	verb = ('verb', 'go')
	object = ('direction', 'north')
	sentence = make_sentence.Sentence(subject, verb, object)

	word_list = make_sentence.lexicon.scan("eat the bear")
	sentence.skip(word_list, 'verb')
	assert_equal(word_list, [('stop', 'the'), ('noun', 'bear')])
	sentence.skip(word_list, 'verb')
	assert_equal(word_list, [('stop', 'the'), ('noun', 'bear')])

def test_parse_verb():
	subject = ('noun', 'player')
	verb = ('verb', 'go')
	object = ('direction', 'north')
	sentence = make_sentence.Sentence(subject, verb, object)

	