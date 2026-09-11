# OBSERVER PATTERN - Simple and Realistic Examples
# Observer: Objects notify multiple listeners when something changes

# ============================================================================
# EXAMPLE 1: STOCK PRICE TRACKER (Most Realistic)
# ============================================================================

print("=" * 80)
print("EXAMPLE 1: Stock Price Tracker")
print("=" * 80)

print("""
Scenario: When stock price changes, notify all investors

Components:
- Subject (Stock): Tracks price, notifies observers
- Observers (Investors): Listen for price changes
- When price changes → All investors are notified
""")


class Stock:
    """Subject - Stock that investors watch"""

    def __init__(self, symbol, price):
        self.symbol = symbol
        self._price = price
        self.observers = []  # List of investors watching

    def attach(self, observer):
        """Investor starts watching this stock"""
        self.observers.append(observer)
        print(f"📌 {observer.name} is now watching {self.symbol}")

    def detach(self, observer):
        """Investor stops watching this stock"""
        self.observers.remove(observer)
        print(f"❌ {observer.name} stopped watching {self.symbol}")

    def notify(self):
        """Notify all investors when price changes"""
        for observer in self.observers:
            observer.update(self.symbol, self._price)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        """When price changes, notify all observers"""
        print(f"\n💹 {self.symbol} price changed: ${self._price} → ${value}")
        self._price = value
        self.notify()


class Investor:
    """Observer - Investor who watches stocks"""

    def __init__(self, name):
        self.name = name

    def update(self, symbol, price):
        """Called when stock price changes"""
        print(f"  📢 {self.name} received alert: {symbol} = ${price}")


# USAGE
print("\nDemo:")
print("-" * 80)

# Create stock
apple = Stock("AAPL", 150)

# Create investors
investor1 = Investor("Alice")
investor2 = Investor("Bob")
investor3 = Investor("Charlie")

# Investors start watching
apple.attach(investor1)
apple.attach(investor2)
apple.attach(investor3)

# Price changes → All investors notified
apple.price = 155

# New investor starts watching
investor4 = Investor("Diana")
apple.attach(investor4)

# Price changes again
apple.price = 152

# Investor stops watching
apple.detach(investor2)

# Price changes → Only 3 investors notified now
apple.price = 160

# ============================================================================
# EXAMPLE 2: EMAIL NEWSLETTER SUBSCRIPTION
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 2: Email Newsletter Subscription")
print("=" * 80)

print("""
Scenario: When new article is published, notify all subscribers

Components:
- BlogPost: Subject that publishes articles
- Subscribers: Observers that receive notifications
""")


class BlogPost:
    """Subject - Blog that publishes posts"""

    def __init__(self, title):
        self.title = title
        self.subscribers = []

    def subscribe(self, subscriber):
        """Someone subscribes to newsletter"""
        self.subscribers.append(subscriber)
        print(f"✓ {subscriber.email} subscribed")

    def unsubscribe(self, subscriber):
        """Someone unsubscribes"""
        self.subscribers.remove(subscriber)
        print(f"✗ {subscriber.email} unsubscribed")

    def publish(self, content):
        """Publish article → Notify all subscribers"""
        print(f"\n📝 New article: '{self.title}'")
        print(f"📤 Notifying {len(self.subscribers)} subscribers...")
        for subscriber in self.subscribers:
            subscriber.receive_notification(self.title, content)


class Subscriber:
    """Observer - Person subscribing to newsletter"""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def receive_notification(self, title, content):
        """Receive article notification"""
        print(f"  📧 {self.name} received: '{title}'")


# USAGE
print("\nDemo:")
print("-" * 80)

blog = BlogPost("Python Tips")

sub1 = Subscriber("Alice", "alice@email.com")
sub2 = Subscriber("Bob", "bob@email.com")
sub3 = Subscriber("Charlie", "charlie@email.com")

blog.subscribe(sub1)
blog.subscribe(sub2)
blog.subscribe(sub3)

blog.publish("10 Python tricks you should know")

blog.unsubscribe(sub2)

blog.publish("Advanced OOP concepts")

# ============================================================================
# EXAMPLE 3: WEATHER STATION
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 3: Weather Station")
print("=" * 80)

print("""
Scenario: Weather station updates, display and alarm notify

Components:
- WeatherStation: Subject that measures weather
- CurrentDisplay, Alarm: Observers that show data
""")


class WeatherStation:
    """Subject - Measures temperature"""

    def __init__(self):
        self._temperature = 70
        self.observers = []

    def attach(self, observer):
        """Add observer"""
        self.observers.append(observer)

    def detach(self, observer):
        """Remove observer"""
        self.observers.remove(observer)

    def notify(self):
        """Notify all observers"""
        for observer in self.observers:
            observer.update(self._temperature)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print(f"\n🌡️  Temperature changed to {value}°F")
        self._temperature = value
        self.notify()


class CurrentDisplay:
    """Observer - Shows current temperature"""

    def update(self, temp):
        print(f"  📺 Display: Current temp is {temp}°F")


class TemperatureAlarm:
    """Observer - Alerts if too hot or cold"""

    def update(self, temp):
        if temp > 85:
            print(f"  🔔 ALARM: Too hot! {temp}°F")
        elif temp < 32:
            print(f"  🔔 ALARM: Freezing! {temp}°F")
        else:
            print(f"  ✓ Alarm: Temperature OK ({temp}°F)")


class HistoryLogger:
    """Observer - Logs temperature history"""

    def __init__(self):
        self.history = []

    def update(self, temp):
        self.history.append(temp)
        print(f"  📊 Logger: Recorded (history: {self.history})")


# USAGE
print("\nDemo:")
print("-" * 80)

station = WeatherStation()

display = CurrentDisplay()
alarm = TemperatureAlarm()
logger = HistoryLogger()

station.attach(display)
station.attach(alarm)
station.attach(logger)

station.temperature = 75
station.temperature = 90
station.temperature = 20

# ============================================================================
# EXAMPLE 4: USER AUTHENTICATION SYSTEM
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 4: User Authentication System")
print("=" * 80)

print("""
Scenario: When user logs in, notify email service, analytics, security

Components:
- UserAuth: Subject that handles login
- EmailService, Analytics, SecurityLogger: Observers
""")


class UserAuth:
    """Subject - Handles user authentication"""

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        """Add observer"""
        self.observers.append(observer)

    def login(self, username):
        """User logs in → Notify all observers"""
        print(f"\n🔐 {username} logged in")
        for observer in self.observers:
            observer.on_user_login(username)

    def logout(self, username):
        """User logs out → Notify all observers"""
        print(f"\n🚪 {username} logged out")
        for observer in self.observers:
            observer.on_user_logout(username)


class EmailService:
    """Observer - Sends email on login"""

    def on_user_login(self, username):
        print(f"  📧 Email service: Sending welcome email to {username}")

    def on_user_logout(self, username):
        print(f"  📧 Email service: Sending goodbye email to {username}")


class AnalyticsService:
    """Observer - Tracks user activity"""

    def on_user_login(self, username):
        print(f"  📊 Analytics: Logged login event for {username}")

    def on_user_logout(self, username):
        print(f"  📊 Analytics: Logged logout event for {username}")


class SecurityLogger:
    """Observer - Logs for security"""

    def on_user_login(self, username):
        print(f"  🔒 Security: Recorded login at {username}")

    def on_user_logout(self, username):
        print(f"  🔒 Security: Recorded logout at {username}")


# USAGE
print("\nDemo:")
print("-" * 80)

auth = UserAuth()

email = EmailService()
analytics = AnalyticsService()
security = SecurityLogger()

auth.attach(email)
auth.attach(analytics)
auth.attach(security)

auth.login("alice@example.com")
auth.logout("alice@example.com")

# ============================================================================
# EXAMPLE 5: GAME EVENT SYSTEM
# ============================================================================

print("\n\n" + "=" * 80)
print("EXAMPLE 5: Game Event System")
print("=" * 80)

print("""
Scenario: When player scores, notify sound, UI, leaderboard

Components:
- Game: Subject that tracks score
- SoundManager, UIManager, Leaderboard: Observers
""")


class Game:
    """Subject - Game that tracks score"""

    def __init__(self):
        self._score = 0
        self.observers = []

    def attach(self, observer):
        """Add observer"""
        self.observers.append(observer)

    def score_points(self, points):
        """Player scores → Notify all observers"""
        self._score += points
        print(f"\n🎮 Player scored {points} points! Total: {self._score}")
        for observer in self.observers:
            observer.on_score_update(self._score)


class SoundManager:
    """Observer - Plays sound effect"""

    def on_score_update(self, score):
        print(f"  🔊 Sound: Playing 'ding' sound")


class UIManager:
    """Observer - Updates display"""

    def on_score_update(self, score):
        print(f"  🎨 UI: Updating score display to {score}")


class Leaderboard:
    """Observer - Updates leaderboard"""

    def on_score_update(self, score):
        print(f"  📋 Leaderboard: Updated with score {score}")


class AchievementSystem:
    """Observer - Checks for achievements"""

    def on_score_update(self, score):
        if score == 100:
            print(f"  🏆 Achievement: Reached 100 points!")
        elif score == 500:
            print(f"  🏆 Achievement: Reached 500 points!")


# USAGE
print("\nDemo:")
print("-" * 80)

game = Game()

sound = SoundManager()
ui = UIManager()
leaderboard = Leaderboard()
achievements = AchievementSystem()

game.attach(sound)
game.attach(ui)
game.attach(leaderboard)
game.attach(achievements)

game.score_points(50)
game.score_points(50)
game.score_points(100)

# ============================================================================
# COMPARISON: WITH vs WITHOUT OBSERVER
# ============================================================================

print("\n\n" + "=" * 80)
print("COMPARISON: With vs Without Observer Pattern")
print("=" * 80)

print("""
WITHOUT OBSERVER (Tightly Coupled):
──────────────────────────────────
class Stock:
    def set_price(self, price):
        self.price = price
        email_service.send_alert(price)
        sms_service.send_alert(price)
        analytics.log_price(price)

Problems:
✗ Stock class knows about all services
✗ Adding new service = modify Stock class
✗ Tight coupling - hard to change
✗ Stock has too many responsibilities


WITH OBSERVER (Loosely Coupled):
───────────────────────────────
class Stock:
    def set_price(self, price):
        self.price = price
        self.notify()  # Notify observers

class EmailService(Observer):
    def update(self, price):
        send_alert(price)

Benefits:
✓ Stock doesn't know about services
✓ Easy to add/remove observers
✓ Loose coupling - easy to change
✓ Single responsibility principle
✓ Stock only manages observers
""")

# ============================================================================
# KEY COMPONENTS
# ============================================================================

print("\n" + "=" * 80)
print("KEY COMPONENTS OF OBSERVER PATTERN")
print("=" * 80)

print("""
1. SUBJECT (Observable)
   - Maintains list of observers
   - Methods: attach(), detach(), notify()
   - Notifies when state changes
   - Example: Stock, WeatherStation, Game

2. OBSERVER (Listener)
   - Receives updates from subject
   - Method: update()
   - Reacts to changes
   - Example: Investor, Display, EmailService

3. CONCRETE SUBJECT
   - Specific subject
   - Example: AppleStock

4. CONCRETE OBSERVER
   - Specific observer
   - Example: EmailNotifier

5. FLOW:
   Subject changes → notify() called
   → All observers' update() called
   → Observers react to change
""")

# ============================================================================
# WHEN TO USE OBSERVER PATTERN
# ============================================================================

print("\n" + "=" * 80)
print("WHEN TO USE OBSERVER PATTERN")
print("=" * 80)

print("""
Use Observer Pattern when:

1. One-to-many relationship
   - One subject, many observers
   - Example: One blog, many subscribers

2. Change in one object affects others
   - Update propagates automatically
   - Example: Stock price → Investors notified

3. Don't want tight coupling
   - Objects don't need to know each other
   - Example: Game doesn't know UI exists

4. Need dynamic relationships
   - Add/remove observers at runtime
   - Example: Subscribe/unsubscribe anytime

5. Event-driven systems
   - React to events
   - Example: Button clicks, price changes


Real-world examples:
✓ Event listeners (JavaScript, GUI frameworks)
✓ MVC pattern (Model notifies Views)
✓ Message queues (Publisher-Subscriber)
✓ Real-time notifications
✓ Stock tickers
✓ Weather stations
✓ Social media feeds
✓ Game engines
✓ Reactive programming (RxJS, RxPython)
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)

print("""
1. Observer Pattern: Subject notifies observers of changes
   - Subject: maintains observers, notifies them
   - Observer: reacts to notifications

2. How it works:
   - Observer attaches to subject
   - Subject state changes
   - Subject calls update() on all observers
   - Observers react

3. Benefits:
   ✓ Loose coupling
   ✓ Dynamic relationships
   ✓ Easy to add/remove observers
   ✓ Single responsibility
   ✓ Open/closed principle

4. Key methods:
   - attach(): Subscribe observer
   - detach(): Unsubscribe observer
   - notify(): Tell observers about change
   - update(): Observer's reaction method

5. Real-world patterns:
   - Event listeners
   - Publish-subscribe
   - Model-View-Controller (MVC)
   - Reactive programming
""")
