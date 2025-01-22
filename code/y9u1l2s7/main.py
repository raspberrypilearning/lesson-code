from dice import dicerolls
attacker_points = 8
defender_points = 8

while attacker_points > 0 and defender_points > 0:
  attacker = dicerolls(3)
  defender = dicerolls(2)

  print("Players’ rolls")
  print("Attacker:", attacker)
  print("Defender:", defender)
  attacker.sort(reverse=True)
  defender.sort(reverse=True)

  print("Sorted")
  print("Attacker:", attacker)
  print("Defender:", defender)

  if attacker[0] > defender[0]:
    defender_points = defender_points - 1
  else:
    attacker_points = attacker_points - 1
  if attacker[1] > defender[1]:
    defender_points = defender_points - 1
  else:
    attacker_points = attacker_points - 1

  print("Attacker points:", attacker_points)
  print("Defender points:", defender_points)
  print("Press ENTER for next round")
  input()

if attacker_points > 0:
  print("The Attacker wins")
elif defender_points > 0:
  print("The Defender wins")
else:
  print("An improbable draw")