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


