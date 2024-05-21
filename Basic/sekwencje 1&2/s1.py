#1
name = "Bill Munny"
print( name[2] )

#2
def element( text, number ):
    return text[number]

#3
def sum_len(x, y):
    return len(x)+len(y)

#4
def diff_len(x, y):
    d = len(x)-len(y)
    if d <=0:
        d *= -1
    return d

#5
def get_month(x):
    return x[2:4]

#6
def get_year( date ):
    if int(date[0:4]) >= 1901 and int(date[0:4]) <= 2000:
        return str(date[0:4])
    else:
        return date[4:8]

#7
def add_dollar( text ):
    return "$$"+text[2:-2]+"$$"

#8
def formatName( name ):
    x = name.index("_")
    return name[0:x]+name[x+1:].title()

#9
def get_initials( name ):
    return name[0].title()+name[name.index(" ")+1]

#10
def get_index( value, text ):
    if value in text:
        return text.index(value)
    return False

#11
def cleanText( text ):
    return text.replace("$", "")

#12
def get_dollar( text ):
    x = text.count("$")
    return x*"$"

#13
def get_percentage( value, text ):
    return text.count(value)/len(text)*100

#14
def hasDuplicates( text ):
    z = ""
    for x in text:
        if x == z:
            return True
        z = x
    return False

#15
text = """I'm glad to say we've got the go-ahead to lend you the money you required. We will, of course,
need for security the deed to your house, the deed to your aunt's house, of your wife's parents' house, 
and of your granny's bungalow. And we will, in addition, need a controlling interest in the stock of 
your new company, unrestricted access to your private bank accounts, the deposit of your three children 
in our vaults as hostages, and a full legal indemnity in case of any embezzlement carried out against 
you by members of our staff during the normal course of their duties."""
for x in "AEIOUY":
    s = text.count(x)+text.count(x.lower())
    print(x, s)

#16
def maxOrd( text ):
    m = 0
    for x in text:
        if ord(x) > m:
            m = ord(x)
    return m

#17
def encrypt( message ):
    d = ""
    for x in message:
        d+= chr(ord(x)*2)
    return d

#18
def decrypt( message, key):
    d = ""
    for x in message:
        d+= chr(int(ord(x)/key))
    return d

#19
def prize( days ):
    f=0
    d=0
    for x in range(days):
        f += x+1
        d += f
    return d

#20
def encrypt( message ):
    h = ""
    for x in range(len(message)):
        h += str(chr(ord(message[x])+x))
    return h

#21
"""
def charsInDoc(a, b):
    f=0
    for x in range(a,b+1):
        f+=charsOnPage(x)
    return f
"""
#22
def reverse(bez):
    g=""
    for x in range(len(bez)-1, -1, -1):
        g+=str(bez[x])
    return g
reverse("abccd")

#23
def oddChars(bez):
    g=""
    for x in range(1, len(bez), 2):
        g+=str(bez[x])
    return g