"""
Use the nesting of conditional operators to solve this issue: students with academic score more than 90 are represented by A,
those between 60-89 are represented by B, and the rest below 60 are marked as ​C.
"""
score = float(input("Please enter your score:"))
if score>=90:
    grade = 'A'
elif 60<=score<90:
    grade = 'B'
elif score<60:
    grade = 'C'
print(f"Your grade is {grade}")