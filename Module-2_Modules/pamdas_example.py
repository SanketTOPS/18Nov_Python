import pandas

stdata={
    "id":[101,102,103],
    "name":["Sanket","Nirav","Ashok"],
    "City":["Rajkot","Baroda","Ahmedabad"]
}
#print(stdata)

x=pandas.DataFrame(stdata)
#print(x)
print(x.iloc[0])
