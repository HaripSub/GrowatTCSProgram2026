# DETAILED EXPLANATION OF SINGLETON PATTERN
# Let's break down every line of code

# ============================================================================
# PART 1: What is __new__() method?
# ============================================================================

print("=" * 80)
print("PART 1: Understanding __new__() vs __init__()")
print("=" * 80)

print("""
When you create an object in Python, TWO methods are called:

1. __new__()   - Creates the object (returns it)
2. __init__()  - Initializes the object (sets up properties)

Example:
    obj = MyClass()

    Step 1: __new__() → Creates empty object
    Step 2: __init__() → Sets up object's data
""")


class NormalClass:
    """Shows when __new__ and __init__ are called"""

    def __new__(cls):
        print("  1. __new__() called - Creating object")
        obj = super().__new__(cls)
        print(f"     Object created with ID: {id(obj)}")
        return obj

    def __init__(self):
        print("  2. __init__() called - Setting up object")
        self.name = "Example"
        print(f"     Object initialized: {self.name}")


print("\nCreating a normal object:")
print("-" * 80)
obj = NormalClass()

# ============================================================================
# PART 2: How Singleton Works
# ============================================================================

print("\n\n" + "=" * 80)
print("PART 2: How Singleton Uses __new__()")
print("=" * 80)

print("""
Singleton Pattern:

1. Create class variable _instance = None
   → Stores the ONE object we create

2. Override __new__() method
   → Runs BEFORE __init__()
   → Check if object already exists
   → If yes: return existing
   → If no: create new and save

3. Always return _instance
   → Every call returns SAME object
""")

# ============================================================================
# PART 3: Detailed Code Walkthrough
# ============================================================================

print("\n\n" + "=" * 80)
print("PART 3: Detailed Code Walkthrough")
print("=" * 80)


class Database:
    # Store the ONE instance
    _instance = None

    def __new__(cls):
        # Check if object already exists
        if cls._instance is None:
            # First time - create new object
            print("    → First time: Creating new instance")
            cls._instance = super().__new__(cls)
        else:
            # Already exists - return saved one
            print("    → Already exists: Returning saved instance")

        # Always return the same object
        return cls._instance


print("\nLet's trace through each creation:\n")

print("1️⃣  First Database object:")
print("-" * 80)
db1 = Database()
print(f"   db1 = {db1}")
print(f"   ID: {id(db1)}")

print("\n2️⃣  Second Database object:")
print("-" * 80)
db2 = Database()
print(f"   db2 = {db2}")
print(f"   ID: {id(db2)}")
print(f"   Same as db1? {db1 is db2}")

print("\n3️⃣  Third Database object:")
print("-" * 80)
db3 = Database()
print(f"   db3 = {db3}")
print(f"   ID: {id(db3)}")
print(f"   Same as db1 and db2? {db1 is db2 is db3}")

# ============================================================================
# PART 4: The _instance Variable Magic
# ============================================================================

print("\n\n" + "=" * 80)
print("PART 4: The Magic _instance Variable")
print("=" * 80)


class MyDatabase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_name(self, name):
        self.name = name


print("\nStarting fresh - _instance is None:")
print(f"MyDatabase._instance = {MyDatabase._instance}\n")

print("Step 1: Create first object")
db_a = MyDatabase()
print(f"MyDatabase._instance now = {MyDatabase._instance}")
print(f"db_a = {db_a}")

print("\nStep 2: Create second object")
db_b = MyDatabase()
print(f"MyDatabase._instance still = {MyDatabase._instance}")
print(f"db_b = {db_b}")
print(f"Is db_a same as db_b? {db_a is db_b} ← YES! Same object")

print("\nStep 3: Change data through db_a")
db_a.set_name("FirstDB")
print(f"db_a.name = {db_a.name}")

print("\nStep 4: Check through db_b")
print(f"db_b.name = {db_b.name}")
print("^ SAME! Because they're the same object!")

# ============================================================================
# PART 5: Normal Class vs Singleton
# ============================================================================

print("\n\n" + "=" * 80)
print("PART 5: Normal Class vs Singleton Comparison")
print("=" * 80)


class NormalDB:
    """Without Singleton - creates new instance each time"""

    def __init__(self):
        self.id = id(self)
        print(f"      Created new object with ID: {self.id}")


class SingletonDB:
    """With Singleton - creates once, returns same"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.id = id(cls._instance)
            print(f"      Created object with ID: {cls._instance.id}")
        else:
            print(f"      Returning object with ID: {cls._instance.id}")
        return cls._instance


print("\nNORMAL CLASS (Without Singleton):")
print("-" * 80)
print("Creating 3 objects:")
normal1 = NormalDB()
normal2 = NormalDB()
normal3 = NormalDB()
print(f"\nIDs: {normal1.id}, {normal2.id}, {normal3.id}")
print("✗ All different - 3 separate objects created")

print("\n\nSINGLETON CLASS (With Singleton):")
print("-" * 80)
print("Creating 3 objects:")
single1 = SingletonDB()
single2 = SingletonDB()
single3 = SingletonDB()
print(f"\nIDs: {single1.id}, {single2.id}, {single3.id}")
print("✓ All same - only 1 object created")

# ============================================================================
# PART 6: Real World Example
# ============================================================================

print("\n\n" + "=" * 80)
print("PART 6: Real World Example - App Config")
print("=" * 80)


class AppConfig:
    """
    Singleton for app configuration

    Why singleton?
    - Load config ONCE, not multiple times
    - All parts use SAME config
    - Changes affect entire app
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("  → Loading config from file...")
            cls._instance = super().__new__(cls)
            cls._instance.database_url = "postgresql://localhost:5432"
            cls._instance.api_key = "sk_live_123456"
            cls._instance.debug_mode = True
        return cls._instance


print("\nApp starts - different parts need config:")
print("-" * 80)

print("\n1. Web server needs config:")
config_web = AppConfig()
print(f"   Database: {config_web.database_url}")

print("\n2. Task scheduler needs config:")
config_task = AppConfig()
print(f"   API Key: {config_task.api_key}")

print("\n3. Logger needs config:")
config_logger = AppConfig()
print(f"   Debug Mode: {config_logger.debug_mode}")

print("\n4. Admin changes debug mode:")
config_web.debug_mode = False
print(f"   Web server changes: {config_web.debug_mode}")

print("\n5. Task scheduler sees change?")
print(f"   Task scheduler sees: {config_task.debug_mode}")
print("   ✓ YES! Same object")

print(f"\n   All same config? {config_web is config_task is config_logger}")

# ============================================================================
# PART 7: Memory Diagram
# ============================================================================

print("\n\n" + "=" * 80)
print("PART 7: Memory Usage Comparison")
print("=" * 80)

print("""
WITHOUT SINGLETON:
─────────────────
normal1 ──→ [Object #1] ID: 140234892847360
normal2 ──→ [Object #2] ID: 140234892847424
normal3 ──→ [Object #3] ID: 140234892847488

Result: 3 objects in memory
Problem: Updates don't sync!


WITH SINGLETON:
───────────────
single1 ──┐
single2 ──┼──→ [Object] ID: 140234892847360
single3 ──┘    (Only ONE)

Result: 1 object in memory
Benefit: Updates visible everywhere!
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)

print("""
1. __new__() runs BEFORE __init__()
   → Controls object CREATION
   → Singleton overrides it

2. _instance class variable
   → Stores the ONE object
   → Persists between calls
   → Used to check if exists

3. if cls._instance is None:
   → None = doesn't exist → create it
   → Not None = exists → return it

4. return cls._instance
   → Always same object
   → Every call gets same instance

5. Real-world uses:
   ✓ Database connections
   ✓ Application config
   ✓ Logger
   ✓ Cache
   ✓ Sessions

6. Benefits:
   ✓ Save memory (one object)
   ✓ Consistent state (shared)
   ✓ Easy access (everywhere)
""")