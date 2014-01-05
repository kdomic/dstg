import cPickle
coords = cPickle.load(open('coords.p', 'rb'))
adjmat = cPickle.load(open('adjmat.p', 'rb'))
distance = cPickle.load(open('distance.p', 'rb'))
names = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','Z','X','Y','W','Q','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AR','AS','AT','AU','AV','AZ','AX','AY','AW','AQ']

def getIndex(let):
    for i in range(0,len(names)):
        if(let==names[i]):
            return i

def dodaj():
    a = getIndex(raw_input("Vrh a: "))
    b = getIndex(raw_input("Vrh b: "))
    adjmat[a][b] = 1
    adjmat[b][a] = 1
    cPickle.dump(adjmat , open('adjmat.p', 'wb'))
    return

def makni():
    a = getIndex(raw_input("Vrh a: "))
    b = getIndex(raw_input("Vrh b: "))
    adjmat[a][b] = 1
    adjmat[b][a] = 1
    cPickle.dump(adjmat , open('adjmat.p', 'wb'))    
    return

#main
while 1==1:
    print
    print '1. Dodaj vezu'
    print '2. Makni vezu'
    temp = int(raw_input('Povezani:'))
    if(temp==1):
        dodaj();
    elif(temp==2):
        makni();


