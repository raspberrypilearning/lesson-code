lucky = 13

guessed = False
while guessed == False:

  print("Can you guess my lucky number?")
  guess = int(input())

  if guess != lucky:
    print("Sorry, it's not", guess)
  else:
    print("Amazing, you guessed it")

print("Nice playing with you")