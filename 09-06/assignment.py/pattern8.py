n = 6
print("8] Hollow Hourglass")
# Upper half
for i in range(n):
    if i == 0:
        print('* ' * n)
    else:
        print(' ' * i + '*' + ' ' * (2 * (n - i) - 3) + ' *')
# Lower half
for i in range(n - 2, -1, -1):
    if i == 0:
        print('* ' * n)
    else:
        print(' ' * i + '*' + ' ' * (2 * (n - i) - 3) + ' *')
print()