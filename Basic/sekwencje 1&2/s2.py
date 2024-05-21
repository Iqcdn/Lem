#1
def formatFirstName( name ):
    if name.isalpha()==True:
        return name.title()
    return ""

#2
def formatHeight( feet, inches ):
    if feet.isnumeric() and ( ( len( feet ) > 1 and feet[0] != '0' ) or len( feet ) == 1 )  and inches.isnumeric() and ( ( len( inches ) > 1 and inches[0] != '0' ) or len( inches ) == 1 ) and 0 <= int( inches ) <= 12:  
        return feet + " ft " + inches
    return 0

#3
def clearText( s ):
    h=""
    for x in range(len(s)):
        if s[x].isalnum()==True:
            h+=s[x]
    return h

#4
"""
import math, balloons

def calcVolume():
    v=0
    for x in range( balloons.balloonsNumber() ):
        v += 4 / 3 * math.pi * balloons.getRadius( x ) ** 3 / 1000
    return v
"""
#5
import time
def displayTime():
    c = time.ctime()
    return c[11:19]+" "+c[0:3].upper()

#6
def findLongest( x ):
    h = 0
    for c in range(len(x)):
        if h <= len(x[c]):
            h = len(x[c])
    return h

#7
def findLongest(x):
    h= 0
    for c in range(len(x)):
        if h < len(x[c]):
            h = len(x[c])
            z = c
    return x[z]

#8
def testA( t1, t2 ):
    h=0
    c=0
    for x in t1:
        if x == "a":
            c+=1
    for l in t2:
        if l == "a":
            h+=1
    if c>=h:
        z = t1+t2
    else:
        z = t2+t1
    return z

#9
def chineseWeekDays(chineseDays, day):
    if day == "monday":
        x = 0
    elif day == "tuesday":
        x = 1
    elif day == "wednesday":
        x=2
    elif day == "thursday":
        x=3
    elif day == "friday":
        x = 4
    elif day == "saturday":
        x = 5
    elif day == "sunday":
        x = 6
    return chineseDays[x]

#10
import math

def calcAV( r ):
    return math.pi*r**2, (4/3)*math.pi*r**3

#11
def results( x ):
    x[2] = x[2]+273.15
    return x

#12
def goldenRaspberry( x ):
    x = sorted(x)
    return x

#13
def getHighest(x):
    x.sort(reverse = True)
    return x[0:3]

#14
def highLow( t1, t2 ):
    x = t1+t2
    x.sort(reverse = True)
    z = x[0:3]+x[-3:]
    return z

#15
def selectEven(t1, t2):
    for x in t2:
        if x % 2 == 0:
            t1.append(x)
    return t1

#16
def concHighest(t1, t2, t3):
    z = [max(t1), max(t2), max(t3)]
    return z

#17
def getBalance( t1, t2, t3 ):
    z = [sum(t1), sum(t2), sum(t3)]
    return z

#18
def temperature(x):
    x.insert(1, x[0]*9/5 + 32)
    return x

#19
def sumUp( args ):
    z = 0
    for x in range(5, len(args), 5):
        x+=z
        args.insert(x, sum(args[x-5:x])-max(args[x-5:x])-min(args[x-5:x]))
        z+=1
    args.insert(len(args), sum(args[-5:])-max(args[-5:])-min(args[-5:]))
    return args

#20
def optimize( operations, toRemove ):
    shift = 0
    for x in toRemove:
        del operations[ x - shift ]
        shift += 1
    return operations

#21
def delNumber( t1, t2 ):
    while t2 in t1:
        t1.remove( t2 )
    return t1

#22
def clearUnderscore(s):
    z=list(s)
    while "_" in z:
        z.remove("_")
    return z

#23
def convert( x ):
    y = list(x)
    for z in range(len(y)):
        if y[z] < 0:
            y[z] = 0
        elif y[z] > 10:
            y[z] = 10
    return x+y

#24
def isPalindrom(x):
    y = list(x)
    x.reverse()
    if x==y:
        return 1
    return 0

#25
def hourDataO3( data, hour ):
    return data[hour::24]

#26
def hasNotAnanym(x):
    z = [word[::-1] for word in x]
    print(z)
    
    to_remove = set()

    for i in range(len(x)):
        for j in range(len(z)):
            if z[j] == x[i]:
                to_remove.add(x[i])
                to_remove.add(z[j])
                print('1')

    x = [item for item in x if item not in to_remove]

    print(x)
    return x

#27
def sumUp( data, nr ):
    z = 0
    for x in range(len(data)):
        if nr in data[x]:
            z+=data[x][1]
    return z

#28
def maxTemp(x):
    l = []
    for z in range(len(x)):
        l.append(max(x[z]))
    return max(l)

#29