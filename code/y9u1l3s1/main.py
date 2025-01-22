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
  else:
    print("Try again")