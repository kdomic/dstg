import urllib, json
import pprint

URL2 = "http://maps.googleapis.com/maps/api/directions/json?origin=45.55797, 18.710975&destination=45.554991, 18.716273&sensor=false"
googleResponse = urllib.urlopen(URL2)
jsonResponse = json.loads(googleResponse.read())
test = json.dumps([s['legs'][0]['distance']['value'] for s in jsonResponse['routes']], indent=3)
test =  test.replace("[", "").replace("]", "").replace(" ", "").strip('\n')

coords = [[45.557987323,18.713408717],[45.557996713,18.710986682],[45.557275538,18.710737237],[45.557776981,18.708792635],[45.557963848,18.708891877],[45.557864311,18.708477476],[45.558108457,18.707418003],[45.558273725,18.707624533],[45.558438992,18.708099284],[45.558292505,18.710223594],[45.560106660,18.715325156],[45.559742332,18.715915242],[45.558889718,18.715920606],[45.557984506,18.715797224],[45.557237038,18.715732851],[45.556117695,18.715689936],[45.556831373,18.712600031]]
distance = []

num = 1
num_max = len(coords)
print "start"
for a in coords:
    dis_temp = []
    for b in coords:        
        URL2 = "http://maps.googleapis.com/maps/api/directions/json?origin="+str(a[0])+","+str(a[1])+"&destination="+str(b[0])+","+str(b[1])+"&sensor=false"
        googleResponse = urllib.urlopen(URL2)
        jsonResponse = json.loads(googleResponse.read())
        test = json.dumps([s['legs'][0]['distance']['value'] for s in jsonResponse['routes']], indent=3)
        test =  test.replace("[", "").replace("]", "").replace(" ", "").strip('\n')
        dis_temp.append(test);
        #print a
        #print b
        #print test
        #print ''
        #print URL2
    distance.append(dis_temp);
    num = num+1
    print 100*num/(num_max*1.0)
    
print distance
print "end"
