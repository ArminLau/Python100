"""
Case014: decompose a number to prime factors. For example, input 90, output 90=?
"""
def decomposeNumber(number, list:list):
    for i in range(2, number+1):
        if number%i == 0:
            list.append(i)
            if int(number/i) == 1:
                return list if len(list)>1 else [1, list[0]]
            else:
                return decomposeNumber(int(number/i), list)

number = int(input("Please enter a random positive integer: "))
print(decomposeNumber(number, []))