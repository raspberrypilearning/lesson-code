import re

def fileitems(filename):
  with open(filename) as textfile:
    items = re.split(r'\W+', textfile.read())

  return items

cities = fileitems('cities.txt')