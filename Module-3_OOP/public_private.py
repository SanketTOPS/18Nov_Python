class studinfo:
    __stid = 32  # private
    __stnm = "Ashok"  # private

    def ___getdata(self):  # private
        print("This is getdata!")
        print("ID:", self.__stid)
        print("Name:", self.__stnm)

    def prindata(self):  # public
        self.___getdata()


st = studinfo()
# print(st.stid)
# print(st.stnm)

# print(st.__stid)
# print(st.__stnm)

# st.getdata()
# st.___getdata()

st.prindata()
