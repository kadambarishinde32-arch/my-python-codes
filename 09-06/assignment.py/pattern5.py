n = 6
print("5] Hollow Triangle")
for i in range(1, n + 1):
    if i == 1:
        print(' ' * (n - i) + '*')
    elif i == n:
        print('*' * (2 * n - 1))
    else:
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + '*')
print()