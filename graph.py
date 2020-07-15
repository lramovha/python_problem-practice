for y_axis in range(1,22):
    for x_axis in range(1,22):
        if y_axis is not 11:
            print(" ", end = "")
            if x_axis == 10:
                print ("|", end = "")
        elif y_axis == 11 and x_axis == 11:
            print("|", end = "")
        else:
            print("+", end = "")
    print()