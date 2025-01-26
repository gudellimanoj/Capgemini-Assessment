# 8. Multiplication Table Generator

def multiplicationTableGenerator():
    num = int(input("Enter a number: "))
    start = int(input("Enter the starting range: "))
    end = int(input("Enter the ending range: "))
    for i in range(start, end+1):
        print(f"{num} x {i} = {num*i}")
multiplicationTableGenerator()

