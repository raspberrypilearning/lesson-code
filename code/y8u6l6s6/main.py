from random import randint

lucky = randint(1,20)
count = 0

guessed = False
while guessed == False and count < 3:

  print("Can you guess my lucky number?")
  guess = int(input())

  count = count + 1

  if guess < lucky:
    print("My lucky number is larger than", guess)
  elif guess > lucky:
    print("My lucky number is smaller than", guess)
  else:
    # raise flag
    guessed = True
    print("Amazing, you guessed it")

if guessed == True:
  print("It took you", count, "guesses")
else:
  print("My lucky number is", lucky)

print("Nice playing with you")