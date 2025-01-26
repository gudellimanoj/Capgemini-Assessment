# 7 Bank Loan Eligibility
def loan_eligibility(salary, age,credit_score ):
    if age <18 and salary <20000 and credit_score <600:
        return "Loan is Approved"
    else:
        return "Loan is Rejected"
salary=int(input("enter salary amount"))
age=int(input("enter age"))
credit_score=int(input("enter credit score"))
print(loan_eligibility(salary, age,credit_score ))