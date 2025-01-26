#  6 Prime Numbers in a Range

def prime_or_not(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def prime_numbers_in_range():
    start = int(input("Enter the starting range: "))
    end = int(input("Enter the ending range: "))
    for i in range(start,end+1):
        if prime_or_not(i):
            print(i)
prime_numbers_in_range()
