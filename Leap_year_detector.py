import calendar
import datetime

print("Welcome to the leap year detector")
print()

year = datetime.datetime.now().year
year_gap_count = 0
while not calendar.isleap(year):
    year = year + 1
    year_gap_count += 1

if year == datetime.datetime.now().year:
    print("This year is a leap year!")
else:
    print(year,"will be the next leap year!")
    print(year,"is in",year_gap_count,"years!")