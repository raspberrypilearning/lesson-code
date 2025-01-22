seasons = ["Winter", "Spring",
           "Summer", "Autumn"]
print("What month is it? (1-12)")
month = int(input())
if month <= 2 or month == 12:
  season = 0
elif month <= 5:
  season = 1
elif month <= 8:
  season = 2
else:
  season = 3
print("It is", seasons[season])