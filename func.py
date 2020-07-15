element = int(input("Please Enter a number: "))
i = 0
k = 1
if element <= 0:
    print("series is", i)
else:
    print(i, k, end = " ")
    for y in range(2, element):
        new = i + k
        print(new, end=" ")
        i = k
        k=new
    
    
    