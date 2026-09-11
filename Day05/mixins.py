# MIXINS - Simple and Realistic Examples
# Mixins: Reusable functionality that can be mixed into multiple classes

# ============================================================================
# EXAMPLE 1: TIMESTAMP MIXIN (Most Realistic)
# ============================================================================

print("=" * 80)
print("EXAMPLE 1: Timestamp Mixin")
print("=" * 80)

print("""
Scenario: Add "created_at" and "updated_at" to different classes

Mixin: Provides timestamp functionality
Classes: User, Post, Comment - all need timestamps
""")

from datetime import datetime


class TimestampMixin:
    """Mixin that adds timestamp functionality"""

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_timestamp(self):
        """Update the modified time"""
        self.updated_at = datetime.now()

    def get_age(self):
        """Get how long ago this was created"""
        age = datetime.now() - self.created_at
        return f"{age.seconds} seconds old"


# Classes using TimestampMixin
class User(TimestampMixin):
    """User class with timestamps"""

    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User({self.name}, created: {self.created_at.strftime('%H:%M:%S')})"


class BlogPost(TimestampMixin):
    """Blog post with timestamps"""

    def __init__(self, title, content):
        super().__init__()
        self.title = title
        self.content = content

    def __repr__(self):
        return f"BlogPost({self.title}, created: {self.created_at.strftime('%H:%M:%S')})"


class Comment(TimestampMixin):
    """Comment with timestamps"""

    def __init__(self, author, text):
        super().__init__()
        self.author = author
        self.text = text

    def __repr__(self):
        return f"Comment({self.author}, created: {self.created_at.strftime('%H:%M:%S')})"


# USAGE
print("\nDemo:")
print("-" * 80)

import time

# Create objects
user = User("Alice", "alice@example.com")
print(f"Created: {user}")
print(f"Age: {user.get_age()}")

post = BlogPost("Python Tips", "10 Python tricks...")
print(f"\nCreated: {post}")
print(f"Age: {post.get_age()}")

comment = Comment("Bob", "Great post!")
print(f"\nCreated: {comment}")
print(f"Age: {comment.get_age()}")

# Update and check
time.sleep(1)
post.update_timestamp()
print(f"\nPost updated at: {post.updated_at.strftime('%H:%M:%S')}")
print(f"Updated: {post.get_age()}")

# ============================================================================
# EXAMPLE 2: JSON SERIALIZATION MIXIN
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 2: JSON Serialization Mixin")
print("=" * 80)

print("""
Scenario: Convert different objects to JSON

Mixin: Provides to_json() and from_json()
Classes: User, Product, Order - all need JSON conversion
""")

import json


class JsonSerializableMixin:
    """Mixin that adds JSON serialization"""

    def to_json(self):
        """Convert object to JSON string"""
        return json.dumps(self.__dict__, default=str)

    def to_dict(self):
        """Convert object to dictionary"""
        return self.__dict__


class User(JsonSerializableMixin):
    """User class with JSON support"""

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"User({self.name}, {self.email})"


class Product(JsonSerializableMixin):
    """Product class with JSON support"""

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product({self.name}, ${self.price})"


class Order(JsonSerializableMixin):
    """Order class with JSON support"""

    def __init__(self, order_id, customer, total):
        self.order_id = order_id
        self.customer = customer
        self.total = total

    def __repr__(self):
        return f"Order({self.order_id}, ${self.total})"


# USAGE
print("\nDemo:")
print("-" * 80)

user = User("Alice", "alice@example.com", 28)
print(f"User: {user}")
print(f"JSON: {user.to_json()}")

product = Product("Laptop", 999.99, "Electronics")
print(f"\nProduct: {product}")
print(f"JSON: {product.to_json()}")

order = Order("ORD001", "Alice", 1500)
print(f"\nOrder: {order}")
print(f"JSON: {order.to_json()}")
print(f"Dict: {order.to_dict()}")

# ============================================================================
# EXAMPLE 3: VALIDATION MIXIN
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 3: Validation Mixin")
print("=" * 80)

print("""
Scenario: Validate data in different classes

Mixin: Provides validation functionality
Classes: User, Email, Phone - all need validation
""")


class ValidatorMixin:
    """Mixin that adds validation functionality"""

    def is_valid(self):
        """Check if object is valid"""
        raise NotImplementedError("Subclass must implement is_valid()")

    def validate_or_error(self):
        """Validate and return message"""
        if self.is_valid():
            return "✓ Valid"
        else:
            return "✗ Invalid"


class Email(ValidatorMixin):
    """Email class with validation"""

    def __init__(self, address):
        self.address = address

    def is_valid(self):
        """Check if email is valid"""
        return "@" in self.address and "." in self.address

    def __repr__(self):
        return f"Email({self.address})"


class Phone(ValidatorMixin):
    """Phone class with validation"""

    def __init__(self, number):
        self.number = number

    def is_valid(self):
        """Check if phone is valid (10 digits)"""
        digits = ''.join(c for c in self.number if c.isdigit())
        return len(digits) >= 10

    def __repr__(self):
        return f"Phone({self.number})"


class URL(ValidatorMixin):
    """URL class with validation"""

    def __init__(self, url):
        self.url = url

    def is_valid(self):
        """Check if URL is valid"""
        return self.url.startswith("http://") or self.url.startswith("https://")

    def __repr__(self):
        return f"URL({self.url})"


# USAGE
print("\nDemo:")
print("-" * 80)

email1 = Email("alice@example.com")
print(f"{email1}: {email1.validate_or_error()}")

email2 = Email("invalid-email")
print(f"{email2}: {email2.validate_or_error()}")

phone1 = Phone("555-123-4567")
print(f"\n{phone1}: {phone1.validate_or_error()}")

phone2 = Phone("123")
print(f"{phone2}: {phone2.validate_or_error()}")

url1 = URL("https://github.com")
print(f"\n{url1}: {url1.validate_or_error()}")

url2 = URL("github.com")
print(f"{url2}: {url2.validate_or_error()}")

# ============================================================================
# EXAMPLE 4: CACHING MIXIN
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 4: Caching Mixin")
print("=" * 80)

print("""
Scenario: Cache results of expensive operations

Mixin: Provides caching functionality
Classes: DataFetcher, Calculator - avoid recalculation
""")


class CacheMixin:
    """Mixin that adds caching functionality"""

    def __init__(self):
        self._cache = {}

    def cache_get(self, key):
        """Get value from cache"""
        return self._cache.get(key, None)

    def cache_set(self, key, value):
        """Set value in cache"""
        self._cache[key] = value

    def cache_clear(self):
        """Clear all cache"""
        self._cache.clear()

    def cache_info(self):
        """Show cache contents"""
        return self._cache


class DataFetcher(CacheMixin):
    """Fetches data with caching"""

    def __init__(self):
        super().__init__()
        self.fetch_count = 0

    def fetch_user(self, user_id):
        """Fetch user, use cache if available"""
        # Check cache first
        cached = self.cache_get(f"user_{user_id}")
        if cached:
            print(f"  💾 Cache hit for user {user_id}")
            return cached

        # Fetch from database (simulated)
        self.fetch_count += 1
        print(f"  🔄 Fetching user {user_id} from database (call #{self.fetch_count})")
        user_data = {"id": user_id, "name": f"User{user_id}", "email": f"user{user_id}@example.com"}

        # Store in cache
        self.cache_set(f"user_{user_id}", user_data)
        return user_data


class Calculator(CacheMixin):
    """Calculates values with caching"""

    def __init__(self):
        super().__init__()
        self.calc_count = 0

    def fibonacci(self, n):
        """Calculate fibonacci with caching"""
        # Check cache
        cached = self.cache_get(f"fib_{n}")
        if cached:
            print(f"  💾 Cache hit for fibonacci({n})")
            return cached

        # Calculate
        self.calc_count += 1
        print(f"  🔄 Calculating fibonacci({n}) (call #{self.calc_count})")

        if n <= 1:
            result = n
        else:
            result = self.fibonacci(n - 1) + self.fibonacci(n - 2)

        # Store in cache
        self.cache_set(f"fib_{n}", result)
        return result


# USAGE
print("\nDemo:")
print("-" * 80)

fetcher = DataFetcher()
print("First fetch:")
user1 = fetcher.fetch_user(1)
print(f"Result: {user1}")

print("\nSecond fetch (same user - from cache):")
user1_again = fetcher.fetch_user(1)

print("\nFetch different user:")
user2 = fetcher.fetch_user(2)

print(f"\nCache contents: {fetcher.cache_info()}")

print("\n" + "-" * 80)
print("\nCalculator with caching:")

calc = Calculator()
result = calc.fibonacci(5)
print(f"Result: {result}")

print("\nCache info:")
for key, value in calc.cache_info().items():
    print(f"  {key}: {value}")

# ============================================================================
# EXAMPLE 5: LOGGING MIXIN
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 5: Logging Mixin")
print("=" * 80)

print("""
Scenario: Add logging to different classes

Mixin: Provides logging functionality
Classes: DatabaseConnection, APIClient, FileHandler - all need logging
""")


class LoggingMixin:
    """Mixin that adds logging functionality"""

    def __init__(self):
        self.logs = []

    def log(self, message):
        """Add log message"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        self.logs.append(log_message)
        print(f"  📝 {log_message}")

    def get_logs(self):
        """Get all logs"""
        return self.logs

    def clear_logs(self):
        """Clear all logs"""
        self.logs.clear()


class DatabaseConnection(LoggingMixin):
    """Database connection with logging"""

    def __init__(self, host):
        super().__init__()
        self.host = host

    def connect(self):
        self.log(f"Connecting to {self.host}")
        return "✓ Connected"

    def query(self, sql):
        self.log(f"Executing: {sql}")
        return "Results"

    def disconnect(self):
        self.log(f"Disconnecting from {self.host}")


class APIClient(LoggingMixin):
    """API client with logging"""

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

    def get(self, endpoint):
        self.log(f"GET {self.base_url}/{endpoint}")
        return {"data": "response"}

    def post(self, endpoint, data):
        self.log(f"POST {self.base_url}/{endpoint} with data {data}")
        return {"success": True}


class FileHandler(LoggingMixin):
    """File handler with logging"""

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def read(self):
        self.log(f"Reading file: {self.filename}")
        return "file contents"

    def write(self, content):
        self.log(f"Writing to file: {self.filename}")

    def delete(self):
        self.log(f"Deleting file: {self.filename}")


# USAGE
print("\nDemo:")
print("-" * 80)

print("Database Connection:")
db = DatabaseConnection("localhost:5432")
db.connect()
db.query("SELECT * FROM users")
db.disconnect()

print("\nAPI Client:")
api = APIClient("https://api.example.com")
api.get("users")
api.post("users", {"name": "Alice"})

print("\nFile Handler:")
fh = FileHandler("data.txt")
fh.read()
fh.write("content")
fh.delete()

print("\n" + "-" * 80)
print("All logs from Database:")
for log in db.get_logs():
    print(f"  {log}")

# ============================================================================
# EXAMPLE 6: COMPARISON MIXIN
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 6: Comparison Mixin")
print("=" * 80)

print("""
Scenario: Compare objects by specific attribute

Mixin: Provides comparison methods
Classes: Student, Product, Employee - compare by different attributes
""")


class ComparableMixin:
    """Mixin that adds comparison functionality"""

    def compare_attribute(self, other, attribute):
        """Compare objects by attribute"""
        self_value = getattr(self, attribute)
        other_value = getattr(other, attribute)

        if self_value > other_value:
            return f"{self} > {other}"
        elif self_value < other_value:
            return f"{self} < {other}"
        else:
            return f"{self} == {other}"


class Student(ComparableMixin):
    """Student class"""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student({self.name}, grade={self.grade})"


class Product(ComparableMixin):
    """Product class"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.name}, ${self.price})"


class Employee(ComparableMixin):
    """Employee class"""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.name}, ${self.salary})"


# USAGE
print("\nDemo:")
print("-" * 80)

alice = Student("Alice", 95)
bob = Student("Bob", 87)
print("Compare by grade:")
print(alice.compare_attribute(bob, "grade"))

print("\nCompare products by price:")
laptop = Product("Laptop", 999)
mouse = Product("Mouse", 25)
print(laptop.compare_attribute(mouse, "price"))

print("\nCompare employees by salary:")
emp1 = Employee("Alice", 80000)
emp2 = Employee("Bob", 95000)
print(emp2.compare_attribute(emp1, "salary"))

# ============================================================================
# MULTIPLE MIXINS - COMBINING POWERS
# ============================================================================

print("\n\n" + "=" * 80)
print("MULTIPLE MIXINS - Combining Powers")
print("=" * 80)

print("""
Scenario: Use multiple mixins in one class

Mixins: TimestampMixin + JsonSerializableMixin + LoggingMixin
Result: Class with timestamps, JSON, and logging
""")


class Article(TimestampMixin, JsonSerializableMixin, LoggingMixin):
    """Article with multiple mixins"""

    def __init__(self, title, content, author):
        TimestampMixin.__init__(self)
        LoggingMixin.__init__(self)
        self.title = title
        self.content = content
        self.author = author

    def publish(self):
        self.log(f"Publishing article: {self.title}")
        self.update_timestamp()

    def __repr__(self):
        return f"Article({self.title})"


# USAGE
print("\nDemo:")
print("-" * 80)

article = Article("Python Mixins", "Mixins are great...", "Alice")
print(f"Created: {article}")
print(f"Created at: {article.created_at.strftime('%H:%M:%S')}")

article.publish()

print(f"\nJSON: {article.to_json()}")
print(f"\nLogs:")
for log in article.get_logs():
    print(f"  {log}")

# ============================================================================
# COMPARISON: WITH vs WITHOUT MIXIN
# ============================================================================

print("\n\n" + "=" * 80)
print("COMPARISON: With vs Without Mixin")
print("=" * 80)

print("""
WITHOUT MIXIN (Code Duplication):
─────────────────────────────────
class User:
    def __init__(self, name):
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_json(self):
        return json.dumps(self.__dict__)

    def log(self, message):
        self.logs.append(message)

class Post:
    def __init__(self, title):
        self.title = title
        self.created_at = datetime.now()  # REPEATED
        self.updated_at = datetime.now()  # REPEATED

    def to_json(self):              # REPEATED
        return json.dumps(self.__dict__)

    def log(self, message):         # REPEATED
        self.logs.append(message)

Problems:
✗ Code duplication
✗ Hard to maintain
✗ Changes needed in multiple places
✗ Violates DRY principle


WITH MIXIN (Code Reuse):
───────────────────────
class TimestampMixin:
    def __init__(self):
        self.created_at = datetime.now()

class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class LoggingMixin:
    def log(self, message):
        self.logs.append(message)

class User(TimestampMixin, JsonSerializableMixin, LoggingMixin):
    pass

class Post(TimestampMixin, JsonSerializableMixin, LoggingMixin):
    pass

Benefits:
✓ No code duplication
✓ Easy to maintain
✓ Change once, applies everywhere
✓ Follows DRY principle
✓ Reusable across classes
""")

# ============================================================================
# WHEN TO USE MIXINS
# ============================================================================

print("\n" + "=" * 80)
print("WHEN TO USE MIXINS")
print("=" * 80)

print("""
Use Mixins when:

1. Multiple classes need same functionality
   Example: Timestamps for User, Post, Comment

2. Functionality is independent
   Example: Logging doesn't depend on core logic

3. Avoid code duplication
   Example: Write once, use in many classes

4. Functionality is optional
   Example: Some classes need caching, some don't

5. Combine multiple features
   Example: Class with timestamps + JSON + logging

6. Keep classes focused
   Example: UserModel focuses on user logic, not timestamps


Real-world examples:
✓ Django models (TimestampField mixin)
✓ SQLAlchemy (declarative base mixins)
✓ Timestamp tracking
✓ Audit logging
✓ JSON serialization
✓ Caching
✓ Validation
✓ Permission checking
✓ Soft deletes
✓ Slug generation
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)

print("""
1. MIXIN: Reusable class providing functionality
   - Not meant to be used alone
   - Mixed into other classes
   - Example: TimestampMixin adds timestamps

2. HOW TO USE:
   class MyClass(MyMixin, AnotherMixin):
       pass

3. BENEFITS:
   ✓ Code reuse
   ✓ Avoid duplication
   ✓ Keep classes focused
   ✓ Composable functionality
   ✓ Easy to maintain

4. COMMON MIXINS:
   - TimestampMixin: created_at, updated_at
   - JsonSerializableMixin: to_json(), from_json()
   - LoggingMixin: log() method
   - CacheMixin: cache_get(), cache_set()
   - ValidatorMixin: is_valid()
   - ComparableMixin: Compare objects

5. vs INHERITANCE:
   - Inheritance: IS-A relationship
   - Mixin: HAS-A relationship (functionality)

6. vs COMPOSITION:
   - Composition: Contains object
   - Mixin: Inherits functionality

7. MRO (Method Resolution Order):
   - Python checks methods in order: left to right
   - Use super() for proper MRO
""")
