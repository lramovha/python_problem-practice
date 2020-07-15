Fib_gen  = int(input("how many fib number do youwant to generate: "))

def Fibonacci(Fib_gen):
    prev = 1
    nxt = 1
    print (prev, ", ")
    print (nxt, ", ")
    add_sum = 0
    for i in range(Fib_gen):
        add_sum = prev + nxt
        print (add_sum)
        print (", ")
        prev = nxt
        nxt = add_sum

Fibonacci(8)
        