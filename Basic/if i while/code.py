# 1
print( 5 == 3 )

# 2
print(2 ** 2 != 2 * 2)
print(5**2 < 2**5)
print("A" == "a")

# 3
print(2 > 3 or 10 > 5)
print(2/3 > 1 or 2//3 == 0)
print(1 == 12 ** 0 and str(1) == "1" )

# 4
def setSign( x ):
    value = 1
    if x>0:
        return value
    return value-2

# 5
def isWeekend( x ):
    value = "Bleeee!!!"
    if x in (5, 6, 7):
        return "Weekend!!!"
    return value

# 6
def whoWins( coyote, roadrunner ):
    if coyote>roadrunner:
        winner = "Coyote"
    else:
        winner = "Roadrunner"
    return winner

# 7
def constValue( constName ):
    if constName == "Pi":
        value=3.14159
    elif constName == "e":
        value=2.71828
    elif constName == "gamma":
        value=0.57721
    elif constName == "phi":
        value=1.61803
    return value

# 8
def dayOfWeek(x):
    if x ==1:
        y ="Monday"
    elif x==2:
        y="Tuesday"
    elif x==3:
        y="Wednesday"
    elif x==4:
        y="Thursday"
    elif x==5:
        y="Friday"
    elif x==6:
        y="Saturday"
    elif x==7:
        y="Sunday"
    else:
        y="wrong value"
    return y
print(dayOfWeek(6))
del dayOfWeek

# 9
def isEven(x):
    if x%2:
        return False
    return True

# 10
def setValve(x):
    if x <= 100:
        return 0
    elif 100 < x <= 200:
        return 1
    elif 200 < x <= 400:
        return 2
    elif 400 < x <= 600:
        return 3
    elif 600 < x <= 800:
        return 4
    elif x > 800:
        return 5

# 11
def setPower( pm25, pm10 ):
    if pm25<=12 and pm10<=20:
        return 0
    elif 12<=pm25<=36 or 21<=pm10<=60:
        return 1
    elif 37<=pm25<=60 or 61<=pm10<=100:
        return 2
    elif 61<=pm25<=84 or 101<=pm10<=140:
        return 3
    elif 85<=pm25<=120 or 141<=pm10<=200:
        return 4
    elif pm25>120 or pm10>200:
        return 5

# 12
#your code
def setAlarm(x, y):
    if 6<=x<22 and 1<=y<=4 :
        return False
    elif 6<=x<18 and y==5:
        return False
    elif 6<=x<14 and y==6:
        return False
    return True


# 13
#your code
def checkTriangle(z, x, c):
    if z+x>c and x+c>z and z+c>x:
        return True
    return False
"""
# 14
def printer_ctrl():
    while pc_leftover() > 5:
        pc_cut()
        pc_position()
        pc_print()
    pc_pause()
"""
"""
# 15
def play_anthem():
    note = get_note()
    while note >0:
        play(note)
        note = get_note()
"""
"""
# 16
def compressor( set_pressure ):
    x = get_pressure()
    while x<set_pressure:
        pump()
        x = get_pressure()
    return 0
"""
"""
# 17
def shooting():
    x = isBall()
    while x is True:
        shoot()
        x = isBall()
"""
"""
# 18
def route():
    while True:
        f = front()
        l = left()
        r = right()
        if front()>=500 and l>=500 and r>=500:
            break
        elif f >100:
            move()
        elif f<=100 and r>=200:
            turnR()
        elif f<=100 and l>=200:
            turnL()
"""
# 19
x = 1
while x <= 10:
    print(x)
    x +=1

# 20
def maxPeriod( debt, equity ):
    x = 0
    while debt <= equity:
        debt *= 1.035
        x+=1
    return x

# 21
def prize(day, month):
    x = 0
    if month == 2:
        while day<=29:
            x += day
            day+=1
    elif month in (1, 3, 5, 7, 8, 10, 12):
        while day<=31:
            x += day
            day+=1
    else:
        while day<=30:
            x += day
            day+=1
    return x