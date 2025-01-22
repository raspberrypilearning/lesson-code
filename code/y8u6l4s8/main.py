from space import people

print("How many people do you think are in space right now?")
guess = int(input())

number = people()

if guess < number:
  print("It's actually more than that.")
elif guess > number:
  print("It's actually fewer than that.")
else:
  print("That's right!")

print("There are", number, "people in space right now.")