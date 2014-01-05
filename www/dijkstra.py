import sys
import cPickle
import urllib, json
import pprint
import time
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

lat = float(sys.argv[1])
lng = float(sys.argv[2])
latLngNum = len(coords)
izvan_dosega = 1

coords.append([lat,lng])
dis_temp = []
adj_temp = []
for red in distance: red.append(['a','b']);
for red in adjmat: red.append(0);
for b in coords:
    adj_temp.append(0);
    dis_temp.append(['a','b']);    
distance.append(dis_temp);
adjmat.append(adj_temp);

for b in range(0,len(coords)):
    a = latLngNum
    error = 0
    while error>=0:
        if(error>0):
            time.sleep(1.0)            
        if(a==b):
            distance[a][b] = 0
        if(a>b):
            URL2 = "http://maps.googleapis.com/maps/api/directions/json?origin="+str(coords[a][0])+","+str(coords[a][1])+"&destination="+str(coords[b][0])+","+str(coords[b][1])+"&mode=walking&sensor=false"
            googleResponse = urllib.urlopen(URL2)               
            jsonResponse = json.loads(googleResponse.read())
            try:
                ij_distance = jsonResponse['routes'][0]['legs'][0]['distance']['value']
            except IndexError:
                ij_distance = ''
            if(ij_distance!=''):
                distance[a][b] = ij_distance
                distance[b][a] = ij_distance
                error = -1
                if( len(jsonResponse['routes'][0]['legs'][0]['steps'])==1 ):
                    adjmat[a][b] = 1
                    adjmat[b][a] = 1
                    izvan_dosega = 0                        
            else:
                error = error + 1
        else:
            error = -1

G = {}
for x in range(0,len(coords)):
    temp = {}	
    for y in range(0,len(coords)):
        if( int(distance[x][y])==0 or int(adjmat[x][y])!=1):
            continue
        temp[names[y]] = int(distance[x][y])                
    G[names[x]] = temp

#print G

fullCordsPath = ""

if izvan_dosega==1:
    fullCordsPath = fullCordsPath + str(coords[0][0])+","+str(coords[0][1])+";"+ str(lat)+","+str(lng)
else:
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


