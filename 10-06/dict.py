x={}
key=input("enter key: ")
value=input("enter value: ")
x[key]=value
print(x)
x.update({"name":"ram"})
x.update({"name":"sita"})
x.update({"age":"70"})
print(x)


stud={
    "name":"ram",
    "age":20,
    "div":"a",

}

print(stud.keys())
print(stud.items())
print(stud.values())

for key,values in stud.items():
    print(key,values)

stud={
    "name":"ram",
    "age":20,
    "div":"a",
    "marks":[100,50,87],
    "rollno":237
}
for values in stud.values():
    if type(values)==list:
        for i in values:
            print(i)
        continue
    print(values)