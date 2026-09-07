# conditional code1 - check voting criteria:
voting_age=18
current_year=2026
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
if age >= voting_age:
    print("Welcome. You are allowed to cast your vote")
else:
    print("Sorry. You are too young to vote")


# conditional code2 - which number is it - zero, positive,negative?

num = int(input("Enter a number"))
if num>0:
 print("num is positive")
elif num<0:
 print("num is negative")
else:
 print("num is zero")


# conditional - which triangle is it - Equilateral,Isosceles,Scalene

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("Equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a triangle")


# looping

# for loop - print even numbers from 1 to 10

for i in range(2, 11, 2):
    print(i)

# Using a while loop - sum of first 10 numbers
total = 0
i = 1
while i <= 10:
    total = total + i
    i = i + 1
print(total)


# more string functions

s = "Hello, World!"
print(s.find('o')) # return the first index where the character is present else -1 if not found
print(s.find('a'))
print(s.startswith('Hello'))
print(s.startswith('hello'))
print(s.endswith('World!'))
print(s.find('World!'))
print(s.count('l'))

# lists

# create a list from a empty list
integer_list_new = []

# Using a for loop to add elements to the list
for i in range(1, 6):
    integer_list_new.append(i)

print(integer_list_new)

# Using a list comprehension to create a list of even numbers from 1 to 10
even_numbers = [i for i in range(11) if i % 2 == 0]

print(even_numbers)

# Creating an odd numbers from an empty list using extend function from 1 to 10
odd_numbers = []

odd_numbers.extend(range(1, 10, 2))

print(odd_numbers)

# Sort list
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 8, 9]

# Reverse list
numbers.reverse()
print(numbers)  # Output: [9, 8, 5, 2, 1]

fruits = ["apple", "banana", "cherry"]
print(fruits)

# Copy a list
fruits_copy_list = fruits.copy()
print(fruits_copy_list)

# Combine two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]

# Count occurrences
my_list = [1, 2, 2, 3, 3, 3, 4]
print(my_list.count(3))  # Output: 3

# Find index of element
print(my_list.index(2))  # Output: 1

dry_fruits_list = ["cashew", "almond", "pistachio", "dates"]

capitalized_dry_fruits_list_sorted = sorted([fruit.capitalize() for fruit in dry_fruits_list])

print(capitalized_dry_fruits_list_sorted)

# deletion of elements in a list
my_list = ["a", "b", "c", "d", "e"]

# remove() - removes first occurrence
my_list.remove("b")
print(my_list)  # Output: ['a', 'c', 'd', 'e']

# pop() - removes and returns by index
item = my_list.pop(1)
print(item)      # Output: c
print(my_list)   # Output: ['a', 'd', 'e']

# del - removes by index
del my_list[0]
print(my_list)   # Output: ['d', 'e']


# slicing and dicing:

whole_numbers = list(range(11))
print(whole_numbers)

slice1 = whole_numbers[2:6]
print(slice1)

slice2 = whole_numbers[:5]
print(slice2)

slice3 = whole_numbers[5:]
print(slice3)

odd_numbers = whole_numbers[1:11:2]
print(odd_numbers)

even_numbers = whole_numbers[0:11:2]
print(even_numbers)

reverse_step = whole_numbers[9:3:-1]
print(reverse_step)

reversed_numbers = whole_numbers[::-1]
print(reversed_numbers)

every_third = whole_numbers[::3]
print(every_third)

whole_numbers[2:5] = [20, 30, 40]
print(whole_numbers)

# sets

# string sets
print("creating set- Using curly braces")
fruits = {"orange", "grapes", "mango"}
print(fruits)

print("creating set - Using the set() function")
integer_list = []
for i in range(1, 6):
    integer_list.append(i)
numbers = set(integer_list)
print(numbers)

print("Adding a single element")
fruits.add("apple")
print(fruits)

print("Adding multiple elements")
fruits.update(["peach", "banana"])
print(fruits)

print("Removing an element")
fruits.remove("banana")
print(fruits)

print("Discarding an element (no error if element not found- pineapple)")
fruits.discard("pineapple")
print(fruits)

# integer sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")

print("Union (elements in either set)")
union_set = set1.union(set2)
print("Union:", union_set)

print("Intersection (elements in both sets)")
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

print("Difference (elements in set1 but not in set2)")
difference_set = set1.difference(set2)
print("Difference:", difference_set)

print("Symmetric Difference (elements in either set, but not both)")
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)

# dictionaries

# Create a dictionary
person = {"name": "John", "age": 25, "city": "NYC"}
print(person)
# Output: {'name': 'John', 'age': 25, 'city': 'NYC'}

# Access dictionary values
print(person["name"])  # Output: John
print(person["age"])   # Output: 25

# Add new key-value pair
person["email"] = "john@example.com"
print(person)
# Output: {'name': 'John', 'age': 25, 'city': 'NYC', 'email': 'john@example.com'}

# Update existing value
person["age"] = 26
print(person)
# Output: {'name': 'John', 'age': 26, 'city': 'NYC', 'email': 'john@example.com'}

# Remove key-value pair
del person["email"]
print(person)
# Output: {'name': 'John', 'age': 26, 'city': 'NYC'}

# Pop (remove and return value)
age = person.pop("age")
print(age)     # Output: 26
print(person)  # Output: {'name': 'John', 'city': 'NYC'}

# Get value with default if key doesn't exist
print(person.get("phone"))           # Output: None
print(person.get("phone", "N/A"))    # Output: N/A

# Check if key exists
if "name" in person:
    print("Name exists")  # This will print

# Get all keys
print(person.keys())
# Output: dict_keys(['name', 'city'])

# Get all values
print(person.values())
# Output: dict_values(['John', 'NYC'])

# Get all key-value pairs
print(person.items())
# Output: dict_items([('name', 'John'), ('city', 'NYC')])

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")
# Output: name: John
#         city: NYC

# Loop through keys only
for key in person:
    print(key)
# Output: name
#         city

# Loop through values only
for value in person.values():
    print(value)
# Output: John
#         NYC

# Dictionary length
print(len(person))  # Output: 2

# Copy a dictionary
person_copy = person.copy()
print(person_copy)

# Create dictionary with keys and default value
scores = dict.fromkeys(["John", "Alice", "Bob"], 0)
print(scores)
# Output: {'John': 0, 'Alice': 0, 'Bob': 0}

# Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Clear all items
person.clear()
print(person)  # Output: {}

# Nested dictionary
student = {
    "name": "Alice",
    "age": 20,
    "courses": {
        "math": 90,
        "english": 85,
        "science": 88
    }
}
print(student["courses"]["math"])  # Output: 90

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 5)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16}






# exceptional handling
def divide_numbers():
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division
        result = num1 / num2

    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")
    except ValueError:
        # Handle invalid input
        print("Error: Invalid input. Please enter numeric values.")
    else:
        # If no exception occurs
        print(f"The result is: {result}")
    finally:
        # Code that runs no matter what
        print("Division operation completed.")


# Example usage
divide_numbers()