n = eval(input("Please enter a number: "))
product = 1

for i in range(1, n + 1):
    product *= i
    print("i ",i)
    print("product ",product)
    