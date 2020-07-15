Fib_gen  = int(input("how many fib number do you want to generate: "))

def Fibonacci(Fib_gen):
    if (Fib_gen == 1):
        print ("1,")
    elif(Fib_gen == 2):
        print ("1, 1,")
    elif(Fib_gen >= 2):
        prev = 1
        nxt = 1
        print (prev,end = ", ")
        print (nxt, end = ", ")
        add_sum = 0
        for i in range((Fib_gen) - 2):
            add_sum = prev + nxt
            print (add_sum, end = ", ")
            prev = nxt
            nxt = add_sum

Fibonacci(Fib_gen)
        