#  18.BMI Calculator

def bmi_calculator():
    weight=float(input("Enter the weight in kg: "))
    height=float(input("Enter the height in m: "))
    bmi=weight/(height**2)
    if bmi<18.5:
        print(f"Underweight: {bmi}")
    elif bmi>=18.5 and bmi<24.9:
        print(f"Normal: {bmi}")
    elif bmi>=24.9 and bmi<29.9:
        print(f"Overweight: {bmi}")
    else:
        print(f"Obese: {bmi}")
bmi_calculator()