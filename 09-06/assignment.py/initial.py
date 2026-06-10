n = 6
print("11] Initial Pattern")
w = 9
for i in range(5 * 2 - 1):  # 9 rows total
    if i == 0 or i == 4 or i == 8:
        print('*' * w)
    elif i < 4:
        print('*')
    else:
        print(' ' * (w - 1) + '*')
print()