print("What day is it today?")
day = int(input())
if day < 4:
  print("It’s a weekday")
  remaining = 5 - day
  print(remaining, "days until the weekend")
elif day == 4:
  print("It’s Friday")
  print("Just a day left until the weekend")
else:
  print("It’s the weekend!")