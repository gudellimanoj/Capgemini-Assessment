# 12.Pattern Generator

def get_input():
    n=int(input('enter the number: '))
    return n
def pattern(n):
    for i in range(1,n+1):
        print('*'*i)
n=get_input()
pattern(n)
def pattern(n):
    for i in range(n,0,-1):
        print('*'*i)
n=get_input()
pattern(n)
