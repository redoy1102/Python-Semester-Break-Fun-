from random import randint
num = int(input("Enter a number = "))
ran = randint(1, 10)
if num == ran:
    print("Winner!")
    print("You pressed - ", num, "and random number is - ", ran)