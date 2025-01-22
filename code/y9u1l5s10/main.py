print("Enter a number:")
number = input()
sum = 0
for character in number:
  digit = int(character)
  sum = sum + digit
print("Sum of digits in", number, "is", sum)