from textfile import words
wordlist = words('gadsby.txt')
length = len(wordlist)
print(length, "words in Gadsby")
for word in wordlist:
  if "e" in word:
    print(word)