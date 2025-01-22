from password_data import passwords
from stdiomask import getpass
print("Password to check:")
password = getpass() # instead of input
if password in passwords:
  print("Common password")
  rank = passwords.index(password)
  print("Popularity", rank)
else:
  print("Not a common password")
