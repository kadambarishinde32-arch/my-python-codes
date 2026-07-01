import sqlite3

conn=sqlite3.connect("student.db")

cursor = conn.cursor()

#table craetion 
cursor.execute('''
    create table if not exists stud(
               sid integer primary key,
               name text not null,
               age integer null
               )
               ''')

print("created!")

# #insert
# cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(1,"ram",23))
# conn.commit()
# print("data inserted")

# #user ip
# sid=int(input("enter your id \n"))
# sname=input("enter your name \n")
# age=int(input("enter your age \n "))
# cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(sid,sname,age))
# conn.commit()
# print("data inserted")

# #entire rows
# cursor.execute("select * from stud")
# rows=cursor.fetchall()
# print(rows)
# for r in rows:
#     print(f"{r[0]}")

# #single
# sid=int(input("enter your id \n"))
# cursor.execute("select * from stud where sid=?",(sid,))
# row=cursor.fetchone()
# print(row)

#update
sid=int(input("enter your id \n"))
cursor.execute("select * from stud where sid=?",(sid,))
row=cursor.fetchone()
print(row)
if sid==row[0]:
    newname=input("enter new name \n")
    cursor.execute("update stud set name=?where sid=?",(newname,sid))
    conn.commit()
    print("data updated")
else:
    print("no record found!")