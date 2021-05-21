"""
If add an integer I with 100, the result is a perfect square. And the result plus 168 can equal another perfect square. What is the number?
"""
import math
I = 0
while (I+1)**2-I**2 <= 168:
    I+=1
for i in range((I+1)**2):
    if (i+100)**0.5-math.floor((i+100)**0.5)==0 and (i+100+168)**0.5-math.floor((i+100+168)**0.5)==0:
        print(i)
        break
