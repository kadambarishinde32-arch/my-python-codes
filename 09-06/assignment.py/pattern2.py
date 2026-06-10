n = 6 
print("2] Diamond Pattern")
# Upper half (including middle)
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
# Lower half
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
print()