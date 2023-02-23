import datetime
day_of_week = input("Enter day").lower()
check_day = datetime.datetime.strtime(day_of_week, '%A')
