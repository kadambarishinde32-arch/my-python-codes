user=input("Enter a username:")
password=input("Entera password:")

if user=="Admin":
    if password=="1234":
        print("Login SuccessFull")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")
