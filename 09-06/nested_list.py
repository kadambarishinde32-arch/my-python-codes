x=[[1,"car",500],
   [2,"doll",1000],
   [3,"grocery",2000],
   [4,"sunglasses",5000]
   ]

print(x,type(x))

for ids in x:
    print(ids[2])

x[1][2]=2500
print(x)

for i in x:
    print(i)


product=input("Enter thr product:")
price=int(input("Enter thr price:"))

id= len(x)+1
x.append([id,product,price])
print(x)