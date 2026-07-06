age=int(input("enter age:"))
gender=input("enter the gender:")
h=float(input("enter the height:"))

if gender=="M" or gender=='m':
    if age>=21 and age<=33:
        if h>=5.6:
            print("Eligible")
        else:
            print("Not Eligible(height issue)")
    else:
        print("Not Eligible(Age Issue)")

elif gender=="F" or gender=='f':
    if age>=21 and age<=28:
        if h>=5.3:
            print("Eligible")
        else:
            print("Not Eligible(height issue)")
    else:
        print("Not Eligible(Age Issue)")

else:
     print("Inavlid Gender")
