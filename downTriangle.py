h = eval(input("Please Enter hight: "))

for r in range(h):
    for s in range(r):
        print (" ", end="")
    for star in range(h-r):
        print ("*", end="")
    print()