lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

print('Enter a password:')
password = input()

length = len(password)
lowercase_count = 0
uppercase_count = 0
digit_count = 0
symbol_count = 0

for character in password:
  if character in lowercase:
    lowercase_count = lowercase_count + 1
  elif character in uppercase:
    uppercase_count = uppercase_count + 1
  elif character in digits:
    digit_count = digit_count + 1
  elif character in symbols:
    symbol_count = symbol_count + 1

valid = True

if length < 8:
  print("Less than 8 characters")
  valid = False

if lowercase_count == 0:
  print("No lowercase characters")
  valid = False

if uppercase_count == 0:
  print("No uppercase characters")
  valid = False

if digit_count == 0:
  print("No digits")
  valid = False

if symbol_count == 0:
  print("No symbols")
  valid = False

if valid:
  print(password, "is considered a safe password")
else:
  print(password, "is not considered a safe password")