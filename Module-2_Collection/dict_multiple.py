"""stdata={}

n=int(input("Enter number of students:"))

for i in range(n):
    stid=int(input("Enter Student's ID:"))
    name=input("Enter Student's Name:")
    city=input("Enter Student's City:")
    stdata[stid]={"nm":name,"ct":city}

#print(stdata)
for j in stdata.items():
    print(j)"""

# ---------------------------------------------------- #
stdata={}
data=[]
n=int(input("Enter number of students:"))
for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter a Name:")
    stdata["id"]=id
    stdata["name"]=name
    data.append(stdata)

print(data)