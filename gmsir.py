import time

hour = int(time.strftime('%H'))

min = int(time.strftime('%M'))

sec = int(time.strftime('%S'))

if hour < 11 and min <= 59:
    print("Good Morning")

elif hour > 11 and min <=59 and hour <17:
    print("Good Afternoon")

elif hour >=17 and min <=59 and hour <=20:
    print("Good Evening")
else:
    print("Good Night")
    