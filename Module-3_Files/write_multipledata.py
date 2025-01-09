import datetime

myfile=open('stdata.txt','a')

n=int(input("Enter number of students:"))

cdate=datetime.datetime.now()

for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter a Name:")
    myfile.write(f"Created:{cdate}\nID:{id}\nName:{name}\n---------------\n")