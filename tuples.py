"""names = ("Fuad", "Bristy", "Abbu", "Ammu", "Riya")
n = list(names)
n[0] = "Md Fuadul Islam Redoy"
names = tuple(n)
print(type(names))
print(names)"""
"""
names = ("Fuad", "Bristy", "Abbu", "Ammu")
ri = ("riya", "Elmi")

names += ri
print(names)"""
"""fruits = ("apple", "banana", "cherry")
green, yellow, red = fruits
print(green)
print(yellow)
print(red)"""
"""names = ("fuad", "banana", "cherrya, ", "banana", "cherry")
a, b, *c = names
print(a)
print(b)
x = tuple(c)
print(x)"""
"""num = []
for x in range(3):
    num.append(input())

[print(int(x), end=' ') for x in num]"""
"""
thistuple = ("apple", "banana", "cherry")
[print(thistuple[i]) for i in range(len(thistuple))]"""
fruits = ("apple", "banana", "cherry", "banana")
print("Index = %d"%fruits.index("banana"))
print("Total number of time banana = %d"%fruits.count("banana"))




