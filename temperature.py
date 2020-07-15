input_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit_value = eval(input_str)

# Calulate equivalent Celsius value
celsius_value = (fahrenheit_value - 32)*(5/9)

# Calulate equivalent Kelvin value
kelvin_value = celsius_value + 273.15

print ("The temperatue in Calcius is: ", celsius_value)
print ("The temperatue in Kelvin is: ", kelvin_value)
