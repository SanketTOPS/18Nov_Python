import re

mystr = "This is python!"

x = re.search("This", mystr)
print(x)


if x:  # TRUE
    print("Match done!")
else:
    print("Error!")
