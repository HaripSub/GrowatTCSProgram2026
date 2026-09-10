class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    def get_name(self):
        return self.__name  # Public method to access private attribute

    def get_age(self):
        return self.__age  # Public method to access private attribute

    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age  # Public method to modify private attribute


# Creating an object
person = Person("Alice", 30)

print(person.get_name())  # Output: Alice
print(person.get_age())  # Output: 30
person.set_age(31)
print(person.get_age())  # Output: 31