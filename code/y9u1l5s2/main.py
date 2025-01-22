from data import cities
from random import choice
city = choice(cities)
done = False
while not done:
  print("Guess the capital:")
  guess = input()
  if guess == city:
    print("You've got it!")
    done = True
  elif guess == "":
    print("It was", city)
    done = True
  elif city[0] != guess[0]:
    print("The first letter is", city[0])
  elif len(guess) != len(city):
    print("It has", len(city), "letters")
  elif city[1] not in guess:
    print("It contains letter", city[1])
  else:
    print("Try again")