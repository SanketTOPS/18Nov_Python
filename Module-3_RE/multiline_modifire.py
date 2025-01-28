import re

mystr = "This is Python!79"

# x = re.findall("^This", mystr)
x = re.findall("78$", mystr)
print(x)

if x:
    print("Match done!")
else:
    print("Error!")
