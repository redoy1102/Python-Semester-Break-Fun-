str = "string"
length = len(str)
if str[length-1] == "g" and str[length-2] == "n" and str[length-3] == "i":
    print(str + "ly")
elif len(str) >= 3:
    print(str + "ing")
else:
    pass

