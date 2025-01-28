import re

mystr = "This is Python!48546"

# x = re.findall("\w", mystr)
# x = re.findall("\W", mystr)
# x = re.findall("\s", mystr)
# x = re.findall("\S", mystr)
# x = re.findall("\d", mystr)
x = re.findall("\D", mystr)
print(x)
