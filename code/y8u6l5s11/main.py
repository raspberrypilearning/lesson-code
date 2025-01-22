from random import randint

questions = 0
correct = 0

while correct < 3:
  a = randint(2,12)
  b = randint(2,12)

  questions = questions + 1
  print("Question", questions)
  print(a, "times", b, "=")
  answer = int(input())

  product = a * b

  if answer == product:
    print("That is correct")
    correct = correct + 1
  else:
    print("I am sorry")
    print(a, "times", b, "is", product)

print("You answered", correct, "out of", questions, "correctly")