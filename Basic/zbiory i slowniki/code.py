#1
def joinData( x ):
    l=int(x[1])/100
    z = str(x[0])+": "
    return str(z)+str(l)

#2
def selectAndSum( x ):
    s=0
    for y in x.split(', '):
        if y.isnumeric():
            s += int(y) 
    return s

#3
def brutto( x ):
    k = float(x[0:-2])*1.08
    return str(round(k, 2))+x[-2:]

#4
import time

def englishBreakfast(x):
    for item in x:
        s = time.mktime(time.strptime(item[1], "%Y%m%d"))
        days_passed = (time.time() - s) // 86400
        item[1] = days_passed
    return x


#5
def countDistinct( x ):
    return len(set(x))

#6
def setSet( x ):
    return {z[0] for z in x}

#7
def clearData( x, y ):
    return {z for z in x if z[1]<y}

#8
def isEqual( x, y ):
    return x==y


#9
def getEmails(s1, s2):
    emails = {email for item in s1 + s2 if (email := item[0]) and item[1]}
    return emails


#10
def getFeatures( x ):
    new = set(x[0])
    for i in x:
        new &= set(i)
    return new

#11
def findSuspects(x, y, z):
    return  ( set(x) & set(y) ) | ( set(x) & set(z) ) | ( set(y) & set(z) )

#12
def getCustomers( myBase, theirBase ):
    x = set(myBase)
    y = set(theirBase)
    return y.difference(x)

#13
def mutation1( m1, m2 ):
    return set(m1)^set(m2)


#14
def findName( d, n ):
    for x in d:
        if x.get("NIP") == n:
            return x.get("name")
    return "Data not found"


#15
def complete( x ):
    for k in x:
        if x.get(k) == "":
            x[k]=False
    return x

#16
def convert( x ):
    k={}
    for z in x:
        k[str(z)]=x[z]
    return k

#17
import time
def update(x):
    ts_limit = time.time() - 5 * 365 * 24 * 60 * 60
    y = dict(x)
    to_remove = []
    for key in y:
        data = y[key][1]
        timestamp = time.mktime(time.strptime(data, "%Y%m%d"))
        if timestamp < ts_limit:
            to_remove.append(key)
    for key in to_remove:
        y.pop(key)
    return y

#18
def setDict( x ):
    prime = ( 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 )
    y = dict.fromkeys(x)
    for z in y:
        if z in prime:
            y[z] = "prime"
    return y

#19
def compareKeys( x, y ):
    if x.keys() == y.keys():
        return 1
    return 0

#20
def checkPrisoners( t, i ):
    x = set( t.items() )
    y = set( i.items() )
    return y.issuperset(x)


#21
def countChars( s ):
    d = dict.fromkeys( s.upper() )
    for x in d:
        d[x.capitalize()] = s.upper().count(x)
    return d

'''
#22
import delivery
def getTemp( x ):
    return delivery.get(x)['data']['engineTemp']

#23
import delivery
def totalRoute():
    y = delivery.robots()
    z = 0
    for x in y:
        z += delivery.get(x)['data']['distanceToday']
    return z

#24
import delivery
def chargeFloat():
    y = delivery.robots()
    z = set()
    for x in delivery.robots():
        if delivery.get( x )['data']['batteryCharge'] < 25:
            delivery.charge(x)

#25
import delivery
def keyPoints():
    s = set( delivery.get( delivery.robots()[0] )['route'] )
    for x in delivery.robots():
      s &= set( delivery.get(x)['route'] )
      if s == set():
        return 0
    return s
'''