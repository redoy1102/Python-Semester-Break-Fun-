# 1*1 + 2*2 + 3*3 + ........ + n*n = Sum
inpt = int(input("Enter range = "))
sum = 1
for x in range(2, inpt + 1, 1):
    sum += 1 / x

print("%.2f" % sum)
