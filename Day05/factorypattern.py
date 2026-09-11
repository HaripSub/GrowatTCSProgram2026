# FACTORY PATTERN - Simple and Realistic Examples
# Factory creates objects WITHOUT needing to know their exact class

# ============================================================================
# EXAMPLE 1: PAYMENT METHOD FACTORY (Most Realistic)
# ============================================================================

print("=" * 80)
print("EXAMPLE 1: Payment Method Factory")
print("=" * 80)


class Payment:
    """Base payment class"""

    def pay(self, amount):
        raise NotImplementedError("Subclass must implement pay()")


class CreditCard(Payment):
    """Credit card payment"""

    def pay(self, amount):
        return f"💳 Paid ${amount} with Credit Card"


class PayPal(Payment):
    """PayPal payment"""

    def pay(self, amount):
        return f"🅿️  Paid ${amount} with PayPal"


class Bitcoin(Payment):
    """Bitcoin payment"""

    def pay(self, amount):
        return f"₿ Paid ${amount} with Bitcoin"


# FACTORY FUNCTION - Creates payment objects
def create_payment(payment_type):
    """Factory function - creates right payment object"""
    if payment_type == "credit_card":
        return CreditCard()
    elif payment_type == "paypal":
        return PayPal()
    elif payment_type == "bitcoin":
        return Bitcoin()
    else:
        raise ValueError(f"Unknown payment type: {payment_type}")


# USAGE
print("\nWithout factory (bad way):")
print("-" * 80)
# You need to know which class to create
payment1 = CreditCard()
payment2 = PayPal()
payment3 = Bitcoin()
print(f"payment1: {payment1}")
print(f"payment2: {payment2}")
print(f"payment3: {payment3}")
print("Problem: You must know each class name!")

print("\n\nWith factory (good way):")
print("-" * 80)
# Factory creates based on type string
payment_type = input("Enter payment method (credit_card/paypal/bitcoin): ") or "credit_card"

payment = create_payment(payment_type)
print(payment.pay(100))
print("✓ No need to know class names!")

# ============================================================================
# EXAMPLE 2: DATABASE FACTORY
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 2: Database Connection Factory")
print("=" * 80)


class Database:
    """Base database class"""

    def connect(self):
        raise NotImplementedError("Subclass must implement connect()")

    def query(self, sql):
        raise NotImplementedError("Subclass must implement query()")


class PostgreSQL(Database):
    """PostgreSQL database"""

    def connect(self):
        return "✓ Connected to PostgreSQL"

    def query(self, sql):
        return f"PostgreSQL: Executing {sql}"


class MySQL(Database):
    """MySQL database"""

    def connect(self):
        return "✓ Connected to MySQL"

    def query(self, sql):
        return f"MySQL: Executing {sql}"


class MongoDB(Database):
    """MongoDB database"""

    def connect(self):
        return "✓ Connected to MongoDB"

    def query(self, sql):
        return f"MongoDB: Executing {sql}"


# FACTORY CLASS - Creates database objects
class DatabaseFactory:
    """Factory class - creates right database"""

    @staticmethod
    def create(db_type):
        """Create database based on type"""
        if db_type == "postgresql":
            return PostgreSQL()
        elif db_type == "mysql":
            return MySQL()
        elif db_type == "mongodb":
            return MongoDB()
        else:
            raise ValueError(f"Unknown database: {db_type}")


# USAGE
print("\nCreating different databases:")
print("-" * 80)

databases = [
    DatabaseFactory.create("postgresql"),
    DatabaseFactory.create("mysql"),
    DatabaseFactory.create("mongodb")
]

for db in databases:
    print(db.connect())
    print(db.query("SELECT * FROM users"))
    print()

# ============================================================================
# EXAMPLE 3: NOTIFICATION FACTORY (Email, SMS, Push)
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 3: Notification Factory")
print("=" * 80)


class Notification:
    """Base notification class"""

    def send(self, message, recipient):
        raise NotImplementedError("Subclass must implement send()")


class EmailNotification(Notification):
    """Send email"""

    def send(self, message, recipient):
        return f"📧 Email sent to {recipient}: {message}"


class SMSNotification(Notification):
    """Send SMS"""

    def send(self, message, recipient):
        return f"📱 SMS sent to {recipient}: {message}"


class PushNotification(Notification):
    """Send push notification"""

    def send(self, message, recipient):
        return f"🔔 Push sent to {recipient}: {message}"


# FACTORY FUNCTION
def create_notification(notification_type):
    """Factory - creates notification"""
    notifications = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification
    }

    if notification_type not in notifications:
        raise ValueError(f"Unknown notification: {notification_type}")

    return notifications[notification_type]()


# USAGE
print("\nSending different notifications:")
print("-" * 80)

notification_types = ["email", "sms", "push"]

for notif_type in notification_types:
    notif = create_notification(notif_type)
    print(notif.send("Hello!", "user@example.com"))

# ============================================================================
# EXAMPLE 4: DOCUMENT FACTORY (PDF, Word, Excel)
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 4: Document Factory")
print("=" * 80)


class Document:
    """Base document class"""

    def create(self):
        raise NotImplementedError("Subclass must implement create()")

    def save(self):
        raise NotImplementedError("Subclass must implement save()")


class PDFDocument(Document):
    """PDF document"""

    def create(self):
        return "📄 Creating PDF document..."

    def save(self):
        return "💾 Saved as .pdf"


class WordDocument(Document):
    """Word document"""

    def create(self):
        return "📝 Creating Word document..."

    def save(self):
        return "💾 Saved as .docx"


class ExcelDocument(Document):
    """Excel spreadsheet"""

    def create(self):
        return "📊 Creating Excel document..."

    def save(self):
        return "💾 Saved as .xlsx"


# FACTORY CLASS
class DocumentFactory:
    """Factory - creates documents"""

    _types = {
        "pdf": PDFDocument,
        "word": WordDocument,
        "excel": ExcelDocument
    }

    @classmethod
    def create(cls, doc_type):
        """Create document based on type"""
        if doc_type not in cls._types:
            raise ValueError(f"Unknown document: {doc_type}")

        return cls._types[doc_type]()


# USAGE
print("\nCreating different documents:")
print("-" * 80)

doc_types = ["pdf", "word", "excel"]

for doc_type in doc_types:
    doc = DocumentFactory.create(doc_type)
    print(doc.create())
    print(doc.save())
    print()

# ============================================================================
# EXAMPLE 5: TRANSPORTATION FACTORY
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 5: Transportation Factory")
print("=" * 80)


class Transport:
    """Base transport class"""

    def deliver(self, package):
        raise NotImplementedError("Subclass must implement deliver()")

    def get_cost(self, distance):
        raise NotImplementedError("Subclass must implement get_cost()")


class Truck(Transport):
    """Truck delivery"""

    def deliver(self, package):
        return f"🚚 Delivering {package} by truck"

    def get_cost(self, distance):
        return f"Cost: ${distance * 0.5} (Truck)"


class Plane(Transport):
    """Plane delivery"""

    def deliver(self, package):
        return f"✈️  Delivering {package} by plane"

    def get_cost(self, distance):
        return f"Cost: ${distance * 2.0} (Plane)"


class Ship(Transport):
    """Ship delivery"""

    def deliver(self, package):
        return f"🚢 Delivering {package} by ship"

    def get_cost(self, distance):
        return f"Cost: ${distance * 0.2} (Ship)"


# FACTORY FUNCTION
def create_transport(transport_type):
    """Factory - creates transport"""
    transports = {
        "truck": Truck,
        "plane": Plane,
        "ship": Ship
    }

    if transport_type not in transports:
        raise ValueError(f"Unknown transport: {transport_type}")

    return transports[transport_type]()


# USAGE
print("\nShipping packages:")
print("-" * 80)

shipments = [
    ("truck", "Local package", 50),
    ("plane", "Express package", 1000),
    ("ship", "Bulk package", 5000)
]

for transport_type, package, distance in shipments:
    transport = create_transport(transport_type)
    print(transport.deliver(package))
    print(transport.get_cost(distance))
    print()

# ============================================================================
# COMPARISON: WITH vs WITHOUT FACTORY
# ============================================================================

print("\n" + "=" * 80)
print("COMPARISON: With vs Without Factory")
print("=" * 80)

print("""
WITHOUT FACTORY (Bad Way):
─────────────────────────
if user_choice == "credit_card":
    payment = CreditCard()
elif user_choice == "paypal":
    payment = PayPal()
elif user_choice == "bitcoin":
    payment = Bitcoin()
else:
    raise ValueError("Unknown payment")

Problems:
✗ Code is repetitive
✗ Need to add new if-else for each type
✗ Scattered everywhere in code
✗ Hard to maintain


WITH FACTORY (Good Way):
───────────────────────
payment = create_payment(user_choice)

Benefits:
✓ Clean and simple
✓ Easy to add new types
✓ Factory handles all logic
✓ Easy to maintain
✓ One place to change
""")

# ============================================================================
# WHEN TO USE FACTORY PATTERN
# ============================================================================

print("\n" + "=" * 80)
print("WHEN TO USE FACTORY PATTERN")
print("=" * 80)

print("""
Use Factory Pattern when:

1. Multiple similar classes exist
   Example: CreditCard, PayPal, Bitcoin

2. Creation logic depends on input
   Example: Different database based on config

3. You want to hide object creation details
   Example: User doesn't need to know CreditCard class

4. You need to add new types easily
   Example: Add new payment method without changing existing code

5. You want centralized object creation
   Example: One place to manage all payment types


Real-world examples:
✓ Payment processors (Stripe, PayPal, Square)
✓ Database connectors (MySQL, PostgreSQL, MongoDB)
✓ File formats (PDF, Excel, Word)
✓ Notification systems (Email, SMS, Push)
✓ Cloud providers (AWS, Google Cloud, Azure)
✓ Web drivers (Chrome, Firefox, Safari)
✓ Cache systems (Redis, Memcached)
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)

print("""
1. Factory Pattern creates objects
   → Without knowing exact class names
   → Based on type/configuration

2. Two ways to implement:
   → Factory Function: create_payment(type)
   → Factory Class: DatabaseFactory.create(type)

3. Steps:
   1. Create base class (Payment)
   2. Create subclasses (CreditCard, PayPal, Bitcoin)
   3. Create factory that returns correct subclass
   4. Use factory instead of creating directly

4. Benefits:
   ✓ Clean code
   ✓ Easy to maintain
   ✓ Easy to extend
   ✓ Hide implementation details
   ✓ Centralized creation logic

5. Key advantage:
   Add new payment method → Only change factory
   Don't change other parts of code!
""")
