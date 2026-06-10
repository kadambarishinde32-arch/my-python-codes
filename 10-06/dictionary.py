x={}
print(x,type(x))

#add
x["name"]="ram"
print(x)
print(x["name"])

#update
x["name"]="sita"
print(x)
x[101]="stud data"
print(x)

#del or pop
del x[101]
print(x)

print(x.pop("name"))
print(x)
