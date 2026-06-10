x=((10,20,30),40,50,["hello","bye"])
for i in x:
    if type(i)==tuple:
        for j in i:
             print(j)

       
    else:
        print(i)



