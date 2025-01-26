# 4 Student Grading System

def studentGrade():
    name = input("Enter student name: ")
    marks = []
    for i in range(5):
        marks.append(int(input("Enter marks for subject " + str(i+1) + ": ")))
    total = sum(marks)
    percentage = total / 5
    grade = "Fail"
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
studentGrade()
