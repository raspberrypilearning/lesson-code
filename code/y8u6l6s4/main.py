lucky = 13
count = 0

guessed = False
while guessed == False and count < 3:

  print("Can you guess my lucky number?")
  guess = int(input())

  count = count + 1

  if guess != lucky:
    print("Sorry, it's not", guess)
  else:
    # raise flag
    guessed = True
    print("Amazing, you guessed it")

print("It took you", count, "guesses")
print("Nice playing with you")