myfile=open('temp.txt','w')

id=input("Enter an ID:")
name=input("Enter a Name:")

"""myfile.write(id)
myfile.write(name)"""

myfile.write(f"ID:{id}\nName:{name}")