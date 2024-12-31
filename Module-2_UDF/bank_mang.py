acnum=0
acnm=''
actype=''

def acount_opening():
    global acnum
    global acnm
    global actype
    acnum=input("Enter an A/c Number:")
    acnm=input("Enter A/c holder Name:")
    actype=input("Enter A/c type:")


def statements():
    print("A/c No.:",acnum)
    print("A/c Holder:",acnm)
    print("A/c Type:",actype)

acount_opening()
statements()
    