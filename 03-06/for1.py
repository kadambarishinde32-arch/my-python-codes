s= int(input("Enter the Starting Value:"))
e=int(input("Enter the ending value:"))
for i in range (s,e+1):
    if i%12==0 and i%6==0:
         print(i)