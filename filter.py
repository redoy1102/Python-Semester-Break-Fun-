# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 45, 89, 63, 74, 85, 96, ]
# even = list(filter(lambda x: x % 2 == 0, numbers))
# ec = len(even)
# print("Even numbers:", even)
# print("Total even numbers =", ec)
#
# odd = list(filter(lambda x: x % 2 != 0, numbers))
# oc = len(odd)
# print("Odd numbers:", odd)
# print("Total odd numbers =", oc)
#

numbers = []
for x in range(5):
    n = int(input())
    numbers.append(n)
re = [x for x in numbers if x % 2 != 0]
#re = list(filter(lambda x: x % 2 != 0, numbers))
print(re)
