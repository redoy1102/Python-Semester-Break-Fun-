"""language = {"c", "c++", "JS", "Python", "JS"}
language.add("zsdfsdfdsfsdfsdds")
print(language)"""
"""thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
tropical.update(thisset)
print(tropical)"""
"""names = {"Fuad", "Bristy", "Riya", "Tonni", "Badol"}
prize = names.pop()
print(names)
print("Winner = " + prize)"""
"""thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)"""
"""set1 = {"a", "b", "c", "c", "c", "c"}
set2 = {1, 2, 3}

print(set1)
print(set2)
set3 = set1.union(set2)
print(set3)"""
"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x)
x.intersection_update(y)
print(x)"""
"""x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)"""
"""num = [1, 2, 3, 9]
numb = [1, 9, 4, 5]
n, nm = set(num), set(numb)
h = n.intersection(nm)
print(h)"""

n = {1, 2, 3, 4, 5, 6}
nb = {7, 8, 9, 10}
res = n.isdisjoint(nb)
print(res)


