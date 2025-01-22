from numpy import array
import matplotlib.image

from collections import namedtuple
colour = namedtuple('colour', 'red, green, blue')

def load(filename):
  return matplotlib.image.imread(filename)

def save(filename, image, shape):
  image_array = array(image).reshape(shape)
  matplotlib.image.imsave(filename, image_array)

def pixels(image):
  for row in image:
    for pixel in row:
      yield colour(*pixel)