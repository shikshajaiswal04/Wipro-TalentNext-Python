import mini_project

name = input("Enter your name: ")

# Check if palindrome
if mini_project.ispalindrome(name):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

# Count vowels
vowel_count = mini_project.count_the_vowels(name)
print("Number of vowels:", vowel_count)

# Frequency of each letter
letter_freq =  mini_project.frequency_of_letters(name)
print("Letter frequencies:")
for letter, freq in letter_freq.items():
    print(f"{letter}: {freq}")
