#2 + 4 + 6 + 8 + .......... + n = ?
l = int(input("Enter the range = "))
sum = 0
for x in range(2, l+1, 2):
    sum += x
    if x != l:
        print(x, "+ ", end='')
    else:
        print(x, end='')

print(" =", sum)
