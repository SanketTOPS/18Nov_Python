myfile=open('new.txt','w')

print(myfile.read())
#print(myfile.readline())
#print(myfile.readlines())
#print(myfile.readlines()[0])
#print(myfile.readlines()[0:3])

"""for i in myfile:
    print(i)
    """

if myfile.readable():
    print("Yes...")
else:
    print("Error!")
