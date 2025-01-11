myfile=open('new.txt','a')

def stdata():
    stid=input("Enter an ID:")
    stnm=input("Enter a Name:")
    myfile.write(f"ID:{stid}\nName:{stnm}\n--------------\n")

n=int(input("Enter number of students:"))

for i in range(n):
    stdata()