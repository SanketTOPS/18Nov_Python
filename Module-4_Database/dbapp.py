import sqlite3

try:
    db = sqlite3.connect("mydb.db")
    print("Database created/connected!")
except Exception as e:
    print(e)


# Create a Table
create_tbl = (
    "create table studinfo(id integer primary key autoincrement,name text,city text)"
)

try:
    db.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)


# Insert Data
"""insert_data = "insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('ashok','surat'),('hitesh','morbi'),('mahesh','rajkot')"
try:
    db.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
"""

"""update_data = "update studinfo set name='pritesh',city='rajkot' where id=9"
try:
    db.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""


# Delete Data
"""n = 5
delete_data = f"delete from studinfo where id={n}"
try:
    db.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


# Show Data
cr = db.cursor()
show_data = "select * from studinfo"
try:
    cr.execute(show_data)
    data = cr.fetchall()
    # data = cr.fetchmany()
    # data = cr.fetchone()
    # print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)
