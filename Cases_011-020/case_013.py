"""
Case013： Print all "Narcissus Number", whose cubic sum of each digit is equal to the number itself, and they are all three-digit.
For example: 153 is a Narcissus Number, because 153 = 1*1*1+5*5*5+3*3*3
"""
for i in range(100, 1000):
    if i == int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3:
        print(i)