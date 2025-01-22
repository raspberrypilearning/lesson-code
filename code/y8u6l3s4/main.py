lucky = 13

print("Guess my number:")
guess = int(input())

if guess == lucky:
    print("Amazing, you guessed it")
else:
    print("Sorry, it’s not", guess)
    print("My lucky number is", lucky)

print("Nice playing with you")