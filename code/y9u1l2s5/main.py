from dice import dicerolls
attacker_points = 0
defender_points = 0
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
