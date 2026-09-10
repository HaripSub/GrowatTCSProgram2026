class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def display_info(self):
        print(f"Name: {self._name}, Age: {self._age}")

    def __str__(self):
        return f"Person(Name: {self._name}, Age: {self._age})"

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str, course: str):
        super().__init__(name, age)
        self._student_id = student_id
        self._course = course

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self._student_id}, Course: {self._course}")

    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, Student ID: {self._student_id}, Course: {self._course})"

    @property
    def student_id(self):
        return self._student_id

    @property
    def course(self):
        return self._course


class Teacher(Person):
    def __init__(self, name: str, age: int, employee_id: str, subject: str):
        super().__init__(name, age)
        self._employee_id = employee_id
        self._subject = subject

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self._employee_id}, Subject: {self._subject}")

    def __str__(self):
        return f"Teacher(Name: {self.name}, Age: {self.age}, Employee ID: {self._employee_id}, Subject: {self._subject})"

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def subject(self):
        return self._subject


# Creating objects
person = Person("Alice", 45)
student = Student("Bob", 21, "S12345", "Computer Science")
teacher = Teacher("Dr. Smith", 50, "T98765", "Mathematics")

# List of persons
persons = [person, student, teacher]

# Demonstrating polymorphism
for p in persons:
    p.display_info()

# Demonstrating __str__ method
for p in persons:
    print(str(p))