"""
Case009: Wait for one second to output
"""
import time
countdown = int(input("Please enter the second for countdown: "))
for i in range(countdown):
    print(countdown-i)
    time.sleep(1)
