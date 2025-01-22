print("How old are you?")
age = int(input())

if age >= 18:
  print("You are eligible to vote")
else:
  print("You are not eligible to vote")
  print(18-age, "more years to go")