city=input("Enter your city name:")
temp=int(input("Enter the temperature today:"))

if temp > 32:
    print("It is very hot today!")
elif temp > 25:
    print("Temperature is warm! :)")
elif temp > 16:
    print("Temperatyre is cool! :)")
else:
    print("It's very cold today!")

import datetime
import calendar
now=datetime.datetime.now()
print(now)
print(calendar.calendar(now.year))