from words_data import dictionary
longest = ""
for word in dictionary:
  if len(word) > len(longest) :
    longest = word
print(longest)