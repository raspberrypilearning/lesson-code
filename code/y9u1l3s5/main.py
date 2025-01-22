from europe import cities
from random import choice
print("City hopping random planner")
trip = []
while len(trip) < 5:
  city = choice(cities)
  trip.append(city)
print("Itinerary:", trip)