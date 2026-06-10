n = 6  
print("0] Solid Square")
for i in range(n):
    print('*' * n)
print()

#1. Hollow Square

print("1] Hollow Square")
for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * n)
    else:
        print('*' + ' ' * (n - 2) + '*')
print()