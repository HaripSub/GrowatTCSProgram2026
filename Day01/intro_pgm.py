# Day 1 Python Session - Basic Program

# 1. Print statements
print("Welcome to Day 1 Python Session!")
print("=" * 50)

def print_hi(name):
    """Print a greeting message"""
    print(f'Hi, {name}!')

print_hi('Anna')

print("Hello", "World", "Python")

print("Apple", "Banana", "Cherry", sep=" - ")

name = "Python"
version = 3.9

# f-string (Python 3.6+)
print(f"f-string: {name} version {version}")

# .format() method
print("format method: {} version {}".format(name, version))

# % operator (old style)
print("Old style: %s version %.1f" % (name, version))


# 2. Variables and data types
name = "Python Learner"
age = 25
height = 5.9
is_student = True

print(f"Value of Name: {name}")
print(f"Type of Name: {type(name)}")
print(f"Value of Age: {age}")
print(f"Type of Age: {type(age)}")
print(f"Value of Height: {height}")
print(f"Type of height: {type(height)}")
print(f"Value of Is Student: {is_student}")
print(f"Type of Is_Student: {type(is_student)}")

# 3. Basic arithmetic with user input
print("\n" + "=" * 50)
print("Basic Arithmetic Operations:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"\n Addition: {num1} + {num2} = {num1 + num2}")
print(f" Subraction: {num1} - {num2} = {num1 - num2}")
print(f" Multliplication:  {num1} * {num2} = {num1 * num2}")
print(f" Division:  {num1} / {num2} = {num1 / num2}")
print(f" Floor Division: {num1} // {num2} = {num1 // num2}")
print(f" Modulus:  {num1} % {num2} = {num1 % num2}")

# 4. string methods
s = "Hello, World!"
print("\nString examples:")
print("original string:" ,s)
print("Upper:", s.upper())
print("Lower:", s.lower())
print("swapcase():", s.swapcase())
print("title():", s.title())
print("capitalize():", s.capitalize())
print("Replace:", s.replace("World", "Python"))
print("Slice (0:5):", s[0:5])
print("Split:", s.split(", "))
rev1 = s[::-1]
print("reversing a string:", rev1)

# 5. Collections: list, tuple, set, dict
fruits = ["apple", "banana", "cherry"]
numbers_tuple = (1, 2, 3)
unique = {1, 2, 2, 3}
person = {"name": "Anna", "age": 30}

print("\nCollections:")
print("List:", fruits)
print("Tuple:", numbers_tuple)
print("Set:", unique)
print("Dict:", person)
print("Access dict:", person["name"])


# 6. control flow

# find greatest of 2 numbers

num1 = 20
num2 = 10

if num1 > num2:
    print("num1 is greater than num2")

else:
    print("num2 is greater than num1")

# 7.Looping

# print numbers from 1 to 5
for i in range(5):
    print(i)




