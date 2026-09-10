from abc import ABC, abstractmethod
import math


# Base class (Abstract class)
class Shape(ABC):
    """Abstract base class for all shapes"""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        pass

    def display_info(self):
        """Display shape information"""
        print(f"{self.__class__.__name__}")
        print(f"  Area: {self.area():.2f}")
        print(f"  Perimeter: {self.perimeter():.2f}")
        print()


# Circle class
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Rectangle class
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Triangle class
class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        # Using Heron's formula
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


# Square class (inherits from Rectangle)
class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)


# Main program demonstrating polymorphism
if __name__ == "__main__":
    # Create different shape objects
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
        Square(5)
    ]

    print("=" * 40)
    print("POLYMORPHISM: AREA OF SHAPES")
    print("=" * 40)
    print()

    # Polymorphic behavior: same method call, different implementations
    for shape in shapes:
        shape.display_info()

    # Calculate total area
    total_area = sum(shape.area() for shape in shapes)
    print("=" * 40)
    print(f"Total Area of all shapes: {total_area:.2f}")
    print("=" * 40)
    total_perimeter = sum(shape.perimeter() for shape in shapes)
    print("=" * 40)
    print(f"Total perimeter if all shapes {total_perimeter:.2f}")
    print("=" * 40)
