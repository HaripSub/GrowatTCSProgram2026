class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}, Course: {self.course}")


class Employee(Person):
    def __init__(self, name, age, employee_id, occupation):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.occupation = occupation

    def display(self):
        super().display()
        print(f"EmployeeID: {self.employee_id}, Occupation: {self.occupation}")


# Creating a Person object
person = Person("Alice", 45)
person.display()
# Output:
# Name: Alice, Age: 45

# Creating a Student object
student = Student("Bob", 21, "S12345", "Computer Science")
student.display()

# Creating a Employee object
employee = Employee("Charlie", 31, "E14567", "Engineer")
employee.display()