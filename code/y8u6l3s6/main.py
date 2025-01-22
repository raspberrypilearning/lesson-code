from random import randint
lucky = randint(1,20)

# this print is only for testing
print("[Cheat to test]", lucky)

print("Guess my number:")
guess = int(input())

if guess == lucky:
  print("Amazing, you guessed it")
else:
  print("Sorry, it’s not", guess)
  print("My lucky number is", lucky)

print("Nice playing with you")