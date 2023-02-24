from datetime import date
#extract todays date
today = date.today()
input("Enter day of the week:").lower()
if today.weekday() == date.today():
    print("True")
else:
    print("False")
if today.weekday() == 0:
    print("Today is Monday")
elif today.weekday() == 1:
    print("Today is Tuesday")
elif today.weekday() == 2:
    print("Today is Wednesday")
elif today.weekday() == 3:
    print("Today is Thurday")
elif today.weekday() == 4:
    print("Today is Friday")
elif today.weekday() == 5:
    print("Today is Saturday")
elif today.weekday() == 6:
    print("Today is Sunday" )