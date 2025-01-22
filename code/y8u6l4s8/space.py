import requests
url = "http://api.open-notify.org/astros.json"

def people():
  response = requests.get(url).json()
  return response["number"]

def names():
  response = requests.get(url).json()
  for person in response["people"]:
    print(person["name"])