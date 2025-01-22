from europe import cities
from random import choice
print("City hopping random planner")
trip = []
while "London" not in trip:
  city = choice(cities)
  trip.append(city)
  cities.remove(city)
trip.insert(0, "London") 
print("Itinerary:", trip)