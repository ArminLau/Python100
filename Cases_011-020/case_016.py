"""
Print date in particular format
"""
import datetime as dt
print(dt.date.today())
print(dt.date(2035,11,14))
print(dt.date.today().strftime("%d/%m %Y"))
day = dt.date(2008, 3, 8)
print(day.replace(year=day.year+10))