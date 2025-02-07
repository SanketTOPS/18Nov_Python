import pymysql


# Database Connection
try:
    db = pymysql.connect(host="localhost", user="root", password="", database="dbapp")
    print("Database connected!")
except Exception as e:
    print(e)


cr = db.cursor()
# Table Create
tbl_create = "create table stuinfo(id integer primary key auto_increment,name varchar(20), city varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data = "insert into stuinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('hitesh','surat'),('ashok','jamnagar')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data = "update stuinfo set name='mahesh',city='rajkot' where id=4"
try:
    cr.execute(update_data)
    db.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data = "delete from stuinfo where id=4"
try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


# Show Data
show_data = "select * from stuinfo"
try:
    cr.execute(show_data)
    data = cr.fetchall()
    # data = cr.fetchmany(2)
    # data = cr.fetchone()
    # print(data)
    for i in data:
        print(i[1])
except Exception as e:
    print(e)
