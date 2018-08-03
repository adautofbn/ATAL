def makeSet(sets,v):
	vSet = set()
	vSet.add(v)
	sets.append(vSet)
	return sets

def findSet(sets,v):
	for s in sets:
		if(v in s):
			return s

def unionMST(sets,u,v):
	uSet = findSet(sets,u)
	vSet = findSet(sets,v)
	newSet = uSet.union(vSet)
	sets.remove(uSet)
	sets.remove(vSet)
	sets.append(newSet)
	return sets
	
def createMST():
	mst = set()
	sets = list()
	for v in vertexs:
		sets = makeSet(sets,v)
	edges.sort()
	for (w,(u,v)) in edges:
		uSet = findSet(sets,u)
		vSet = findSet(sets,v)
		if(uSet != vSet):
			mst.add((w,(u,v)))
			sets = unionMST(sets,u,v)
	return mst

def walkMST(mst):	
	finalTime = 0
	rests = 0
	for (w,(u,v)) in mst:
		finalTime += w
		if(w > tmax):
			rests += 1
			finalTime += 2
	return finalTime, rests
	
blocks, paths, tmax = map(float, raw_input().split())

while (blocks != 0 and paths != 0 and tmax != 0):
	
	vertexs = set()
	edges = list()
	paths = int(paths)
	
	for i in range(paths):
		v1, v2, w = map(float,raw_input().split())
		vertexs.add(int(v1))
		vertexs.add(int(v2))
		edges.append((w,(int(v1),int(v2))))
	mst = createMST()
	finalTime, rests = walkMST(mst)
	print "%.2f %d" % (finalTime, rests)
	blocks, paths, tmax = map(float, raw_input().split())
