n1 = eval(input("Please enter the first number: "))
n2 = eval(input("Please enter the first number: "))
n3 = eval(input("Please enter the first number: "))
n4 = eval(input("Please enter the first number: "))

if n1 < n2:
    if n1 < n3:
        if n1 < n4:
            print("the minimum is ", n1)
if n2 < n1:
    if n2 < n3:
        if n2 < n4:
            print("the minimum is ", n2)
if n3 < n1:
    if n3 < n2:
        if n3 < n4:
            print("the minimum is ", n3)
if n4 < n1:
    if n4 < n2:
        if n4 < n3:
            print("the minimum is ", n4)
        