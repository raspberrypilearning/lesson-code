from textfile import words
wordlist = words('dracula.txt')
length = len(wordlist)
print(length, "words in Dracula")
times = wordlist.count('vampire')
print("The word 'vampire' appears", times, "times")