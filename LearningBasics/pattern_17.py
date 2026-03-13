h = ["A", "B", "C", "D"]
for i in range(1, 5):
    for j in range(5, i, -1):
        print(" ", end="")
    for k in range(0, i):         
        print(h[k], end="")
    for k in range(i-2, -1, -1):   
        print(h[k], end="")
    for l in range(5, i, -1):
        print(" ", end="")
    print()
    