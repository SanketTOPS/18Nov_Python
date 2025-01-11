myfile=open('stdata.txt','a') #append mode

stid=input("Enter an ID:")
stnm=input("Entger a Name:")

myfile.write(f"\nID:{stid}\nName:{stnm}")

