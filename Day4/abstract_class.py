from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_info(self):
        pass


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Course: {self.course}")


class Employee(Person):
    def __init__(self, name, age, employee_id, occupation):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.occupation = occupation

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Occupation: {self.occupation}")


# Creating objects
student = Student("Bob", 21, "S12345", "Computer Science")
employee = Employee("Dr. Smith", 50, "E98765", "Doctor")

# List of persons
persons = [student, employee]

# Demonstrating abstraction
for p in persons:
    p.display_info()