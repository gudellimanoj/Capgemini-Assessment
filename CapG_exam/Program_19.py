# 19.Find Second Largest Number
def get_input():
    n = int(input('Enter the number of elements: '))
    data = []
    for i in range(n):
        data.append(int(input(f'Enter the number {i+1}: ')))    
    return data

def second_largest(data):
    unique_data = list(set(data))  # Remove duplicates
    unique_data.sort()
    if len(unique_data) < 2:
        return "Not enough unique elements to determine the second largest."
    return unique_data[-2]

data = get_input()
print(second_largest(data))
