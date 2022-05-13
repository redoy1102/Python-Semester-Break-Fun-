file = open("msg.txt", "r")
text = file.read()
print(text)
print("The size of the file  = ", len(text))
file.close()

