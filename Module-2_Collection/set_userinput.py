'''data=set()

n=int(input("Enter any number:"))

for i in range(n):
    x=input("Enter any Value:")
    data.add(x)

#print(data)
print(list(data))'''

# ----------------------- #

data=[]
n=int(input("Enter number of students:"))

for i in range(n):
    x=input("Enter student's name: ")
    data.append(x)

print(data)
print(set(data))