# 15.Leap Year Checker

def leap_year_checker(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    return False
def get_input():
    year=int(input('Enter the year: '))
    return year
year=get_input()
print(leap_year_checker(year))

