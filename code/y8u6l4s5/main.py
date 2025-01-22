print("Where do you live?")
location = input()
print("What's the weather in", location, "now?")
weather = input()

if weather == "cloudy":
  advice = "No sunglasses"
elif weather == "rainy":
  advice = "Get an umbrella"
elif weather == "snowy":
  advice = "Mittens and earmuffs"
else:
  advice = "No particular advice"

print(advice)