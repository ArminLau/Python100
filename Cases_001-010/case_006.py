"""
Case006: Fibonacci sequence, of which the first and the second number are both one, then since the third number, the next number equals to the sum of previous two numbers
"""
def Fibonacci(n):
    n = int(n)
    return 1 if 0< n < 3 else Fibonacci(n-1)+Fibonacci(n-2)

for i in range(1, 10):
    print(Fibonacci(i))

