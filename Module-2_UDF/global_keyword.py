a=23

print("A:",a)

def getval():
    global a
    a+=1
    print("A:",a)

getval()