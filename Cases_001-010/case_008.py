"""
Case008: Print a multiplication-table
"""
for i in range(1,10):
    line = ""
    for j in range(1,i+1):
        line += f"{j} * {i} = {j*i}  "
    print(line)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%2ld '%(i,j,i*j),end='')
#     print()
