#1 + 2 + 3 + 4 + ........... + n = ?
l = int(input("Enter the range = "))
sum = 0
for x in range(1, l+1):
    sum += x
    if x != l:
        print(x, "+ ", end='')
    else:
        print(x, end='')

print(" =", sum)
