from weather import description

print("Where do you live?")
location = input()
weather = description(location)
print("In", location, "the weather is", weather)

if weather == "cloudy":
  advice = "No sunglasses"
elif weather == "rainy":
  advice = "Get an umbrella"
elif weather == "snowy":
  advice = "Mittens and earmuffs"
else:
  advice = "No particular advice"

print(advice)