letters = 'abcdefghijklmnopqrstuvwxyz'

print("Enter the plaintext:")
plaintext = input()

print("Enter the key:")
key = int(input())

cipherlist = []
for character in plaintext:
  if character in letters:
    position = letters.index(character)
    position = position + key
    if position >= 26:
      position = position - 26
    shifted_character = letters[position]
  else:
    shifted_character = character
  cipherlist.append(shifted_character)

ciphertext = "".join(cipherlist)
print("Ciphertext:", ciphertext)
