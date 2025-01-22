from images import * 
image = load('island.png')
processed = []
for pixel in pixels(image):
  r = pixel.red
  g = pixel.green
  b = pixel.blue
  p_pixel = colour(r, g, b)
  processed.append(p_pixel)

save('p-island.png', processed, image.shape)