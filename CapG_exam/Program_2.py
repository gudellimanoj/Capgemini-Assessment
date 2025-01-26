# 2 Temperature Conversion Tool

def celsius_to_fahrenheit(c):
    return (c*9/5)+32
def fahrenheit_to_celsius(f):
    return (f-32)*5/9
def celsius_to_kelvin(c):
    return c+273.15
def kelvin_to_celsius(k):
    return k-273.15
def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))
def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))
def temp_menu():
    while True:
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")
        choice =input("Choose otp")

        if choice =='1':
            c=float(input("Enter temperature in celsius: "))
            print(f"{c}C is{celsius_to_fahrenheit(c):}F")
        elif choice =='2':
            c=float(input("Enter temperature in fahrenheit: "))
            print(f"{f}C is{fahrenheit_to_celsius(f):}F")
        elif choice =='3':
            c=float(input("Enter temperature in celsius: "))
            print(f"{c}C is{celsius_to_kelvin(c):}F")
        elif choice =='4':
            c=float(input("Enter temperature in kelvin: "))
            print(f"{k}C is{kelvin_to_celsius(k):}F")
        elif choice =='5':
            c=float(input("Enter temperature in fahrenheit: "))
            print(f"{f}C is{fahrenheit_to_kelvin(f):}F")
        elif choice =='6':
            c=float(input("Enter temperature in kelvin: "))
            print(f"{k}C is{kelvin_to_fahrenheit(k):}F")
        elif choice =='7':
            print("Exit")
            break
        else:
            print("Invalid")
temp_menu()
            
        