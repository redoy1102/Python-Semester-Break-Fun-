family = {
    "name": "fuad",
    "age": 22,
    "study": "iubat"
}
family.update({"nick": "redoy"})
res = family.popitem()
print(family)
print(res)















"""thisDict = {
    "name": "Fuad",
    "age": 22
}
print(thisDict["name"])"""
"""family = {
    "child1": {
        "name": "Fuad",
        "age": 22
    },
    "child2": {
        "name": "Bristy",
        "age": 21
    },
    "child3": {
        "name": "Riya",
        "age": 17
    }
}
print(family["child1"])"""
"""k = ("key-1", "key-2", "key-3")
v = 1, 2, 3
res = dict.fromkeys(k)
print(res)"""
"""thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
thisdict.update({"color": "green"})
print(thisdict)"""
"""year = int(input())

info = {
    "name": "Fuad",
    "age": 22,
    "y": year
}
print(info)

req = int(input("Do you want change your age ?\nPress-1 for yes.\nPress-2 for no.\nPress here: "))
if req == 1:
    newAge = int(input("Enter age: "))
    info.update({"y": newAge})
    print(info)
else:
    print("OK!")"""
"""myInfo = {
    "name": "Md Fuadul Islam Redoy",
    "university": "IUBAT",
    "dept": "BCSE",
    "age": 22,
    "hobby": "programming"
}
x = myInfo.keys()
print("Keys: ", x)"""
"""car = {
    "name": "Tesla",
    "color": "red"
}
item = car.items()
print(item)"""
"""b = car.keys()
v = car.values()
print(b)
print(v)

car["quantity"] = 1000
a = car.keys()
print(a)"""
