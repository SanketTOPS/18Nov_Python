import keyword

x=keyword.kwlist
"""print(x)

for i in x:
    print(i)"""

k=input("Enter any keyword:")

if k in x:
    print("Yes...This is keyword")
else:
    print("No..This is not a keyword!")