#4 + 8 + 12 + 16 + .......... + n = ?
l = int(input("Enter the range = "))
sum = 0
for x in range(4, l+1, 4):
    sum += x
    if x != l:
        print(x, "+ ", end='')
    else:
        print(x, end='')

print(" =", sum)
