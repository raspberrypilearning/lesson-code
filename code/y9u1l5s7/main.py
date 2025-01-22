from random import choice, shuffle

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

characters = []

character = choice(uppercase)
characters.append(character)

character = choice(digits)
characters.append(character)

character = choice(symbols)
characters.append(character)

while len(characters) < 8:
  character = choice(lowercase)
  characters.append(character)

shuffle(characters)
password = "".join(characters)

print(password)