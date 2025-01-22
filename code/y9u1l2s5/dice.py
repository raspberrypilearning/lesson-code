from random import randint

def diceroll():
  return randint(1,6)

def dicerolls(n):
  return [diceroll() for roll in range(n)]