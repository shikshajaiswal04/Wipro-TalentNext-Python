'''
1. Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.

Constraint: All the colors will be completely in either lowercase or uppercase.

Input: green-red-yellow-black-white 
Output: black-green-red-white-yellow

Input: PINK-BLUE-TAN-PURPLE 
Output: BLUE-PINK-PURPLE-TAN
'''

def sort_colors(color_string):
  
    colors = color_string.split('-')

    colors.sort()
    sorted_colors = '-'.join(colors)
    
    return sorted_colors

'''
Create a Python module with the following functions:


ispalindrome(name) -	Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name)- Given the user name as input, this function should tell us how many vowels are present in it.
frequency_of_letters(name)-	Given the user name as input, this function should tell us how many times each letter appears in the name.

'''
def ispalindrome(name):
    name = name.lower()
    return name == name[::-1]


def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in name if char in vowels)


def frequency_of_letters(name):

    freq = {}
    for char in name:
        if char.isalpha():  # only consider letters
            char = char.lower()
            freq[char] = freq.get(char, 0) + 1
    return freq
