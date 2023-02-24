import datetime
date_str = input("Enter a date in the format 'YYYY-MM-DD':")
try:
    year, month, day = map(int,date_str.split("-"))
    date = datetime.date(year, month, day)
    print(date.strftime("%A"))
except ValueError:
    print("False")
