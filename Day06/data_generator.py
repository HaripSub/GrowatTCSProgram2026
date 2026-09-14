import csv
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of records
num_records = 10

# Define the output file
output_file = "person_data.csv"

# Define the field names
fieldnames = ['id', 'name', 'age', 'location', 'gender', 'occupation']

cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "San Francisco", "Seattle", "Denver", "Washington", "Boston"
]

genders = ['Male', 'Female']

# Define occupation rules based on age
occupation_rules = [
    (range(1, 5), ["Baby"]),
    (range(5, 17), ["School Student"]),
    (range(17, 25), ["College Student"]),
    (range(25, 66), ["Engineer", "Doctor", "Lawyer", "Shop Owner", "Pharmacist", "Accountant", "Bank Manager"]),
    (range(66, 101), ["Retired"])
]


def get_occupation(age):
    for age_range, occupations in occupation_rules:
        if age in age_range:
            return random.choice(occupations)
    return "Unknown"


# Open the CSV file for writing
with open(output_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # Generate the data
    for i in range(1, num_records + 1):
        age = fake.random_int(min=1, max=100)
        occupation = get_occupation(age)
        writer.writerow({
            'id': i,
            'name': fake.name(),
            'age': age,
            'location': random.choice(cities),
            'gender': random.choice(genders),
            'occupation': occupation
        })

print(f"Generated {num_records} records and saved to {output_file}")