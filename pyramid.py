h = eval(input("Please enter hight: "))

for r in range(h):
    for space in range(h - r):
        print(" ", end="")
    for star in range(r + 1):
        print(" ", end="")
        print("*", end="")
    print()
