import pandas

mydata=({
    'ID':[1,2,3,4,5],
    'Name':['Sanket','Nirav','Ashok','Hitesh','Prasiddh']
})

pn=pandas.DataFrame(mydata)

pn.to_excel('stdata.xlsx','tshee-1',index=False)