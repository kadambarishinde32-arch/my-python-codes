x=[[1,'car',500],
   [2,'doll',1000],
   [3,'Grocery',1500],
   [4,'Sunglasses',600],
 ]
print(x,type(x))
#accessing the elements of list
for i in x:
    print(i)
#adding new element to the list
"""a =input("Enter the Product: ")
P=float(input("Enter the Price: "))
id= len(x)+1
x.append([id,a,P])
print(x)"""
#updating the list
"""n=int(input("What do you want to update:"))
ch=input("Update Product or Price:")

for p in x:
    if p[0]==n:
        if ch=="Product"or ch=="product":
            p[1]=input("Enter the new Product:")
        elif ch=="Price" or ch=="price":
            p[2]=float(input("Enter the new Price:"))
        else:
            print("Invalid input")
print(x)"""
#deleting the element from the list
"""n=int(input("What do you want to delete:"))
for p1 in x:
    if p1 [0]==n:
        x.remove(p1)
        break
    else:
        x.clear()
print(x)"""
#buying the product
"""total=0
for i1 in x:
    if i1[1]=="doll" and i1[1]=='car':
        total+=i1[2]*95/100
    elif i1[1]=="Grocery":
        total+=i1[2]*93/100
    else:
        total+=i1[2]*97/100
gst=total*18/100
print("GST",gst)
print("Total amount to be paid:",total+gst)"""

#searching the product
s=input("What do you want to search:")
d=input("Search by Id or Product:")
for h in x:
    if d=="Id" or d  =="id":
        if h[0]==int(s):
            print(h)
            break
    elif d=="Product" or d=="product": 
         if h[1]==s:
           print(h)
           break
    else:
         print("Invalid input")
       






        

    

    
  
   


    

x=[[1,'car',500],
   [2,'doll',1000],
   [3,'Grocery',1500],
   [4,'Sunglasses',600],
 ]
print(x,type(x))
#accessing the elements of list
for i in x:
    print(i)
#adding new element to the list
"""a =input("Enter the Product: ")
P=float(input("Enter the Price: "))
id= len(x)+1
x.append([id,a,P])
print(x)"""
#updating the list
"""n=int(input("What do you want to update:"))
ch=input("Update Product or Price:")

for p in x:
    if p[0]==n:
        if ch=="Product"or ch=="product":
            p[1]=input("Enter the new Product:")
        elif ch=="Price" or ch=="price":
            p[2]=float(input("Enter the new Price:"))
        else:
            print("Invalid input")
print(x)"""
#deleting the element from the list
"""n=int(input("What do you want to delete:"))
for p1 in x:
    if p1 [0]==n:
        x.remove(p1)
        break
    else:
        x.clear()
print(x)"""
#buying the product
"""total=0
for i1 in x:
    if i1[1]=="doll" and i1[1]=='car':
        total+=i1[2]*95/100
    elif i1[1]=="Grocery":
        total+=i1[2]*93/100
    else:
        total+=i1[2]*97/100
gst=total*18/100
print("GST",gst)
print("Total amount to be paid:",total+gst)"""

#searching the product
s=input("What do you want to search:")
d=input("Search by Id or Product:")
for h in x:
    if d=="Id" or d  =="id":
        if h[0]==int(s):
            print(h)
            break
    elif d=="Product" or d=="product": 
         if h[1]==s:
           print(h)
           break
    else:
         print("Invalid input")