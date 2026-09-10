class Person:
    def __init__(self, name, age, occupation, city):
        self.name = name  # Attribute
        self.age = age  # Attribute
        self.occupation = occupation  # Attribute
        self.city = city  # Attribute

    def print_details(self):
        print(
            f"The given person name is: {self.name}, is of age: {self.age}, works as: {self.occupation}, and is from: {self.city}")

    # Method to get person's information as a dictionary
    def to_dict(self):
        """Returns person's information as a dictionary"""
        return {
            'Name': self.name,
            'Age': self.age,
            'Occupation': self.occupation,
            'City':self.city
        }


    # Method to check if person is an adult
    def is_adult(self):
        """Returns True if person is 18 or older"""
        return self.age >= 18

    # Method to check if person is a senior (65+)
    def is_senior(self):
        """Returns True if person is 65 or older"""
        return self.age >= 65

    # Method to update person's occupation
    def update_occupation(self, new_occupation):
        """Updates person's occupation"""
        old_occupation = self.occupation
        self.occupation = new_occupation
        print(f"{self.name}'s occupation updated from {old_occupation} to {new_occupation}")

    # Method to update person's city
    def update_city(self, new_city):
        """Updates person's city"""
        old_city = self.city
        self.city = new_city
        print(f"{self.name} moved from {old_city} to {new_city}")

    def is_valid(self):
        """Validates if all person attributes are valid and returns detailed feedback"""
        errors = []

        # Validate name
        if not isinstance(self.name, str):
            errors.append("Name must be a string")
        elif len(self.name) == 0:
            errors.append("Name cannot be empty")
        elif len(self.name) < 2:
            errors.append("Name must be at least 2 characters long")

        # Validate age
        if not isinstance(self.age, int):
            errors.append("Age must be an integer")
        elif self.age < 0:
            errors.append("Age cannot be negative")
        elif self.age > 100:
            errors.append("Age cannot exceed 100 years")

        # Validate occupation
        if not isinstance(self.occupation, str):
            errors.append("Occupation must be a string")
        elif len(self.occupation) == 0:
            errors.append("Occupation cannot be empty")
        elif len(self.occupation) < 2:
            errors.append("Occupation must be at least 2 characters long")

        # Validate city
        if not isinstance(self.city, str):
            errors.append("City must be a string")
        elif len(self.city) == 0:
            errors.append("City cannot be empty")
        elif len(self.city) < 2:
            errors.append("City must be at least 2 characters long")

        # Return validation result with messages
        if errors:
            return {
                'is_valid': False,
                'errors': errors,
                'error_count': len(errors),
                'message': f"Validation failed with {len(errors)} error(s)"
            }
        else:
            return {
                'is_valid': True,
                'errors': [],
                'error_count': 0,
                'message': "All attributes are valid"
            }

    def print_validation_report(self):
        """Prints a detailed validation report"""
        result = self.is_valid()

        print("\n" + "=" * 50)
        print(f"VALIDATION REPORT FOR: {self.name}")
        print("=" * 50)

        if result['is_valid']:
            print("✓ Status: VALID")
            print("✓ All attributes passed validation")
        else:
            print("✗ Status: INVALID")
            print(f"✗ Found {result['error_count']} error(s):\n")
            for idx, error in enumerate(result['errors'], 1):
                print(f"  {idx}. {error}")

        print("=" * 50 + "\n")

    def __str__(self):
        """String representation of Person object"""
        return f"{self.name} ({self.age} years old) - {self.occupation} from {self.city}"


    def __repr__(self):
        """Object representation of Person"""
        return f"Person(Name='{self.name}', Age={self.age}, Occupation='{self.occupation}', City='{self.city}')"


# creating an object for person class

p= Person("Alice",102,"Doctor","Paris")
# Demonstrate new methods
print("\n--- Demonstrating New Methods ---")
print(f"\nUsing new methods for {p.name}:")
print(f"String representation: {str(p)}")
print(f"Object representation: {repr(p)}")
print(f"Dictionary representation: {p.to_dict()}")
print(f"Is adult: {p.is_adult()}")
print(f"Is senior: {p.is_senior()}")
print(f"Is valid: {p.is_valid()}")
p.print_validation_report()
