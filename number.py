secret_num = 22

guess = eval(input("Please Enter a number?: "))
while guess != secret_num:
    if guess > secret_num:
        print("Hi")
    elif guess < secret_num:
        print("lo")
    guess = eval(input("Please Enter a number?: "))
    if guess == secret_num:
        print ("correct")    
    