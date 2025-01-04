maths=int(input("Enter maths subject marks:"))
che=int(input("Enter chemistry subject marks:"))
phy=int(input("Enter physics subject marks:"))

total=maths+che+phy
print("Total Marks: ", total)
pr=total/3

if pr > 90:
    print("A Grad:..")
elif pr > 80:
    print("B grad...")
elif pr> 70:
    print("c grad....")
else:
    print("d grad...")