num=int(input("enter a number:"))
og=num
sum=0
while num>0:
    digit=num%10
    fact = 1
    for i in range(1,num):
        fact=fact*i
        sum+=fact
    num=num//10
if og==sum:
    print("strong no")
else:
    print("not strong no")

ouput:
enter a number:145
not strong no
