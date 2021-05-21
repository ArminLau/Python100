"""
Input the date in format yyyy/MM/dd then output how many days have passed in that year
"""
date = input("Please input date in format \"yyyy/MM/dd\":")
year = int(date.split("/")[0])
month = int(date.split("/")[1])
day = int(date.split("/")[2])
is_leap_year = (year%400==0 or (year%4==0 and year%100!=0))
sum = 0
month_in_a_year = (0,31,28,31,30,31,30,31,31,30,31,30)
for i in range(1,13):
    sum += month_in_a_year[i-1]
    if month == i:
        sum = sum+day+1 if month > 2 and is_leap_year else sum+day
        break
print(f"{sum-1} days has been passed in this year")
