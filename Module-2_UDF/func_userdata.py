def getdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)

n=int(input("Enter number of stuednts:"))

for i in range(n):
    stid=input("Enter an ID:")
    stnm=input("Enter a Name:")
    stct=input("Enter City:")

    getdata(stid,stnm,stct)