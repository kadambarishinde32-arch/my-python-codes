num=int(input("enter a number:"))
sum=0
for i in range (1,num):
    if num%i==0:
        sum+=i
        
if sum==num:
        print("perfect no")
else:
        print("not perfect no")

ouput:
enter a number:6
perfect no
