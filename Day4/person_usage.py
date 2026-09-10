# Creating a list of persons
from person import Person

persons = []

# Get number of persons to add
num_persons = int(input("How many persons do you want to add? "))

# Create multiple person objects
for i in range(num_persons):
    print(f"\n--- Person {i + 1} ---")
    name = input("Enter the name of the person: ")
    age = int(input("Enter the age of the person: "))
    occupation = input("Enter the occupation of the person: ")
    city = input("Enter the city of the person: ")

    person = Person(name, age, occupation, city)
    persons.append(person)

# Display all persons
print("\n--- All Persons ---")
for idx, person in enumerate(persons, 1):
    print(f"\nPerson {idx}:")
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    print(f"Occupation: {person.occupation}")
    print(f"City: {person.city}")
    person.print_details()

# Filter persons with age greater than 30
print("\n--- Persons with Age > 30 ---")
filtered_persons = [person for person in persons if person.age > 30]

if filtered_persons:
    for idx, person in enumerate(filtered_persons, 1):
        print(f"Name: {person.name}")
        print(f"Age: {person.age}")
        print(f"Occupation: {person.occupation}")
        print(f"City: {person.city}")
else:
    print("No persons found with age greater than 30")

# Filter and count Engineers
print("\n--- Engineers Count ---")
engineers = [person for person in persons if person.occupation.lower() == "engineer"]

print(f"Total number of Engineers: {len(engineers)}")

if engineers:
    print("\nEngineers:")
    for idx, person in enumerate(engineers, 1):
        print(f"\n{idx}. Name: {person.name}, Age: {person.age}, City: {person.city}")
else:
    print("No engineers found")

# Filter and count persons from Paris
print("\n--- Persons from Paris Count ---")
paris_persons = [person for person in persons if person.city.lower() == "paris"]

print(f"Total number of persons from Paris: {len(paris_persons)}")

if paris_persons:
    print("\nPersons from Paris:")
    for idx, person in enumerate(paris_persons, 1):
        print(f"\n{idx}. Name: {person.name}, Age: {person.age}, Occupation: {person.occupation}")
else:
    print("No persons found from Paris")