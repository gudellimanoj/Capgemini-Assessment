# 13. Palindrome Checker
def palindrome_checker(n):
    if n==n[::-1]:
        return True
    return False        
def get_input():            
    n=input('enter the number or string to check palindrome: ')     
    return n
n=get_input()
print(palindrome_checker(n))