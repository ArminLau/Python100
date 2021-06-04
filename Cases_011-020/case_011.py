"""
Case011: There is a pair of rabbits, and they give birth to another pair of rabbits per month since 3 month after they were born. The pair of little rabbits can
give birth to a pair of rabbits after 3 months. Assume that all rabbits will not die. Can you calculate that how many rabbits are there of per month?
"""
# Actually, this problem is similar to Fibonacci sequence
def rabbitCount(n):
    if 0< n <3:
        return 2
    else:
        return rabbitCount(n-1)+rabbitCount(n-2)

month = int(input("Please input the month:"))
print(f"There are {rabbitCount(month)} rabbits after {month} months")