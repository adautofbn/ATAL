#coding utf-8

def emptyTable():
	result = []
	for i in xrange(5):
		line = []
		for j in xrange(5):
			line.append(0)
		result.append(line)
	return result
	
def validCell(x,y):
	if(x < 5 and y < 5 and x >= 0 and y >= 0):
		if(table[x][y] == 0 and pathTable[x][y] == 0):
			return True
		else:
			return False
	else:
		return False
	
def createPath(x,y):
	if(validCell(x,y)):
		pathTable[x][y] = 1
		createPath(x-1,y)
		createPath(x+1,y)
		createPath(x,y-1)
		createPath(x,y+1)

n = int(raw_input())
count = 0

while(count < n):
	global table
	table = []
	line = raw_input()
	global pathTable
	pathTable = emptyTable()
	if(len(line.strip()) > 0):
		count += 1
		table.append(list(map(int, line.split())))
		for i in xrange(4):
			line = raw_input()
			table.append(list(map(int, line.split())))
		createPath(0,0)
		if(pathTable[4][4]):
			print "COPS"
		else:
			print "ROBBERS"
