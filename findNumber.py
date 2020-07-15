
def findNumber(arr, k):
    i = 0
    for i in arr:
        if (i == k):
            print("YES")
            break;
    else:
        print("NO")
            
arr = [3 , 1, 5, 9 , 4]
k = 8

findNumber(arr, k)