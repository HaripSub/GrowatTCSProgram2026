# variable declarations


name = input('Enter your name: ')
age = int(input('Enter your age: '))

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

print("...........................................................................................")

print("Functions without arguments")

def print_details():

    print('my name is %s and age is %d' % (name, age))


print("...........................................................................................")

print_details()


print("...........................................................................................")

print("Functions with arguments")

print("...........................................................................................")


def addition(a, b):
    return int(a) + int(b)


def maximum(a, b):
    return max(int(a), int(b))


print(f"The sum of {a} and {b} is {addition(a, b)}")
print(f"The maximum of {a} and {b} is {maximum(a, b)}")

print("...........................................................................................")


print("Default Arguments")

print("...........................................................................................")


def print_color(color="green"):
    print("The color that is adored by me is: " + color)


print_color("Yellow")
print_color("blue")
print_color()

print("------------------------------------------------------------------------------------")

print("Keyword Arguments")

print("------------------------------------------------------------------------------------")


def print_your_details(name, age):
    print(f'my name is {name} and age is {age}')


print_your_details(name="George", age=45)

print_your_details(age=45, name="Sam")


print("------------------------------------------------------------------------------------")

print("Arbitrary Arguments")

print("------------------------------------------------------------------------------------")


def welcome_members(*member_names):
    for team_member in member_names:
        print("Welcome " + team_member + " to the team")


welcome_members("Alice", "Bob", "Charlie", "Daniel")

print("------------------------------------------------------------------------------------")


# math module
import math

# Constants
print(math.pi)      # 3.141592653589793
print(math.e)       # 2.718281828459045


# Functions
print(math.sqrt(16)) # 4.0
print(math.pow(2, 3))  # 8.0
print(math.ceil(4.3)) # 5
print(math.floor(4.7)) # 4
print(math.factorial(5)) # 120
print(math.gcd(12, 8)) # 4
print(math.sin(math.pi/2))  # 1.0

# random module
import random

# Random float
print(random.random())  # 0.xxx

# Random integer
print(random.randint(1, 10))

# Random choice from list
print(random.choice(['apple', 'banana', 'cherry']))

# Shuffle list
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)

# Random sample
print(random.sample(range(100), 5))

# creating a ransom list and sorting it
random_list = random.choices(range(1, 101), k=10)
random_list.sort()
print(random_list)


# date time module

from datetime import datetime, date, time, timedelta

print("today's date:" , date.today())

now = datetime.now()
print("current data and time now:", now)

d = date(2025, 3, 1)
print(d)

t = time(14, 30, 15)
print(t)

dt = datetime(2025, 3, 1, 14, 30)
print(dt)

delta = timedelta(days=7, hours=3)
print(delta)

dt = datetime.strptime("2025-03-01 14:30", "%Y-%m-%d %H:%M")
print(dt)

print("current date time in human readable format", now.strftime("%A, %B %d, %Y at %H:%M"))

print("current year:", now.year)

print("current month:" , now.month)

print("current day:", now.day)

# adding 5 days to the given date
new_dt = dt + timedelta(days=5)
print("new date after adding 5 days:", new_dt)

# importing user defined modules

from Day03.calculator import *

addition = add(2,3)
print(f"result of addition of 2 numbers {addition}")

subraction = sub(2,3)
print(f"result of subraction of 2 numbers {subraction}")

multiplication = mul(2,3)
print(f"result of multiplication of 2 numbers {multiplication}")

division = divide(20,10)
print(f"result of division of 2 numbers {division}")

# lambda functions

add = lambda x, y: x + y

print(f"result of addition of 2 numbers using lambda {add(2,3)}")

maximum_two_numbers = lambda a, b: a if a > b else b

print(f"result of maximum  of 2 numbers using lambda {maximum_two_numbers(6, 9)}")

factorial_num = lambda num: math.factorial(num)

print(f"result of factorial using lambda {factorial_num(6)}")

from functools import reduce

# find the maximum from a list of numbers using lambda

find_max_numbers_list = lambda numbers: reduce(lambda a, b: a if a > b else b, numbers)

given_list = [23, 89, 56, 45, 67]

print(f" maximum from a list using lambda {find_max_numbers_list(given_list)}")

is_prime = lambda number: f"The number {number} is prime" if number > 1 and all(number % i != 0 for i in
                                                                         range(2, int(math.sqrt(
                                                                             number)) + 1)) \
    else f"The number {number} is not prime"

print(f"is_prime using lambda {is_prime(7)}")







