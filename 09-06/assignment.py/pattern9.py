n = 6
print("9] Random Pattern")
size = 11
mid = size // 2
for i in range(size):
    row = ''
    for j in range(size):
        if (i == 0 or i == size - 1 or       # top/bottom border
            j == mid or                        # vertical center
            i == j or                          # main diagonal
            i + j == size - 1):               # anti-diagonal
            row += '* '
        else:
            row += '  '
    print(' ' + row)
print()