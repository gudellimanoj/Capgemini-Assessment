# 11. Password Strength Checker

def password_checker(pw):
    if len(pw) < 8:
        return False
    upper = False
    lower = False
    digit = False
    special = False
    for i in pw:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isdigit():
            digit = True
        if not i.isalnum():
            special = True
    if upper and lower and digit and special:
        return True
    return False
pw=input('Enter the password: ')
print(password_checker(pw))