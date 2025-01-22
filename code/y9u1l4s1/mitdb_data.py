import matplotlib.pyplot as plotter
from textfile import load

# source of dataset:
# physionet.org/content/mitdb/, specifically, dataset '100'
# note: single-channel data has been extracted from 
# the original dataset and written to a text file 
mitdb_data = load('mitdb_data.txt')

def load(nb_values=None):
  if nb_values is None:
    return mitdb_data
  else:
    return mitdb_data[:nb_values]

def plot(data, filename):
  plotter.plot(data)
  plotter.savefig(filename)