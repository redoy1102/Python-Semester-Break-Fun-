def add():
    num1, num2 = input("Enter a number = "), input("Enter another number = ")
    iNum1, iNum2 = int(num1), int(num2)
    addition = iNum1 + iNum2
    return addition


res = isinstance(add(), int)

if res:
    print("Yes this is an int value")
else:
    print("No")
