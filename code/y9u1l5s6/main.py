print('Enter an ISBN:')
isbn = input()

sum = 0
weight = 1
for character in isbn:
    digit = int(character)
    sum = sum + weight * digit
    if weight == 3:
      weight = 1
    else:
      weight = 3

print("Weighted sum:", sum)
if sum % 10 == 0:
  print('This is a valid ISBN')
else:
  print('This is not a valid ISBN')
