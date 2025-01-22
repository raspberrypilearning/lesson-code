from city_data import cities
from random import choice
city = choice(cities)
count = 0
done = False
gaveup = False
while not done:
  print("Guess the capital:")
  guess = input()
  count = count + 1
  if guess == city:
    print("You've got it!")
    done = True
  elif guess == "":
    print("It was", city)
    gaveup = True
    done = True
  elif city[0] != guess[0]:
    print("The first letter is", city[0])
  elif len(guess) != len(city):
    print("It has", len(city), "letters")
  elif city[1] not in guess:
    print("It contains letter", city[1])
  else:
    print("Try again")

if gaveup:
  print("You tried", count-1, "times before you gave up")
else:
  print("It took you", count, "attempts to guess it")