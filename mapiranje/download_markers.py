import urllib, json
import pprint
import time
import cPickle

coords = [[45.557986854,18.713400671],[45.557994366,18.710986682],[45.558283584,18.710772106],[45.557962439,18.708891877],[45.557862902,18.708492228],[45.557782146,18.708792635],[45.557273191,18.710745284],[45.556980211,18.712043473],[45.556108774,18.715680548],[45.557231873,18.715720781],[45.557983098,18.715793201],[45.558786896,18.715862938],[45.559624488,18.715954134],[45.560105252,18.715321132],[45.559819799,18.715133378],[45.560383192,18.715927311],[45.560916532,18.717901417],[45.560555965,18.719006487],[45.560345632,18.718883106],[45.560330609,18.718453952],[45.559808531,18.718207189],[45.559870504,18.718893835],[45.558863895,18.719151327],[45.558800043,18.717922875],[45.558766238,18.716941186],[45.557748341,18.717912146],[45.557973707,18.718593427],[45.557256288,18.716871449],[45.557320143,18.719381997],[45.556313488,18.719682404],[45.555002556,18.720256397],[45.555922841,18.716731974],[45.556099384,18.716839263],[45.557962439,18.717981213],[45.558120195,18.707424038]]
distance = []
adjmat = []

num = 0
num_max = len(coords)
error = 0

print "start"

for a in coords:
    dis_temp = []
    adj_temp = []
    for b in coords:
        dis_temp.append(['a','b']);
        adj_temp.append(0);
    distance.append(dis_temp);
    adjmat.append(adj_temp);

for a in range(0,num_max):    
    print 100*num/num_max
    for b in range(0,num_max):
        error = 0
        while error>=0:
            if(error>0):
                time.sleep(1.0)
            if(error>5):
                print "!!! RESRATRIRAJ IP !!!"
                time.sleep(60.0)
            if(a==b):
                distance[a][b] = 0
            if(a<b):
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
                else:
                    error = error + 1
            else:
                error = -1
    num = num+1

cPickle.dump(coords , open('coords.p', 'wb'))
cPickle.dump(distance , open('distance.p', 'wb'))
cPickle.dump(adjmat , open('adjmat.p', 'wb'))

print distance
print
print "-----"
print adjmat
print
print "end"

