# 10. Bill Splitter

def billSplitter():
    total = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))
    tip = float(input("Enter tip percentage: "))
    total += total * tip / 100
    amount = total / people
    print("Each person has to pay:", amount)
billSplitter()