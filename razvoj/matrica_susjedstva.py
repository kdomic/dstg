fread = open('DATA.CSV.csv','r')
data = []
for line in fread:
    data.append(line.strip().split(','))
print data
