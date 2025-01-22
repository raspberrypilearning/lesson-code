from random import randint

planets = ["Mercury", "Venus", "Earth",
           "Mars", "Jupiter", "Saturn",
           "Uranus", "Neptune"]

correct = 0

index = randint(0, 7)
planet = planets[index]
position = index + 1

print("Question #1")
print("What is the position of", planet, "relative to the Sun?")
answer = int(input())

if answer == position:
  print("That is correct.")
  correct = correct + 1
else:
  print("That is not correct.")
print(planet, "is planet number", position, "from the Sun.")

index = randint(0, 7)
planet = planets[index]
position = index + 1

print("Question #2")
print("What is the name planet number", position, "from the Sun?")
answer = input()

if answer == planet:
  print("That is correct.")
  correct = correct + 1
else:
  print("That is not correct.")
print(planet, "is planet number", position, "from the Sun.")

index = randint(0, 6)
planet = planets[index]
next = planets[index+1]

print("Question #3")
print("The name of the planet that comes after", planet, "is...")
answer = input()

if answer == next:
  print("That is correct.")
  correct = correct + 1
else:
  print("That is not correct.")
print(next, "comes after", planet)

print("You got", correct, "out of 3 right.")