from datetime import datetime
day = datetime.now().weekday()

days = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]

if day < 4:
  print("It’s", days[day])
  remaining = 5 - day
  print(remaining, "days until the weekend")
elif day == 4:
  print("It’s Friday")
  print("Just a day left until the weekend")
else:
  print("It’s the weekend!")