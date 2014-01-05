import sys
import cPickle
def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # we've found our end node, now find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]
    # detect if it's the first time through, set current distance to zero
    if not visited: distances[start]=0
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxint)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,sys.maxint)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
    return shortestpath(graph,closestnode,end,visited,distances,predecessors)

#main
coords = cPickle.load(open('coords.p', 'rb'))
adjmat = cPickle.load(open('adjmat.p', 'rb'))
distance = cPickle.load(open('distance.p', 'rb'))

names = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Z','X','Y','W','Q','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AR','AS','AT','AU','AV','AZ','AX','AY','AW','AQ']

G = {}
lat = float(sys.argv[1])
lng = float(sys.argv[2])

latLngNum = 0

for x in range(0,len(coords)):
        temp = {}
	if(coords[x][0]==lat and coords[x][1]==lng):		
		latLngNum = x		
        for y in range(0,len(coords)):
                if( int(distance[x][y])==0 ):
                    continue
                if( int(adjmat[x][y])!=1 ):
                    continue
                temp[names[y]] = int(distance[x][y])                
        G[names[x]] = temp

#print G

#print shortestpath(G,"A",names[latLngNum])[1]

fullCordsPath = ""

for index, nood in enumerate(shortestpath(G,"A",names[latLngNum])[1]):
	poz = 0	
	for i in range(0,len(names)):
		if(str(nood)==names[i]):
			poz = i
			break
	if i == 0:
		fullCordsPath = fullCordsPath + str(coords[poz][0])+","+str(coords[poz][1])
	else:
		fullCordsPath = fullCordsPath+ ";" + str(coords[poz][0])+","+str(coords[poz][1])

print fullCordsPath



