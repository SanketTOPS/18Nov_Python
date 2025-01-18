class studinfo:
    stid = 12
    stnm = "Sanket"

    def printdata(self):
        print("This is printdata!")

    def getsum(self, a, b):
        print("Sum:", a + b)


# Object of class
st = studinfo()
print("ID:", st.stid)
print("Name:", st.stnm)
st.printdata()
st.getsum(34, 76)
