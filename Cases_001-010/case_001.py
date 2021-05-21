"""
case001: How many different three-digit numbers consisted of four numbers "1, 2, 3, 4" and have not replicated number? what are they?
"""
count = 0
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            number = a*100+b*10+c
            if a!=b and a!=c and b!=c:
                count += 1
                print(number)
print(f"Total: {count}")