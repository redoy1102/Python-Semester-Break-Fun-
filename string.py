"""
#upper case
name = "Md Fuadul Islam Redoy"
upper = name.upper()
print("Upper case of " + name + " = " + upper)
"""

"""
#Lower case
name = "MD FUADUL ISLAM REDOY"
lower = name.lower()
print("Lower case of " + name + " = " + lower)"""

"""
#strip fun
msg = " Hey python "
wos = msg.strip()
print(wos)"""

"""
#replace
name = "Guad"
rName = name.replace("G", "F")
print(rName)"""

"""
#split
name = "a,b,c,d"
s = name.split(",")
print(s)
print(type(s))"""

"""
#capitalize
name = "md fuadul islam redoy"
capital = name.capitalize()
print(capital)"""

"""#casefold()
name = "Md Fuadul Islam Redoy"
name1 = "FUAD"
print(name.casefold(), name1.casefold())"""

"""#center
txt = "banana"
c = txt.center(20, "a")
print(c)"""

"""
#count fun
txt = "aaaaa"
c = txt.count("a", 3)
print(c)"""

"""
#endswith fun
txt = "Fuad."
ch = txt.endswith(".")
print(int(ch))"""

"""#endswith fun
name = "20103046@iubat.edu"
c = name.endswith("@iubat.edu", -10)
if c:
    print("Your edu mail is right!")
eduMail = input("Enter your edu mail: ")
check = eduMail.endswith("010", 1, 4)
if check:
    print("Valid edu mail for 2010 batch.")
else:
    print("Oops! Invalid edu mail for 2010 batch.\nEdu mail should start by 2010 for this batch.\n")
"""

# name = "Md Fuadul Islam Redoy"
# print(name[0:9])

"""#isalnum fun
txt = "Fuad01232"
print(txt.isalnum())"""

"""
num = "0123"
print(num.isdecimal())"""

"""
txt = "1236Fuadul"
print(txt.isdigit())"""

"""#partition fun
msg = "My Name is Md Fuadul Islam Redoy"
print(msg.partition("Fuadul"))"""

"""#rjust fun
msg = "amar bou"
print(msg.rjust(10), "sdfsdfs")"""

"""txt = "50"
x = txt.zfill(12)
print(x)"""

"""
a = "fuad"
print(a.zfill(10))"""

"""
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
print(bool(12))
"""
x, y = [float(x) for x in input().split()]
print(x)
print(y)


