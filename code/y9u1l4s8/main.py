from data import dictionary, plot
counts = 35*[0]
for word in dictionary:
  length = len(word)
  counts[length] = counts[length] + 1 
print(counts)

# every item in counts corresponds to
# the number of words of a given length,
# e.g. counts[12] is the number of words
# in the dictionary that have 12 letters
# 
# word_lengths.png is a plot of the counts lists: 
plot(counts, 'word_lengths.png')