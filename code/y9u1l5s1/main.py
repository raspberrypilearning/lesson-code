vowels = "aeiouAEIOU"
print("Enter a sentence:")
sentence = input()
vowel_count = 0
for character in sentence:
  if character in vowels:
    vowel_count = vowel_count + 1
print(vowel_count, "vowels in this sentence")