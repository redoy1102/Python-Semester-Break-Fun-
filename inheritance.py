list1 = []
list2 = []
for x in range(5):
    n = int(input())
    list1.append(n)

print("List - 1: ", end='')
for x in range(len(list1)):
    print(list1[x], " ")







"""class Person:
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName

    def printName(self):
        print(self.firstName, self.lastName)


class Student(Person):
    def __init__(self, fName, lName, gy):
        super().__init__(fName, lName)
        self.graduation = gy

    def msg(self):
        print("Welcome", self.firstName, self.lastName, "Your graduation year is", self.graduation)


x = Student("sdss", "ssdsd", 2024)
x.msg()
"""