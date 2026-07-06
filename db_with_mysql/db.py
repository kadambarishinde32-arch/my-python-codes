import mysql.connector

#conn create 
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kadu@2008",
    database="linkcode"
)
print("database connected!")

cursor=conn.cursor()
#create table
cursor.execute("""
    create table if not exists emp(
               empid int primary key auto_increament,
               name varchar(20) not null,
               sal decimal(19,2) check(sal>0)
               )
""")

conn.commit()
print("table created!")
