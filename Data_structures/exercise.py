'''
LIST
'''
# 1: Create a list of 5 integers and display it
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# Access individual elements by index
print("First element:", my_list[0])
print("Third element:", my_list[2])

# 2: Append a new item to the end of the list
my_list.append(60)
print("After appending 60:", my_list)

# 3: Reverse the order of the list
my_list.reverse()
print("After reversing:", my_list)

# 4: Print the number of occurrences of a specified element
print("Number of times 30 appears:", my_list.count(30))

# 5: Append items of list1 to the front of list2
list1 = [1, 2, 3]
list2 = my_list
list2 = list1 + list2
print("After appending list1 to front of list2:", list2)

# 6: Insert a new item before the second element in list2
list2.insert(1, 99)
print("After inserting 99 before second element:", list2)

# 7: Remove the item from a specified index (e.g., index 3)
removed_item = list2.pop(3)
print(f"After removing item at index 3 ({removed_item}):", list2)

# 8: Remove the first occurrence of a specified element 
if 30 in list2:
    list2.remove(30)
    print("After removing first occurrence of 30:", list2)
else:
    print("30 not found in list to remove.")

'''
DICTIONARY
'''
# 1. WAP to add a key and value to a dictionary.

sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30

print("Updated Dictionary:", sample_dict)

# 2. WAP to Concatenate multiple dictionaries into one

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {}
for d in (dic1, dic2, dic3):
    merged_dict.update(d)

print("Merged Dictionary:", merged_dict)

# 3. WAP to Check if a given key alredy exists in a dictionary.

check_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}

key_to_check = int(input("Enter a key to check: "))

if key_to_check in check_dict:
    print(f"Key {key_to_check} exists with value:", check_dict[key_to_check])
else:
    print(f"Key {key_to_check} does not exist.")

# 4. WAP to iterate over a dictionary using for loop and print keys only, values only, and both keys and values.

fruits = {1: 'apple', 2: 'banana', 3: 'cherry'}

print("Keys:")
for key in fruits:
    print(key)

print("\nValues:")
for value in fruits.values():
    print(value)

print("\nKeys and Values:")
for key, value in fruits.items():
    print(f"{key}: {value}")

# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (inclusive), and the values are the squares of the keys.
squares_dict = {}

for i in range(1, 16):
    squares_dict[i] = i ** 2

print("Squares Dictionary:", squares_dict)

# 6. Write a program to sum all the values in a dictionary, assuming the values are of int type.

marks = {'Math': 90, 'Physics': 85, 'Chemistry': 88}

total = sum(marks.values())

print("Sum of all values:", total)

'''
TUPLE
'''

# 1. Write a program to print the 4th element from the beginning and the 4th element from the end in a tuple.
sample_tuple = (5, 10, 15, 20, 25, 30, 35, 40)

print("4th element from beginning:", sample_tuple[3])
print("4th element from end:", sample_tuple[-4])

# 2. Write a program to check whether an element exists in a tuple or not.
my_tuple = (1, 3, 5, 7, 9)
element = int(input("Enter an element to check: "))

if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# 3. Write a program to convert a list into a tuple.
my_list = [10, 20, 30, 40]

converted_tuple = tuple(my_list)

print("Converted tuple:", converted_tuple)

# 4. Write a program to find the index of an item in a tuple.
# Sample tuple
sample_tuple = ('apple', 'banana', 'cherry', 'date')

item = input("Enter item to find index of: ")

if item in sample_tuple:
    index = sample_tuple.index(item)
    print(f"Index of '{item}' is:", index)
else:
    print(f"'{item}' is not in the tuple.")

# 5.Write a program to replace the last value of each tuple in a list with 100.

# Sample List: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in sample_list]

print("Updated list:", updated_list)

'''
SET
'''
# 1.Write a program to remove a given item from a set.
my_set = {1, 2, 3, 4, 5}

item = int(input("Enter item to remove from set: "))

if item in my_set:
    my_set.remove(item)
    print("Updated set:", my_set)
else:
    print(f"{item} not found in the set.")

# 2.Write a program to create an intersection of sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1.intersection(set2)

print("Intersection of sets:", intersection)

# 3.Write a program to create a union of sets.
set1 = {1, 2, 3}
set2 = {4, 5, 6}

union = set1.union(set2)

print("Union of sets:", union)

# 4.Write a program to find the maximum and minimum value in a set.

num_set = {12, 45, 23, 67, 34, 89}

maximum = max(num_set)
minimum = min(num_set)

print("Maximum value in set:", maximum)
print("Minimum value in set:", minimum)

'''
STRING
'''
# 1.Write a program to count the number of uppercase and lowercase letters in a string.
text = input("Enter a string: ")

upper_count = sum(1 for ch in text if ch.isupper())
lower_count = sum(1 for ch in text if ch.islower())

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)

# 2.Write a program to check whether a given string is a palindrome or not.
word = input("Enter a string to check palindrome: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

'''
3. Given a string, return a new string made of n copies of the first 2 characters of the original string, where n is the length of the string.

Example: If input is "Wipro", output should be "WiWiWiWiWi".
'''
string = input("Enter a string: ")
n = len(string)

# Get first 2 characters, or whole string if shorter than 2
first_two = string[:2]

# Repeat n times
result = first_two * n
print("Result:", result)

'''
4. Given a string, if the first or last character is 'x', return the string without those 'x' characters. Otherwise, return the string unchanged.

Example: If input is "xHix", output should be "Hi".
'''
string = input("Enter a string: ")

if string.startswith('x') or string.endswith('x'):
    # Remove 'x' from both ends
    if string.startswith('x'):
        string = string[1:]
    if string.endswith('x'):
        string = string[:-1]

print("Processed string:", string)

'''
5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.

Example: If inputs are "Wipro" and 3, output should be "propropro".
'''
string = input("Enter a string: ")
n = int(input("Enter a number: "))

last_n = string[-n:]  # Get last n characters
result = last_n * n   # Repeat n times

print("Result:", result)
