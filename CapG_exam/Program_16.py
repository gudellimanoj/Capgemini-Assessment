# 16.Odd and Even Separator

def odd_even_separator(data):
    odd=[]
    even=[]
    for i in data:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return f'Even list is :{even} and odd list is:{odd}'
data= list(map(int,input('Enter the numbers: ').split()))
print(odd_even_separator(data))