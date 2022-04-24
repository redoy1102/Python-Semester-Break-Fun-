"""thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))"""

"""names = ["Fuad", "Redoy", "MD", "Bristy", "Islam", "Riya", "Tonni", "Badol"]
names[0:3] = ["Md", "Fuadul", "Islam"]
names[3:5] = ["Redoy", "Bristy"]
print(names)"""

"""thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
"""

"""names = ["Md", "Fuadul", "Islam"]
names.insert(3, "Redoy")
names.append("Bristy")
print(names)"""

# names = ["MD", "Fuadul", "MD", "Fuadul"]
# for i in range(1, len(names)):
#     print(i+1, " - ", names[i])
# i = 0
# for i in range(11):
#     print(i)
#     i = i + 2

"""food = ["Fried Rice", "Chicken Ball", "Soup"]
# i = 0
# while i < len(food):
#     print(food[i])
#     i = i + 1
[print(x) for x in food]"""
"""food = ["Fried Rice", "Chicken Ball", "Soup", "Chicken Khicuri"]
newList = []
for x in food:
    if "c" in x:
        newList.append(x)


print(newList)"""

"""name = ["fuad", "fun", "Redoy"]
newList = []
for x in name:
    if "f" == x[0]:
        newList.append(x)


for x in newList:
    print(x)"""
"""sum = 0
for x in range(101):
    if x % 2 == 0:
        sum += x


print(sum)"""

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x.upper() for x in fruits]
print(newList)"""

"""names = ["a", "b", "d", "B", "A", "c", "d", "r"]
names.sort()
print(names)
names.reverse()
print(names)"""

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
l = []
for x in fruits:
    l.append(x)


print(l)"""

"""fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = fruits.copy()
print("New list = ", newList, "\n")"""

"""list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)

print(list1)"""

txt = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,"
print(txt.count("amet"))
print(txt.count("consectetuer"))


