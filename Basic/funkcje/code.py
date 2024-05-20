#1
def display_greetings():
    print( "Hello!" )
print('And now for something completely different.')
del display_greetings

#2
def display_greetings():
    print( "Hello!" )
    print('And now for something completely different.')
del display_greetings

#3
def display_greetings():
    print( "Hello!" )
    print( "And now for something completely different." )
display_greetings()
del display_greetings

#4
def display_self_congratulations():
    print( "I am" )
    print( "really great" )
    print( "in calling" )
    print( "functions!" )
display_self_congratulations()
del display_self_congratulations

#5
#your first function in Python
def great_moment_in_human_history():
    print("My first function in Python")
del great_moment_in_human_history

#6
#your second function in Python
def yet_another_great_moment():
    print("My second function in Python")
yet_another_great_moment()
del yet_another_great_moment

#7
#your function
def display():
    print("Eric Idle")
display()
del display

#8
def display( number ):
    print( number )
display(3.14)
del display

#9
def display( some_text ):
    print( some_text )
display("And now for something completely different")
del display

#10
def display_area( x, y ):
    print( x * y )
display_area(3, 8)
del display_area

#11
def simple_per(a, b, c):
    print(a+b+c)
simple_per(23, 9, 8)
del simple_per

#12
def andNow():
    return "And now something completely different"
print(andNow())
del andNow

#13
def add(x, y):
    return x+y
print(add(2, 3))
del add

#14
def multiply(x, y):
    return x*y
print(multiply("Ole!", 10))
del multiply

#15
def calc_area(x, y):
    print("calculating area of a rectangle ...")
    return x*y
area = calc_area(17, 36)
print(area)
del calc_area

#16
def plus_tax(x):
    return x*1.23
del plus_tax

#17
def C_to_F(x):
    return x*9/5+32
del C_to_F

#18
def GallonsToLiters(x):
    return x/0.26417
del GallonsToLiters

#19
def calcCirc(x):
    return x*2*3.1416
del calcCirc

#20
def calcArea(x):
    return x*x*3.1416
del calcArea

#21
def calcArea( r ):
    return 3.1416 * r**2    
def calcVolume(x, h):
    return calcArea(x)*h
del calcArea, calcVolume

#22
def to_time(x, y, z):
    return z*10000+y*100+x
print(to_time(23, 42, 60))
del to_time

#23
def to_time(x):
    z = int(x)/3600
    h = int(x)%3600/60
    k = int(x)%3600%60
    return int(z)*10000+int(h)*100+int(k)
del to_time

#24
def plus_tax(x, y):
    y /= 100
    return x*(y+1)
del plus_tax
