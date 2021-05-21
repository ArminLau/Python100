"""
Case005: Input three numbers and output them order by value
"""
numbers = []
for i in range(3):
    numbers.append(int(input(f"Please input number {i+1}: ")))

for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j],numbers[i]
print(numbers)