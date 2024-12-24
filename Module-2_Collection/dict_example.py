stdata={'id':101,
        'name':'sanket',
        'city':'rajkot'}



"""print(stdata)
print(stdata['name'])
print(stdata['city'])
print(stdata.get('id'))"""

#----------------------------------#
#print(stdata)
#print(len(stdata))
#print(stdata.keys())
#print(stdata.values())

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""

#--------------------------------#
"""print(stdata)
stdata['id']=102 #update value
stdata['sub']='Python' #new value
print(stdata)"""

#print(stdata)
#stdata.pop('name')
#del stdata['city']
#stdata.clear()
#print(stdata)

# ------------------------- #
print(stdata)

newstdata=stdata.copy()
print(newstdata)
