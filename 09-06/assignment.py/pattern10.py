n = 6
print("10] Hollow Reverse Triangle")
for i in range(n, 0, -1):
    if i == n:
        print(' ' * (n - i) + '* ' * i)
    elif i == 1:
        print(' ' * (n - i) + '*')
    else:
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + ' *')
print()