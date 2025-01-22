from data import dictionary
nb_words = len(dictionary)       
print(nb_words, "english words in the list")
print("Length of words to search for:")
length = int(input())
count = 0
for word in dictionary:
  if len(word) == length:
    count = count + 1
print("There are", count, "words with", length, "letters")