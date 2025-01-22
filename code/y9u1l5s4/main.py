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

if (length >= 8 and
    lowercase_count > 0 and
    uppercase_count > 0 and
    digit_count > 0 and
    symbol_count > 0):
  print(password, "is considered a safe password")
else:
  print(password, "is not considered a safe password")