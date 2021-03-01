import datetime
import time

date = datetime.date(2000, 1, 1)  # Chosen date (Year, Month, Day)

# Every second, calculate delta
while True:
    today = datetime.date.today()  # Today
    delta = int((date - today).days)  # Difference between today and the given date, in days

    if delta < 0:
        print("The chosen date has already passed", abs(delta), "day(s) ago", end="\r")
    elif delta == 0:
        print("It's the chosen day!", end="\r")
    elif delta > 0:
        print("You have", delta, "day(s) until the chosen date", end="\r")

    time.sleep(1)
