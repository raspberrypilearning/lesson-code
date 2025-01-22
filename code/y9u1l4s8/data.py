import matplotlib.pyplot as plotter
from textfile import lines

# source of words:
# https://github.com/dwyl/english-words
dictionary = lines('words_alpha.txt')

def plot(data, filename):
  plotter.plot(data)
  plotter.savefig(filename)