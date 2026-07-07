import mysql.connector

#conn create 
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kadu@2008",
    database="linkcode"
)
print ("db connected")
cursor=conn.cursor()
#table create
cursor.execute("create table files(id int primary key auto_generate)")
print("table created")
#read binary data


file=open("image.png","rb")
data=file.read()
print(data)
file.close()
query="insert into files(filename,filedata) values(%s,%s)"
values=("image.png",data)
cursor.execute(query,values)
conn.commit()
print("data save")