myfile=open('hello.txt','a') #append mode

id=input("Enter an ID:")
name=input("Enter a Name:")

myfile.write(f"\nID:{id}\nName:{name}")