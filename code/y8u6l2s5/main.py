from time import localtime
year = localtime().tm_year

print("Year of birth?")
birth_year = int(input())
age = year - birth_year
print("You are", age, "years old")