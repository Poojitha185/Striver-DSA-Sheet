n = 5

for i in range(n):
    start = n - 1 - i
    for j in range(start, n):
        print(chr(65 + j), end=" ")
    print()