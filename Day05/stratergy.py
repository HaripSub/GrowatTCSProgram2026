# STRATEGY PATTERN - Simple and Realistic Examples
# Strategy: Different ways to do the same task, choose at runtime

# ============================================================================
# EXAMPLE 1: PAYMENT STRATEGIES (Most Realistic)
# ============================================================================

print("=" * 80)
print("EXAMPLE 1: Payment Strategies")
print("=" * 80)

print("""
Scenario: Different payment methods have different processing

Components:
- ShoppingCart: Uses payment strategy
- PaymentStrategy: Interface for all payment methods
- CreditCardPayment, PayPalPayment, CryptoCurrency: Different strategies
""")


# Base strategy (interface)
class PaymentStrategy:
    """Base payment strategy"""

    def pay(self, amount):
        raise NotImplementedError("Subclass must implement pay()")


# Different strategies
class CreditCardPayment(PaymentStrategy):
    """Strategy 1: Credit Card"""

    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        return f"💳 Paid ${amount} with Credit Card ending in {self.card_number[-4:]}"


class PayPalPayment(PaymentStrategy):
    """Strategy 2: PayPal"""

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"🅿️  Paid ${amount} via PayPal ({self.email})"


class CryptoPayment(PaymentStrategy):
    """Strategy 3: Cryptocurrency"""

    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"₿ Paid ${amount} with Crypto (Wallet: {self.wallet_address[:8]}...)"


class ApplePayPayment(PaymentStrategy):
    """Strategy 4: Apple Pay"""

    def __init__(self, device_id):
        self.device_id = device_id

    def pay(self, amount):
        return f"🍎 Paid ${amount} with Apple Pay"


# Context: Uses the strategy
class ShoppingCart:
    """Shopping cart that can use any payment strategy"""

    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def add_item(self, item, price):
        self.items.append((item, price))
        print(f"  ✓ Added {item} (${price})")

    def set_payment_strategy(self, strategy):
        """Choose payment method (strategy)"""
        self.payment_strategy = strategy
        print(f"  📌 Payment method set")

    def checkout(self):
        """Checkout using the chosen strategy"""
        total = sum(price for _, price in self.items)
        print(f"\n  Total: ${total}")

        if self.payment_strategy is None:
            print("  ✗ No payment method selected!")
            return

        print(self.payment_strategy.pay(total))
        self.items = []


# USAGE
print("\nDemo:")
print("-" * 80)

cart = ShoppingCart()
cart.add_item("Laptop", 999)
cart.add_item("Mouse", 25)

print("\nCustomer 1: Pays with Credit Card")
card_strategy = CreditCardPayment("4532-1111-2222-3333", "123")
cart.set_payment_strategy(card_strategy)
cart.checkout()

print("\n" + "-" * 80)
cart.add_item("Monitor", 350)
cart.add_item("Keyboard", 150)

print("\nCustomer 2: Pays with PayPal")
paypal_strategy = PayPalPayment("customer@example.com")
cart.set_payment_strategy(paypal_strategy)
cart.checkout()

print("\n" + "-" * 80)
cart.add_item("USB Cable", 10)

print("\nCustomer 3: Pays with Cryptocurrency")
crypto_strategy = CryptoPayment("1A1z7agoat2YLZW51Bc5M5sF5wExWFhDa")
cart.set_payment_strategy(crypto_strategy)
cart.checkout()

# ============================================================================
# EXAMPLE 2: SORTING STRATEGIES
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 2: Sorting Strategies")
print("=" * 80)

print("""
Scenario: Sort data using different algorithms

Components:
- DataProcessor: Uses sorting strategy
- SortStrategy: Interface for sorting
- BubbleSort, QuickSort, MergeSort: Different strategies
""")


class SortStrategy:
    """Base sorting strategy"""

    def sort(self, data):
        raise NotImplementedError("Subclass must implement sort()")


class BubbleSort(SortStrategy):
    """Strategy 1: Bubble Sort"""

    def sort(self, data):
        result = data.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result


class QuickSort(SortStrategy):
    """Strategy 2: Quick Sort"""

    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class MergeSort(SortStrategy):
    """Strategy 3: Merge Sort"""

    def sort(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


class DataProcessor:
    """Uses sorting strategy"""

    def __init__(self):
        self.strategy = None

    def set_sort_strategy(self, strategy):
        """Choose sorting algorithm"""
        self.strategy = strategy

    def process(self, data):
        """Sort data using chosen strategy"""
        if self.strategy is None:
            return "No strategy set!"
        return self.strategy.sort(data)


# USAGE
print("\nDemo:")
print("-" * 80)

processor = DataProcessor()
data = [64, 34, 25, 12, 22, 11, 90]

print(f"Original data: {data}")

print("\nSorting with Bubble Sort:")
processor.set_sort_strategy(BubbleSort())
result1 = processor.process(data)
print(f"Result: {result1}")

print("\nSorting with Quick Sort:")
processor.set_sort_strategy(QuickSort())
result2 = processor.process(data)
print(f"Result: {result2}")

print("\nSorting with Merge Sort:")
processor.set_sort_strategy(MergeSort())
result3 = processor.process(data)
print(f"Result: {result3}")

# ============================================================================
# EXAMPLE 3: SHIPPING STRATEGIES
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 3: Shipping Strategies")
print("=" * 80)

print("""
Scenario: Different shipping methods with different costs and times

Components:
- Order: Uses shipping strategy
- ShippingStrategy: Interface
- StandardShipping, ExpressShipping, OvernightShipping: Strategies
""")


class ShippingStrategy:
    """Base shipping strategy"""

    def calculate_cost(self, weight):
        raise NotImplementedError("Subclass must implement calculate_cost()")

    def get_delivery_time(self):
        raise NotImplementedError("Subclass must implement get_delivery_time()")


class StandardShipping(ShippingStrategy):
    """Strategy 1: Standard Shipping"""

    def calculate_cost(self, weight):
        return weight * 0.5  # $0.50 per kg

    def get_delivery_time(self):
        return "5-7 business days"


class ExpressShipping(ShippingStrategy):
    """Strategy 2: Express Shipping"""

    def calculate_cost(self, weight):
        return weight * 1.5  # $1.50 per kg

    def get_delivery_time(self):
        return "2-3 business days"


class OvernightShipping(ShippingStrategy):
    """Strategy 3: Overnight Shipping"""

    def calculate_cost(self, weight):
        return weight * 3.0  # $3.00 per kg

    def get_delivery_time(self):
        return "Next day"


class FreeShipping(ShippingStrategy):
    """Strategy 4: Free Shipping (for orders over $100)"""

    def calculate_cost(self, weight):
        return 0

    def get_delivery_time(self):
        return "7-10 business days"


class Order:
    """Uses shipping strategy"""

    def __init__(self, items_price):
        self.items_price = items_price
        self.weight = 0
        self.shipping_strategy = None

    def set_shipping_strategy(self, strategy):
        """Choose shipping method"""
        self.shipping_strategy = strategy

    def add_item(self, weight):
        self.weight += weight

    def calculate_total(self):
        """Calculate total with shipping"""
        if self.shipping_strategy is None:
            return "No shipping method selected!"

        shipping_cost = self.shipping_strategy.calculate_cost(self.weight)
        total = self.items_price + shipping_cost
        delivery_time = self.shipping_strategy.get_delivery_time()

        return f"Items: ${self.items_price} | Shipping: ${shipping_cost:.2f} | Total: ${total:.2f} | Delivery: {delivery_time}"


# USAGE
print("\nDemo:")
print("-" * 80)

order = Order(75)
order.add_item(2)  # 2 kg

print("\nCustomer chooses Standard Shipping:")
order.set_shipping_strategy(StandardShipping())
print(order.calculate_total())

print("\nCustomer changes to Express Shipping:")
order.set_shipping_strategy(ExpressShipping())
print(order.calculate_total())

print("\nCustomer changes to Overnight Shipping:")
order.set_shipping_strategy(OvernightShipping())
print(order.calculate_total())

order2 = Order(150)
order2.add_item(3)

print("\n\nHigh value order qualifies for Free Shipping:")
order2.set_shipping_strategy(FreeShipping())
print(order2.calculate_total())

# ============================================================================
# EXAMPLE 4: COMPRESSION STRATEGIES
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 4: File Compression Strategies")
print("=" * 80)

print("""
Scenario: Different file compression algorithms

Components:
- FileArchive: Uses compression strategy
- CompressionStrategy: Interface
- ZipCompression, RarCompression, GzipCompression: Strategies
""")


class CompressionStrategy:
    """Base compression strategy"""

    def compress(self, file_name):
        raise NotImplementedError("Subclass must implement compress()")


class ZipCompression(CompressionStrategy):
    """Strategy 1: ZIP"""

    def compress(self, file_name):
        return f"📦 Compressed {file_name} to {file_name}.zip (ZIP format)"


class RarCompression(CompressionStrategy):
    """Strategy 2: RAR"""

    def compress(self, file_name):
        return f"📦 Compressed {file_name} to {file_name}.rar (RAR format)"


class GzipCompression(CompressionStrategy):
    """Strategy 3: GZIP"""

    def compress(self, file_name):
        return f"📦 Compressed {file_name} to {file_name}.gz (GZIP format)"


class Tar7zCompression(CompressionStrategy):
    """Strategy 4: 7Z"""

    def compress(self, file_name):
        return f"📦 Compressed {file_name} to {file_name}.7z (7Z format)"


class FileArchive:
    """Uses compression strategy"""

    def __init__(self):
        self.strategy = None

    def set_compression_strategy(self, strategy):
        """Choose compression format"""
        self.strategy = strategy

    def archive(self, file_name):
        """Compress file using chosen strategy"""
        if self.strategy is None:
            return "No compression strategy set!"
        return self.strategy.compress(file_name)


# USAGE
print("\nDemo:")
print("-" * 80)

archive = FileArchive()
file_name = "myproject.txt"

print("\nUsing ZIP compression:")
archive.set_compression_strategy(ZipCompression())
print(archive.archive(file_name))

print("\nUsing RAR compression:")
archive.set_compression_strategy(RarCompression())
print(archive.archive(file_name))

print("\nUsing GZIP compression:")
archive.set_compression_strategy(GzipCompression())
print(archive.archive(file_name))

print("\nUsing 7Z compression:")
archive.set_compression_strategy(Tar7zCompression())
print(archive.archive(file_name))

# ============================================================================
# EXAMPLE 5: AUTHENTICATION STRATEGIES
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 5: Authentication Strategies")
print("=" * 80)

print("""
Scenario: Different authentication methods

Components:
- LoginService: Uses authentication strategy
- AuthStrategy: Interface
- UsernamePasswordAuth, BiometricAuth, OAuthAuth: Strategies
""")


class AuthStrategy:
    """Base authentication strategy"""

    def authenticate(self, credentials):
        raise NotImplementedError("Subclass must implement authenticate()")


class UsernamePasswordAuth(AuthStrategy):
    """Strategy 1: Username & Password"""

    def authenticate(self, credentials):
        username, password = credentials
        # Simple validation
        if password == "secret123":
            return f"✓ {username} authenticated with username & password"
        return "✗ Invalid credentials"


class BiometricAuth(AuthStrategy):
    """Strategy 2: Fingerprint/Face Recognition"""

    def authenticate(self, credentials):
        fingerprint = credentials
        # Simple validation
        if fingerprint == "fingerprint_data":
            return f"✓ Authenticated with biometric scan"
        return "✗ Biometric mismatch"


class OAuthAuth(AuthStrategy):
    """Strategy 3: OAuth (Google, GitHub, etc)"""

    def authenticate(self, credentials):
        token = credentials
        # Simple validation
        if token.startswith("oauth_"):
            return f"✓ Authenticated with OAuth token"
        return "✗ Invalid OAuth token"


class TwoFactorAuth(AuthStrategy):
    """Strategy 4: Two-Factor Authentication"""

    def authenticate(self, credentials):
        password, otp = credentials
        # Simple validation
        if password == "pass123" and len(otp) == 6:
            return f"✓ Authenticated with 2FA (password + OTP)"
        return "✗ 2FA verification failed"


class LoginService:
    """Uses authentication strategy"""

    def __init__(self):
        self.auth_strategy = None

    def set_auth_strategy(self, strategy):
        """Choose authentication method"""
        self.auth_strategy = strategy

    def login(self, credentials):
        """Login using chosen strategy"""
        if self.auth_strategy is None:
            return "No authentication strategy set!"
        return self.auth_strategy.authenticate(credentials)


# USAGE
print("\nDemo:")
print("-" * 80)

login = LoginService()

print("\nMethod 1: Username & Password")
login.set_auth_strategy(UsernamePasswordAuth())
print(login.login(("alice", "secret123")))

print("\nMethod 2: Biometric")
login.set_auth_strategy(BiometricAuth())
print(login.login("fingerprint_data"))

print("\nMethod 3: OAuth")
login.set_auth_strategy(OAuthAuth())
print(login.login("oauth_token_xyz123"))

print("\nMethod 4: Two-Factor Authentication")
login.set_auth_strategy(TwoFactorAuth())
print(login.login(("pass123", "123456")))

# ============================================================================
# COMPARISON: WITH vs WITHOUT STRATEGY
# ============================================================================

print("\n\n" + "=" * 80)
print("COMPARISON: With vs Without Strategy Pattern")
print("=" * 80)

print("""
WITHOUT STRATEGY (Bad Way - Hardcoded Logic):
──────────────────────────────────────────────
class ShoppingCart:
    def checkout(self, payment_type, amount):
        if payment_type == "credit_card":
            # Process credit card
            print(f"Charge ${amount} to credit card")
        elif payment_type == "paypal":
            # Process PayPal
            print(f"Charge ${amount} via PayPal")
        elif payment_type == "crypto":
            # Process crypto
            print(f"Charge ${amount} with crypto")

Problems:
✗ Logic scattered in one method
✗ Adding new payment method = modify cart class
✗ Hard to test each payment method
✗ Violates Single Responsibility Principle
✗ Cart knows about all payment details


WITH STRATEGY (Good Way - Encapsulated):
─────────────────────────────────────────
class PaymentStrategy:
    def pay(self, amount):
        pass

class ShoppingCart:
    def checkout(self, strategy, amount):
        strategy.pay(amount)

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        # Credit card logic here

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        # PayPal logic here

Benefits:
✓ Logic encapsulated in strategy classes
✓ Adding new payment = new strategy class
✓ Easy to test each strategy independently
✓ Follows Single Responsibility Principle
✓ Cart is simple and focused
✓ Open/Closed Principle (open for extension, closed for modification)
""")

# ============================================================================
# WHEN TO USE STRATEGY PATTERN
# ============================================================================

print("\n" + "=" * 80)
print("WHEN TO USE STRATEGY PATTERN")
print("=" * 80)

print("""
Use Strategy Pattern when:

1. Multiple ways to do the same task
   Example: Sort data (bubble sort, quick sort, merge sort)

2. Need to switch behavior at runtime
   Example: Change payment method before checkout

3. Avoid large if-elif-else chains
   Example: Instead of many conditions, use strategies

4. Each behavior should be independent
   Example: Each algorithm in separate class

5. Need to test different approaches
   Example: Test each sorting algorithm separately

6. Clients should choose algorithm
   Example: User picks shipping method


Real-world examples:
✓ Payment processing (card, PayPal, crypto)
✓ Sorting algorithms (bubble, quick, merge sort)
✓ Compression formats (ZIP, RAR, 7Z)
✓ Shipping methods (standard, express, overnight)
✓ Authentication (password, biometric, OAuth)
✓ Image filters (grayscale, sepia, blur)
✓ Discount strategies (percentage, fixed, buy-one-get-one)
✓ Route planning (fastest, shortest, least traffic)
✓ Notification delivery (email, SMS, push)
""")

# ============================================================================
# KEY COMPONENTS
# ============================================================================

print("\n" + "=" * 80)
print("KEY COMPONENTS OF STRATEGY PATTERN")
print("=" * 80)

print("""
1. CONTEXT
   - Uses strategy to perform task
   - Has reference to strategy
   - Example: ShoppingCart, DataProcessor, Order

2. STRATEGY (Interface)
   - Defines common interface
   - All concrete strategies implement this
   - Example: PaymentStrategy, SortStrategy

3. CONCRETE STRATEGIES
   - Different implementations
   - Each does the task differently
   - Example: CreditCardPayment, PayPalPayment

4. FLOW:
   Context → choose strategy → strategy.execute()

5. KEY METHOD:
   - set_strategy(): Choose algorithm
   - Then context uses chosen strategy
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)

print("""
1. Strategy Pattern: Encapsulate different behaviors
   - Each behavior in separate class
   - Choose at runtime

2. How it works:
   1. Create base strategy interface
   2. Create concrete strategy classes
   3. Context uses strategy
   4. Switch strategies as needed

3. Benefits:
   ✓ Avoid if-elif-else chains
   ✓ Easy to add new strategies
   ✓ Strategies are interchangeable
   ✓ Easy to test
   ✓ Single Responsibility Principle
   ✓ Open/Closed Principle

4. Key difference from Factory:
   - Factory: Creates objects
   - Strategy: Encapsulates algorithms

5. Similar to:
   - Decorator: Adds features
   - State: Changes behavior based on state
   - Strategy: Change behavior by selecting strategy

6. Common use cases:
   - Payment methods
   - Sorting algorithms
   - Compression formats
   - Shipping methods
   - Authentication methods
   - Discount strategies
""")
