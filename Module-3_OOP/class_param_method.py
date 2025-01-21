class studinfo:
    def getdata(self, id, name):
        print("ID:", id)
        print("Name:", name)


st = studinfo()
# st.getdata(101, "Sanket")

stid = input("Enter an ID:")
stnm = input("Enter a Name:")
st.getdata(stid, stnm)
