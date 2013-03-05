# match keywords in the following lexicon:
# --------------------------------------------------------------------
# | Direction | north, south, east, west, down, up, left, right, back|
# |   Verbs   | go, stop, kill, eat                                  |
# |Stop words | the, in, of, from, at, it                            |
# |   Nouns   | door, bear, princess, cabinet                        |
# |  Numbers  | any string of 0 though 9 characters                  |
# --------------------------------------------------------------------

def scan(sentence):
	#stuff = raw_input('> ')
	words = sentence.split()
	
	direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
	verbs = ['go', 'stop', 'kill', 'eat']
	stops = ['the', 'in', 'of', 'from', 'at', 'it']
	nouns = ['door', 'bear', 'princess', 'cabinet']

	results = []
	for items in words:
		if items in direction:
			results.append(('direction', items)) 
		elif items in verbs:
			results.append(('verb', items)) 
		elif items in stops:
			results.append(('stop', items)) 
		elif items in nouns:
			results.append(('noun', items)) 
		elif convert_number(items) == False:
			results.append(('error', items)) 
		else:
			results.append(('number', items)) 
			
	return results
	
		
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return False
