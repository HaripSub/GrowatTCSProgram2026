# ASYNC/AWAIT IN PYTHON - Simple and Realistic Examples
# Async/Await: Run multiple tasks concurrently without blocking

import asyncio
import time
from datetime import datetime

# ============================================================================
# EXAMPLE 1: BASIC ASYNC/AWAIT (Simplest Example)
# ============================================================================

print("=" * 80)
print("EXAMPLE 1: Basic Async/Await (Simplest Example)")
print("=" * 80)

print("""
Scenario: Execute tasks that take time without blocking

Normal Code (BLOCKING):
    print("Start")
    time.sleep(2)     # Blocks for 2 seconds
    print("Done")
    print("This waits for sleep to finish!")

Async Code (NON-BLOCKING):
    print("Start")
    await asyncio.sleep(2)    # Doesn't block!
    print("Done")
    print("Can run other tasks while waiting")
""")


async def task_with_delay():
    """Simple async function"""
    print("  ⏱️  Task started")
    await asyncio.sleep(2)  # Wait 2 seconds (non-blocking)
    print("  ✓ Task completed")


async def run_basic_example():
    """Run basic async example"""
    print("\nDemo:")
    print("-" * 80)
    print("Running async task...")
    await task_with_delay()
    print("Done!\n")


# Run the example
asyncio.run(run_basic_example())

# ============================================================================
# EXAMPLE 2: MULTIPLE CONCURRENT TASKS
# ============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 2: Multiple Concurrent Tasks")
print("=" * 80)

print("""
Scenario: Download files from multiple servers at the same time

WITHOUT Async (Sequential - Slow):
    download_file("server1")  # Takes 2 seconds
    download_file("server2")  # Takes 2 seconds
    download_file("server3")  # Takes 2 seconds
    Total: 6 seconds

WITH Async (Concurrent - Fast):
    await asyncio.gather(
        download_file("server1"),
        download_file("server2"),
        download_file("server3")
    )
    Total: 2 seconds (all run at same time!)
""")


async def download_file(filename):
    """Simulate downloading a file"""
    print(f"  📥 Downloading {filename}...")
    await asyncio.sleep(2)  # Simulate download taking 2 seconds
    print(f"  ✓ {filename} downloaded")
    return f"Downloaded {filename}"


async def run_concurrent_example():
    """Run multiple tasks concurrently"""
    print("\nDemo:")
    print("-" * 80)
    start = time.time()

    # Run all 3 downloads at the same time
    results = await asyncio.gather(
        download_file("file1.txt"),
        download_file("file2.txt"),
        download_file("file3.txt")
    )

    elapsed = time.time() - start
    print(f"\nResults: {results}")
    print(f"Total time: {elapsed:.1f} seconds (would be 6 seconds if sequential)")


asyncio.run(run_concurrent_example())

# ============================================================================
# EXAMPLE 3: FETCHING DATA FROM MULTIPLE APIs
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 3: Fetching Data from Multiple APIs")
print("=" * 80)

print("""
Scenario: Get data from multiple API endpoints concurrently

Use Case:
    1. Fetch user data from API
    2. Fetch posts data from API
    3. Fetch comments data from API
    (All at the same time!)
""")


async def fetch_from_api(endpoint):
    """Simulate fetching data from API"""
    print(f"  🌐 Fetching from {endpoint}...")
    await asyncio.sleep(1.5)  # Simulate API call

    # Simulate API response
    data = {
        "users": {"id": 1, "name": "Alice"},
        "posts": {"id": 101, "title": "Python Tips"},
        "comments": {"id": 1001, "text": "Great post!"}
    }

    print(f"  ✓ Got data from {endpoint}")
    return data.get(endpoint, {})


async def run_api_example():
    """Fetch from multiple APIs concurrently"""
    print("\nDemo:")
    print("-" * 80)
    start = time.time()

    # Fetch from multiple endpoints at the same time
    user_data, post_data, comment_data = await asyncio.gather(
        fetch_from_api("users"),
        fetch_from_api("posts"),
        fetch_from_api("comments")
    )

    elapsed = time.time() - start
    print(f"\nUser: {user_data}")
    print(f"Post: {post_data}")
    print(f"Comment: {comment_data}")
    print(f"Total time: {elapsed:.1f} seconds")


asyncio.run(run_api_example())

# ============================================================================
# EXAMPLE 4: WEB SCRAPING (Realistic Use Case)
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 4: Web Scraping (Realistic Use Case)")
print("=" * 80)

print("""
Scenario: Scrape data from multiple websites concurrently

Use Case:
    Get prices from 5 different e-commerce sites
    Normally: 5 seconds (1 second each)
    Async: 1 second (all at same time!)
""")


async def scrape_website(website):
    """Simulate scraping a website"""
    print(f"  🕷️  Scraping {website}...")
    await asyncio.sleep(1)  # Simulate scraping

    # Simulate scraped data
    prices = {
        "amazon": 99.99,
        "ebay": 95.50,
        "walmart": 98.00,
        "target": 99.99,
        "bestbuy": 94.99
    }

    print(f"  ✓ Scraped {website}")
    return {"website": website, "price": prices.get(website, 0)}


async def run_scraping_example():
    """Scrape multiple websites concurrently"""
    print("\nDemo:")
    print("-" * 80)
    start = time.time()

    websites = ["amazon", "ebay", "walmart", "target", "bestbuy"]

    # Scrape all websites at the same time
    results = await asyncio.gather(
        *[scrape_website(site) for site in websites]
    )

    elapsed = time.time() - start

    print("\nPrice Comparison:")
    for result in results:
        print(f"  {result['website']}: ${result['price']}")

    print(f"\nTotal time: {elapsed:.1f} seconds")
    print(f"(Sequential would take {len(websites)} seconds)")


asyncio.run(run_scraping_example())

# ============================================================================
# EXAMPLE 5: ASYNC WITH ERROR HANDLING
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 5: Async with Error Handling")
print("=" * 80)

print("""
Scenario: Handle errors in async operations

Use Case:
    Some API calls might fail
    Continue with others
    Collect errors
""")


async def api_call_with_error(endpoint, should_fail=False):
    """Simulate API call that might fail"""
    print(f"  🌐 Calling {endpoint}...")
    await asyncio.sleep(1)

    if should_fail:
        print(f"  ✗ {endpoint} failed!")
        raise Exception(f"{endpoint} connection error")

    print(f"  ✓ {endpoint} succeeded")
    return f"Data from {endpoint}"


async def run_error_handling_example():
    """Handle errors in concurrent tasks"""
    print("\nDemo:")
    print("-" * 80)

    tasks = [
        api_call_with_error("api1"),
        api_call_with_error("api2", should_fail=True),  # This will fail
        api_call_with_error("api3"),
    ]

    # Method 1: gather with return_exceptions=True
    results = await asyncio.gather(*tasks, return_exceptions=True)

    print("\nResults:")
    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"  API{i}: ✗ Error - {result}")
        else:
            print(f"  API{i}: ✓ {result}")


asyncio.run(run_error_handling_example())

# ============================================================================
# EXAMPLE 6: DATABASE OPERATIONS (Realistic)
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 6: Database Operations (Realistic)")
print("=" * 80)

print("""
Scenario: Insert data into database concurrently

Use Case:
    Bulk insert 5 records
    Normally: 5 seconds (1 second each)
    Async: 1 second (all at same time!)
""")


async def insert_record(record_id, data):
    """Simulate inserting record into database"""
    print(f"  💾 Inserting record {record_id}...")
    await asyncio.sleep(1)  # Simulate database operation
    print(f"  ✓ Record {record_id} inserted")
    return f"Record {record_id} saved"


async def run_database_example():
    """Insert multiple records concurrently"""
    print("\nDemo:")
    print("-" * 80)
    start = time.time()

    records = [
        (1, {"name": "Alice", "email": "alice@example.com"}),
        (2, {"name": "Bob", "email": "bob@example.com"}),
        (3, {"name": "Charlie", "email": "charlie@example.com"}),
        (4, {"name": "Diana", "email": "diana@example.com"}),
        (5, {"name": "Eve", "email": "eve@example.com"}),
    ]

    # Insert all records concurrently
    results = await asyncio.gather(
        *[insert_record(rid, data) for rid, data in records]
    )

    elapsed = time.time() - start
    print(f"\nInserted {len(results)} records")
    print(f"Total time: {elapsed:.1f} seconds")
    print(f"(Sequential would take {len(records)} seconds)")


asyncio.run(run_database_example())

# ============================================================================
# EXAMPLE 7: REAL-WORLD - WEATHER API CALLS
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 7: Real-World - Weather API Calls")
print("=" * 80)

print("""
Scenario: Get weather for multiple cities concurrently

Use Case:
    Dashboard shows weather for 10 cities
    Normally: 10 seconds (1 second each)
    Async: 1 second (all at same time!)
""")


async def get_weather(city):
    """Simulate getting weather from API"""
    print(f"  🌤️  Fetching weather for {city}...")
    await asyncio.sleep(1)  # Simulate API call

    # Simulate weather data
    weather_data = {
        "New York": {"temp": 72, "condition": "Sunny"},
        "London": {"temp": 59, "condition": "Rainy"},
        "Tokyo": {"temp": 68, "condition": "Cloudy"},
        "Sydney": {"temp": 64, "condition": "Partly Cloudy"},
        "Paris": {"temp": 66, "condition": "Sunny"},
    }

    print(f"  ✓ Got weather for {city}")
    return {
        "city": city,
        "weather": weather_data.get(city, {"temp": 70, "condition": "Unknown"})
    }


async def run_weather_example():
    """Get weather for multiple cities concurrently"""
    print("\nDemo:")
    print("-" * 80)
    start = time.time()

    cities = ["New York", "London", "Tokyo", "Sydney", "Paris"]

    # Get weather for all cities at the same time
    results = await asyncio.gather(
        *[get_weather(city) for city in cities]
    )

    elapsed = time.time() - start

    print("\n🌍 Weather Report:")
    for result in results:
        city = result["city"]
        weather = result["weather"]
        print(f"  {city}: {weather['temp']}°F, {weather['condition']}")

    print(f"\nTotal time: {elapsed:.1f} seconds")


asyncio.run(run_weather_example())

# ============================================================================
# EXAMPLE 8: ASYNC CONTEXT MANAGER
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 8: Async Context Manager (with statement)")
print("=" * 80)

print("""
Scenario: Manage resources safely with async

Use Case:
    Open connection
    Use connection
    Close connection (guaranteed)
""")


class AsyncDatabaseConnection:
    """Async database connection with context manager"""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    async def __aenter__(self):
        """Enter context - open connection"""
        print(f"  🔗 Connecting to {self.db_name}...")
        await asyncio.sleep(0.5)
        self.connected = True
        print(f"  ✓ Connected")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit context - close connection"""
        print(f"  🔌 Disconnecting from {self.db_name}...")
        await asyncio.sleep(0.5)
        self.connected = False
        print(f"  ✓ Disconnected")
        return False

    async def query(self, sql):
        """Execute query"""
        if not self.connected:
            raise RuntimeError("Not connected")
        print(f"  📝 Executing: {sql}")
        await asyncio.sleep(0.5)
        return "Query results"


async def run_context_manager_example():
    """Use async context manager"""
    print("\nDemo:")
    print("-" * 80)

    # Context manager automatically handles connect/disconnect
    async with AsyncDatabaseConnection("mydb") as db:
        result = await db.query("SELECT * FROM users")
        print(f"  Result: {result}")

    print("\nConnection closed automatically!")


asyncio.run(run_context_manager_example())

# ============================================================================
# EXAMPLE 9: ASYNC GENERATOR
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 9: Async Generator")
print("=" * 80)

print("""
Scenario: Stream data asynchronously

Use Case:
    Process large file chunk by chunk
    Stream data from database
""")


async def fetch_data_stream(num_chunks):
    """Async generator - yields data one at a time"""
    for i in range(1, num_chunks + 1):
        print(f"  📦 Fetching chunk {i}...")
        await asyncio.sleep(0.5)
        yield f"Data chunk {i}"
        print(f"  ✓ Chunk {i} ready")


async def run_generator_example():
    """Use async generator"""
    print("\nDemo:")
    print("-" * 80)

    print("Processing data stream:")
    async for chunk in fetch_data_stream(3):
        print(f"  Processing: {chunk}")


asyncio.run(run_generator_example())

# ============================================================================
# COMPARISON: SYNC vs ASYNC
# ============================================================================

print("\n\n" + "=" * 80)
print("COMPARISON: Sync vs Async")
print("=" * 80)

print("""
SYNCHRONOUS (Blocking):
──────────────────────
def download(url):
    print("Downloading...")
    time.sleep(2)
    return "Downloaded"

# Usage
result1 = download("url1")  # Waits 2 seconds
result2 = download("url2")  # Waits 2 seconds
result3 = download("url3")  # Waits 2 seconds
# Total: 6 seconds ❌

Problems:
✗ Blocks while waiting
✗ One at a time
✗ Slow
✗ Can't do anything else


ASYNCHRONOUS (Non-blocking):
───────────────────────────
async def download(url):
    print("Downloading...")
    await asyncio.sleep(2)
    return "Downloaded"

# Usage
results = await asyncio.gather(
    download("url1"),
    download("url2"),
    download("url3")
)
# Total: 2 seconds ✅

Benefits:
✓ Doesn't block
✓ All at same time
✓ Fast
✓ Can handle many tasks
""")

# ============================================================================
# WHEN TO USE ASYNC/AWAIT
# ============================================================================

print("\n" + "=" * 80)
print("WHEN TO USE ASYNC/AWAIT")
print("=" * 80)

print("""
Use Async/Await when:

1. I/O Operations (Network, Database, Files)
   Example: API calls, web scraping, database queries

2. Want concurrent execution
   Example: Multiple downloads at same time

3. Don't want to block
   Example: Web server handling multiple requests

4. High performance needed
   Example: Process thousands of tasks

5. Event-driven programming
   Example: React to events as they happen


DO NOT use Async/Await for:
✗ CPU-intensive tasks (use multiprocessing instead)
✗ Simple operations (overhead not worth it)
✗ If not doing I/O or waiting


Real-world examples:
✓ Web scraping multiple sites
✓ API aggregation (combine multiple APIs)
✓ Web servers (FastAPI, aiohttp)
✓ Real-time applications (websockets)
✓ Bulk database operations
✓ Downloading multiple files
✓ Processing job queues
✓ Real-time chat applications
✓ Live data feeds
""")

# ============================================================================
# KEY ASYNC CONCEPTS
# ============================================================================

print("\n" + "=" * 80)
print("KEY ASYNC CONCEPTS")
print("=" * 80)

print("""
1. async def
   - Define async function
   - Can use await inside

2. await
   - Wait for async operation
   - Only works inside async function
   - Doesn't block other tasks

3. asyncio.gather()
   - Run multiple coroutines concurrently
   - Wait for all to complete
   - Return list of results

4. asyncio.create_task()
   - Create task from coroutine
   - Run in background

5. asyncio.sleep()
   - Async sleep (non-blocking)
   - Like time.sleep() but async

6. asyncio.run()
   - Run async function from synchronous code
   - Entry point for async program

7. async with
   - Context manager for async
   - __aenter__ and __aexit__

8. async for
   - Loop over async generator
   - Yields values asynchronously

9. Coroutine
   - Function created with async def
   - Returns awaitable object

10. Task
    - Wrapper around coroutine
    - Scheduled for execution
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)

print("""
1. ASYNC/AWAIT: Run multiple tasks concurrently
   - Doesn't block
   - Great for I/O operations
   - Much faster

2. HOW IT WORKS:
   1. Define async function with 'async def'
   2. Use 'await' to wait for operations
   3. Use 'asyncio.gather()' to run concurrently
   4. Run with 'asyncio.run()'

3. BENEFITS:
   ✓ Concurrent execution
   ✓ Non-blocking
   ✓ Fast (many tasks simultaneously)
   ✓ Responsive applications
   ✓ Better resource usage

4. COMMON PATTERNS:
   # Sequential (slow)
   await task1()
   await task2()
   await task3()

   # Concurrent (fast)
   await asyncio.gather(task1(), task2(), task3())

5. REMEMBER:
   ✓ Use for I/O operations
   ✓ Not for CPU-intensive tasks
   ✓ Always use 'await' with async functions
   ✓ Only use await inside async functions
   ✓ asyncio.gather() for multiple tasks

6. REAL-WORLD USES:
   - Web scraping
   - API calls
   - Database queries
   - File operations
   - Web servers
   - Real-time applications
""")
