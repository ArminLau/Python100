"""
Case012: Output all prime numbers between 100 and 200
"""
import math
for number in range(100, 201):
    for j in range(2, round(math.sqrt(number))+1):
        if number%j == 0:
            break
    else:
        print(number)
