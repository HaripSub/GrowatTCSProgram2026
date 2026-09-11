# ENUMS IN PYTHON - Simple and Realistic Examples
# Enum: A set of symbolic names (members) bound to unique, constant values

# ============================================================================
# EXAMPLE 1: COLOR ENUM (Simplest Example)
# ============================================================================

print("=" * 80)
print("EXAMPLE 1: Color Enum (Simplest Example)")
print("=" * 80)

from enum import Enum

print("""
Scenario: Define colors in an organized way

Without Enum (Bad):
  RED = 1
  GREEN = 2
  BLUE = 3
  Problem: Easy to use wrong value, no validation

With Enum (Good):
  class Color(Enum):
      RED = 1
      GREEN = 2
      BLUE = 3

  Benefit: Type-safe, self-documenting
""")


class Color(Enum):
    """Simple color enum"""
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    BLACK = 5
    WHITE = 6


# USAGE
print("\nDemo:")
print("-" * 80)

# Access enum members
print(f"Red color: {Color.RED}")
print(f"Red name: {Color.RED.name}")
print(f"Red value: {Color.RED.value}")

# Iterate through enum
print("\nAll colors:")
for color in Color:
    print(f"  {color.name} = {color.value}")

# Compare enums
print(f"\nColor.RED == Color.RED: {Color.RED == Color.RED}")
print(f"Color.RED == Color.BLUE: {Color.RED == Color.BLUE}")

# Access by value
print(f"\nColor by value 2: {Color(2)}")

# ============================================================================
# EXAMPLE 2: USER STATUS ENUM (Most Realistic)
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 2: User Status Enum")
print("=" * 80)

print("""
Scenario: Track user account status

Statuses: active, inactive, suspended, deleted
Instead of: "active", "Active", "ACTIVE" (inconsistent)
Use Enum: Ensures consistency and prevents typos
""")


class UserStatus(Enum):
    """User account status"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DELETED = "deleted"


class User:
    """User with status enum"""

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.status = UserStatus.ACTIVE

    def suspend(self):
        """Suspend the user"""
        self.status = UserStatus.SUSPENDED

    def reactivate(self):
        """Reactivate the user"""
        self.status = UserStatus.ACTIVE

    def delete(self):
        """Delete the user"""
        self.status = UserStatus.DELETED

    def is_active(self):
        """Check if user is active"""
        return self.status == UserStatus.ACTIVE

    def __repr__(self):
        return f"User({self.name}, {self.status.value})"


# USAGE
print("\nDemo:")
print("-" * 80)

user = User("Alice", "alice@example.com")
print(f"Created: {user}")
print(f"Is active: {user.is_active()}")

user.suspend()
print(f"\nAfter suspension: {user}")
print(f"Is active: {user.is_active()}")

user.reactivate()
print(f"\nAfter reactivation: {user}")
print(f"Is active: {user.is_active()}")

# ============================================================================
# EXAMPLE 3: ORDER STATUS ENUM (E-commerce)
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 3: Order Status Enum (E-commerce)")
print("=" * 80)

print("""
Scenario: Track order lifecycle

Statuses: pending, processing, shipped, delivered, cancelled
Use Enum to ensure consistency in order tracking
""")


class OrderStatus(Enum):
    """Order status in e-commerce"""
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order:
    """Order with status"""

    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
        self.status = OrderStatus.PENDING

    def process(self):
        """Move to processing"""
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.PROCESSING
            return "✓ Order is being processed"
        return "✗ Cannot process order"

    def ship(self):
        """Ship the order"""
        if self.status == OrderStatus.PROCESSING:
            self.status = OrderStatus.SHIPPED
            return "📦 Order shipped"
        return "✗ Cannot ship order"

    def deliver(self):
        """Deliver the order"""
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            return "✓ Order delivered"
        return "✗ Cannot deliver order"

    def cancel(self):
        """Cancel the order"""
        if self.status in [OrderStatus.PENDING, OrderStatus.PROCESSING]:
            self.status = OrderStatus.CANCELLED
            return "✗ Order cancelled"
        return "✗ Cannot cancel order"

    def __repr__(self):
        return f"Order({self.order_id}, {self.status.value})"


# USAGE
print("\nDemo:")
print("-" * 80)

order = Order("ORD001", 150)
print(f"Created: {order}")

print(f"\n{order.process()}")
print(f"Status: {order}")

print(f"\n{order.ship()}")
print(f"Status: {order}")

print(f"\n{order.deliver()}")
print(f"Status: {order}")

# ============================================================================
# EXAMPLE 4: PAYMENT METHOD ENUM
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 4: Payment Method Enum")
print("=" * 80)

print("""
Scenario: Different payment methods

Methods: credit_card, debit_card, paypal, crypto, bank_transfer
Use Enum to validate payment method
""")


class PaymentMethod(Enum):
    """Payment methods available"""
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    CRYPTOCURRENCY = "crypto"
    BANK_TRANSFER = "bank_transfer"
    APPLE_PAY = "apple_pay"


class Payment:
    """Payment with method"""

    def __init__(self, amount, method):
        self.amount = amount
        self.method = method

    def get_fee(self):
        """Get payment fee based on method"""
        fees = {
            PaymentMethod.CREDIT_CARD: 0.029,  # 2.9%
            PaymentMethod.DEBIT_CARD: 0.015,  # 1.5%
            PaymentMethod.PAYPAL: 0.034,  # 3.4%
            PaymentMethod.CRYPTOCURRENCY: 0.001,  # 0.1%
            PaymentMethod.BANK_TRANSFER: 0.005,  # 0.5%
            PaymentMethod.APPLE_PAY: 0.015,  # 1.5%
        }
        return self.amount * fees.get(self.method, 0)

    def process(self):
        """Process payment"""
        fee = self.get_fee()
        total = self.amount + fee
        return f"💰 Paid ${self.amount} via {self.method.value} (fee: ${fee:.2f}, total: ${total:.2f})"

    def __repr__(self):
        return f"Payment(${self.amount}, {self.method.value})"


# USAGE
print("\nDemo:")
print("-" * 80)

payments = [
    Payment(100, PaymentMethod.CREDIT_CARD),
    Payment(100, PaymentMethod.CRYPTOCURRENCY),
    Payment(100, PaymentMethod.BANK_TRANSFER),
]

for payment in payments:
    print(f"{payment}")
    print(f"  {payment.process()}\n")

# ============================================================================
# EXAMPLE 5: HTTP STATUS CODE ENUM
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 5: HTTP Status Code Enum")
print("=" * 80)

print("""
Scenario: Different HTTP response status codes

Codes: 200 OK, 400 Bad Request, 404 Not Found, 500 Server Error, etc
Use Enum to make responses type-safe
""")


class HTTPStatus(Enum):
    """HTTP status codes"""
    OK = (200, "OK")
    CREATED = (201, "Created")
    BAD_REQUEST = (400, "Bad Request")
    UNAUTHORIZED = (401, "Unauthorized")
    FORBIDDEN = (403, "Forbidden")
    NOT_FOUND = (404, "Not Found")
    INTERNAL_SERVER_ERROR = (500, "Internal Server Error")
    SERVICE_UNAVAILABLE = (503, "Service Unavailable")

    @property
    def code(self):
        """Get status code"""
        return self.value[0]

    @property
    def message(self):
        """Get status message"""
        return self.value[1]


class Response:
    """API response"""

    def __init__(self, data, status):
        self.data = data
        self.status = status

    def to_dict(self):
        """Convert to dictionary"""
        return {
            "code": self.status.code,
            "message": self.status.message,
            "data": self.data
        }

    def __repr__(self):
        return f"Response({self.status.code}, {self.data})"


# USAGE
print("\nDemo:")
print("-" * 80)

responses = [
    Response({"id": 1, "name": "Alice"}, HTTPStatus.OK),
    Response({"error": "Invalid input"}, HTTPStatus.BAD_REQUEST),
    Response(None, HTTPStatus.NOT_FOUND),
    Response({"error": "Server error"}, HTTPStatus.INTERNAL_SERVER_ERROR),
]

for response in responses:
    print(f"{response}")
    print(f"  Status: {response.status.code} {response.status.message}")
    print(f"  Response: {response.to_dict()}\n")

# ============================================================================
# EXAMPLE 6: LOG LEVEL ENUM
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 6: Log Level Enum")
print("=" * 80)

print("""
Scenario: Different logging levels

Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
Use Enum to standardize logging
""")


class LogLevel(Enum):
    """Logging levels"""
    DEBUG = (1, "🐛")
    INFO = (2, "ℹ️")
    WARNING = (3, "⚠️")
    ERROR = (4, "❌")
    CRITICAL = (5, "🔥")

    @property
    def priority(self):
        """Get priority level"""
        return self.value[0]

    @property
    def icon(self):
        """Get emoji icon"""
        return self.value[1]


class Logger:
    """Logger with levels"""

    def __init__(self, name):
        self.name = name
        self.min_level = LogLevel.DEBUG
        self.logs = []

    def set_level(self, level):
        """Set minimum logging level"""
        self.min_level = level

    def _log(self, level, message):
        """Internal logging method"""
        if level.priority >= self.min_level.priority:
            log_message = f"{level.icon} [{level.name}] {message}"
            self.logs.append(log_message)
            print(f"  {log_message}")

    def debug(self, message):
        self._log(LogLevel.DEBUG, message)

    def info(self, message):
        self._log(LogLevel.INFO, message)

    def warning(self, message):
        self._log(LogLevel.WARNING, message)

    def error(self, message):
        self._log(LogLevel.ERROR, message)

    def critical(self, message):
        self._log(LogLevel.CRITICAL, message)


# USAGE
print("\nDemo:")
print("-" * 80)

logger = Logger("MyApp")

print("Logging at all levels:")
logger.debug("Application started")
logger.info("Processing request")
logger.warning("Memory usage high")
logger.error("Database connection failed")
logger.critical("System shutdown")

print("\n\nLogging with WARNING level and above:")
logger2 = Logger("MyApp2")
logger2.set_level(LogLevel.WARNING)
logger2.debug("This won't be logged")
logger2.info("This won't be logged either")
logger2.warning("But this will be logged")
logger2.error("And this will be logged")

# ============================================================================
# EXAMPLE 7: PERMISSION ENUM
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 7: Permission Enum (Flags)")
print("=" * 80)

print("""
Scenario: User permissions that can be combined

Permissions: read, write, delete, admin
Use Enum with Flags for combining permissions
""")

from enum import Flag, auto


class Permission(Flag):
    """User permissions (can be combined)"""
    READ = auto()  # 1
    WRITE = auto()  # 2
    DELETE = auto()  # 4
    ADMIN = auto()  # 8


class Account:
    """Account with permissions"""

    def __init__(self, username):
        self.username = username
        self.permissions = Permission.READ  # Start with read-only

    def grant_permission(self, permission):
        """Add permission"""
        self.permissions |= permission

    def revoke_permission(self, permission):
        """Remove permission"""
        self.permissions &= ~permission

    def has_permission(self, permission):
        """Check if has permission"""
        return permission in self.permissions

    def get_permissions(self):
        """Get all permissions"""
        return [p.name for p in Permission if p in self.permissions]

    def __repr__(self):
        perms = self.get_permissions()
        return f"Account({self.username}, permissions={perms})"


# USAGE
print("\nDemo:")
print("-" * 80)

account = Account("alice")
print(f"Initial: {account}")

account.grant_permission(Permission.WRITE)
print(f"After granting WRITE: {account}")

account.grant_permission(Permission.DELETE)
print(f"After granting DELETE: {account}")

print(f"\nHas READ permission: {account.has_permission(Permission.READ)}")
print(f"Has ADMIN permission: {account.has_permission(Permission.ADMIN)}")

account.grant_permission(Permission.ADMIN)
print(f"\nAfter granting ADMIN: {account}")

account.revoke_permission(Permission.WRITE)
print(f"After revoking WRITE: {account}")

# ============================================================================
# COMPARISON: WITH vs WITHOUT ENUM
# ============================================================================

print("\n\n" + "=" * 80)
print("COMPARISON: With vs Without Enum")
print("=" * 80)

print("""
WITHOUT ENUM (Bad Way):
──────────────────────
status = "active"
status = "Active"        # Different!
status = "ACTIVE"        # Different again!
status = "activ"         # Typo!

Problems:
✗ Inconsistent spelling
✗ Easy to make typos
✗ No validation
✗ Hard to refactor
✗ No IDE autocomplete


WITH ENUM (Good Way):
────────────────────
class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

status = Status.ACTIVE
status = Status.ACTIVE    # Same every time
status = Status.ACTIVE    # Type-safe

Benefits:
✓ Consistent values
✓ No typos possible
✓ Type-safe (IDE autocomplete)
✓ Easy to refactor
✓ Self-documenting
✓ Easy to iterate
✓ Works with isinstance()
""")

# ============================================================================
# WHEN TO USE ENUMS
# ============================================================================

print("\n" + "=" * 80)
print("WHEN TO USE ENUMS")
print("=" * 80)

print("""
Use Enums when:

1. Fixed set of options
   Example: Colors, statuses, roles

2. Options should not change
   Example: Days of week, months

3. Want type safety
   Example: Payment methods should be validated

4. Prevent invalid values
   Example: Status should be one of predefined values

5. Need to iterate over values
   Example: Loop through all user roles

6. Want self-documenting code
   Example: UserRole.ADMIN is clearer than 3

7. Combine multiple flags
   Example: File permissions (read, write, execute)


Real-world examples:
✓ User statuses (active, inactive, suspended)
✓ Order statuses (pending, shipped, delivered)
✓ Payment methods (card, PayPal, crypto)
✓ User roles (admin, user, guest)
✓ HTTP status codes
✓ Log levels (debug, info, warning, error)
✓ File permissions (read, write, execute)
✓ Gender (male, female, other)
✓ Days of week
✓ Environment (dev, staging, production)
""")

# ============================================================================
# KEY ENUM FEATURES
# ============================================================================

print("\n" + "=" * 80)
print("KEY ENUM FEATURES")
print("=" * 80)

print("""
1. ACCESS MEMBERS:
   Color.RED          # Access member
   Color.RED.name     # Get name: "RED"
   Color.RED.value    # Get value: 1

2. ITERATE:
   for color in Color:
       print(color)

3. ITERATE BY VALUE:
   Color(1)           # Get member by value

4. COMPARE:
   Color.RED == Color.RED    # True
   Color.RED is Color.RED    # True (same object)

5. CHECK MEMBERSHIP:
   Color.RED in Color        # True

6. GET ALL MEMBERS:
   list(Color)        # List all members

7. CUSTOM METHODS:
   class Status(Enum):
       ACTIVE = 1

       def is_valid(self):
           return True

8. PROPERTIES:
   class Status(Enum):
       ACTIVE = (1, "Active")

       @property
       def code(self):
           return self.value[0]

9. FLAGS (Combine permissions):
   class Permission(Flag):
       READ = auto()
       WRITE = auto()

   perms = Permission.READ | Permission.WRITE

10. AUTO VALUES:
    from enum import auto

    class Color(Enum):
        RED = auto()    # 1
        GREEN = auto()  # 2
        BLUE = auto()   # 3
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)

print("""
1. ENUM: Set of named constants
   - Fixed set of options
   - Type-safe
   - Self-documenting

2. HOW TO CREATE:
   from enum import Enum

   class MyEnum(Enum):
       OPTION1 = value1
       OPTION2 = value2

3. BENEFITS:
   ✓ Prevent invalid values
   ✓ Type safety (IDE autocomplete)
   ✓ Self-documenting code
   ✓ Easy to iterate
   ✓ Easy to refactor
   ✓ Consistent values

4. COMMON TYPES:
   - Enum: Basic enums
   - IntEnum: Enums with integer values
   - Flag: Enums that can be combined (permissions)
   - IntFlag: Like Flag but with integers

5. USE WHEN:
   - Fixed set of options
   - Need type safety
   - Want to prevent invalid values
   - Self-documenting code
   - Need to iterate over options

6. REAL-WORLD:
   - User statuses
   - Order statuses
   - Payment methods
   - User roles
   - HTTP status codes
   - Log levels
   - File permissions
   - Environment variables
""")
