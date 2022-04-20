#1: start
#2: Take two input
#3: Convert in int type of two inputs
#4: Calculate sum, sub, div
#5: Print all result
#6: End

fn = input("Enter first number = ")
sn = input("Enter second number = ")
intFn, intSn = int(fn), int(sn)

sum, sub, div = (intFn + intSn), (intFn - intSn), (intFn / intSn)
print("Summation of ", intFn, "and ", intSn, " = ", sum)
print("Subtraction of ", intFn, "and ", intSn, " = ", sub)
print("Division of ", intFn, "and ", intSn, " = ", div)

