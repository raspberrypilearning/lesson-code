print("Let's form a band")
band = []
while "guitar" not in band:
  print("Pick an instrument:")
  instrument = input()
  band.append(instrument)
print(band)