from data import dictionary
print("Text to search for:")
sub = input()
collection = []
for word in dictionary:
  if sub in word:
    collection.append(word)
for word in collection:
  print(word)