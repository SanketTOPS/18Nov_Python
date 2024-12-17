while True:
    n1=int(input("Enter number1:"))
    n2=int(input("Enter number2:"))
    print("-------Welcome to Calc App-------")
    print("1:Add")
    print("2:Sub")
    print("3:Mul")
    print("4:Div")
    print("5:Exit")
    choice=int(input("Select any one option: "))

    if choice==1:
        print("\nAdd:",n1+n2)
    elif choice==2:
        print("\nSub:",n1-n2)
    elif choice==3:
        print("\nMul:",n1*n2)
    elif choice==4:
        print("\nDiv:",n1/n2)
    else:
        break
