#coding utf-8

def backtracking(word):
		
	if(len(word) < 3):
		return
	
	for i in xrange(len(word)):
		new_word = word[:i] + word[i+1:]
		if(new_word not in set_words):
			set_words.add(new_word)
			backtracking(new_word)

while True:
	
	try:
		global set_words
		set_words = set()
		
		word = raw_input()
		set_words.add(word)
		
		for i in xrange(len(word)):
			set_words.add(word[i])
		
		backtracking(word)
		
		list_words = list(set_words)
		list_words.sort()
		
		for iword in list_words:
			print iword
		print
	
	except EOFError:
		break
		
