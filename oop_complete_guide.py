"""
╔══════════════════════════════════════════════════════════════════════════════╗
║           OBJECT-ORIENTED PROGRAMMING IN PYTHON — COMPLETE GUIDE            ║
║                     All Topics with Explanations                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

TOPICS COVERED
──────────────
 1.  Classes & Objects                  — blueprint vs instance
 2.  __init__ & Instance Variables      — constructor, self
 3.  Class Variables & Class Methods    — shared state, @classmethod
 4.  Static Methods                     — @staticmethod, utility functions
 5.  Encapsulation                      — public, protected, private, getters/setters
 6.  Properties                         — @property, @setter, @deleter
 7.  Inheritance (Single)               — super(), method override
 8.  Multiple Inheritance               — MRO, diamond problem
 9.  Multilevel Inheritance             — chained parent → child → grandchild
10.  Polymorphism                       — same interface, different behaviour
11.  Method Overriding                  — child redefines parent method
12.  Method Overloading (Pythonic)      — default args, *args dispatch
13.  Operator Overloading               — __add__, __eq__, __lt__, __str__, etc.
14.  Abstract Classes & Methods         — abc module, ABC, @abstractmethod
15.  Interfaces (via ABC)               — enforcing contracts
16.  Mixins                             — reusable behaviour blocks
17.  Dunder / Magic Methods             — __repr__, __len__, __iter__, __getitem__
18.  Dataclasses                        — @dataclass, field(), post_init
19.  Class Decorators                   — custom decorators on methods & classes
20.  Descriptors                        — __get__, __set__, __delete__
21.  Metaclasses                        — type, custom metaclass, __new__
22.  Composition vs Inheritance         — HAS-A vs IS-A design
23.  SOLID Principles                   — applied in Python examples
24.  Design Patterns                    — Singleton, Factory, Observer, Strategy
25.  __slots__                          — memory optimisation
"""

# ─────────────────────────────────────────────────────────────────────────────
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import total_ordering
from typing import Protocol
import math


separator = lambda title: print(f"\n{'═'*60}\n  {title}\n{'═'*60}")


# ═════════════════════════════════════════════════════════════════════════════
# 1. CLASSES & OBJECTS
# ═════════════════════════════════════════════════════════════════════════════
"""
A CLASS is a blueprint / template that defines attributes (data) and
methods (behaviour).  An OBJECT is a concrete instance created from
that blueprint.  Every object gets its own copy of instance attributes
but shares the class's methods.
"""

class Dog:
    # Class-level docstring
    """Represents a dog with a name and breed."""

    # (Instance variables are set in __init__ — see next section)
    def bark(self):
        return "Woof!"

# Creating objects (instances)
dog1 = Dog()
dog2 = Dog()

# Each object is independent — they are different objects in memory
print(dog1 is dog2)          # False
print(type(dog1))            # <class '__main__.Dog'>
print(isinstance(dog1, Dog)) # True


# ═════════════════════════════════════════════════════════════════════════════
# 2. __init__ & INSTANCE VARIABLES
# ═════════════════════════════════════════════════════════════════════════════
"""
__init__ is the CONSTRUCTOR — it runs automatically when an object is
created.  'self' refers to the current object being initialised.
Instance variables (self.x) are unique to each object.
"""

class Person:
    def __init__(self, name: str, age: int):
        self.name = name      # instance variable
        self.age  = age       # instance variable

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

p1 = Person("Alice", 30)
p2 = Person("Bob",   25)

print(p1.greet())   # Hi, I'm Alice ...
print(p2.greet())   # Hi, I'm Bob ...
print(p1)           # Person(name='Alice', age=30)

# Dynamically adding an attribute (possible but not recommended)
p1.email = "alice@example.com"
print(p1.email)


# ═════════════════════════════════════════════════════════════════════════════
# 3. CLASS VARIABLES & CLASS METHODS
# ═════════════════════════════════════════════════════════════════════════════
"""
CLASS VARIABLES are shared across ALL instances of the class.
Changing them on the class affects all instances (unless overridden
on the instance).  @classmethod receives the class (cls) not the
instance — useful as alternative constructors or factory methods.
"""

class BankAccount:
    bank_name   = "Python National Bank"   # class variable — shared
    total_accounts = 0                     # class-level counter

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner   = owner
        self.balance = balance
        BankAccount.total_accounts += 1    # update class variable

    # ── Alternative constructor (class method) ─────────
    @classmethod
    def from_dict(cls, data: dict):
        """Create an account from a dictionary."""
        return cls(data["owner"], data["balance"])

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    def deposit(self, amount: float):
        self.balance += amount

    def __repr__(self):
        return f"BankAccount({self.owner!r}, ${self.balance:.2f})"


acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount.from_dict({"owner": "Bob", "balance": 500})
print(BankAccount.total_accounts)    # 2
print(BankAccount.get_bank_name())   # Python National Bank
print(acc1, acc2)


# ═════════════════════════════════════════════════════════════════════════════
# 4. STATIC METHODS
# ═════════════════════════════════════════════════════════════════════════════
"""
@staticmethod belongs to the class's NAMESPACE but receives neither
'self' nor 'cls'.  Use them for utility/helper logic that is
conceptually related to the class but doesn't need class or instance state.
"""

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return c * 9/5 + 32

print(MathUtils.add(3, 4))                    # 7
print(MathUtils.is_prime(17))                 # True
print(MathUtils.celsius_to_fahrenheit(100))   # 212.0
# Can also be called on an instance, but calling on the class is cleaner


# ═════════════════════════════════════════════════════════════════════════════
# 5. ENCAPSULATION
# ═════════════════════════════════════════════════════════════════════════════
"""
Encapsulation bundles data + methods together and RESTRICTS direct
access to internal state, exposing only what is necessary.

Python convention:
  name      → public      (anyone can access)
  _name     → protected   (internal use; convention only, not enforced)
  __name    → private     (name-mangled to _ClassName__name; harder to access)
"""

class Employee:
    def __init__(self, name: str, salary: float):
        self.name     = name          # public
        self._dept    = "Engineering" # protected — internal but accessible
        self.__salary = salary        # private — name-mangled

    # Getter
    def get_salary(self) -> float:
        return self.__salary

    # Setter with validation
    def set_salary(self, amount: float):
        if amount < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = amount

    def __repr__(self):
        return f"Employee({self.name!r}, dept={self._dept!r})"

emp = Employee("Carol", 75_000)
print(emp.name)            # Carol  (public)
print(emp._dept)           # Engineering  (accessible but "hands off")
print(emp.get_salary())    # 75000  (via getter)
emp.set_salary(80_000)
# print(emp.__salary)      # AttributeError — name-mangled
print(emp._Employee__salary)  # 80000 — mangled name (escape hatch, not recommended)


# ═════════════════════════════════════════════════════════════════════════════
# 6. PROPERTIES
# ═════════════════════════════════════════════════════════════════════════════
"""
@property lets you define a method that is accessed like an attribute —
no parentheses needed.  Pair with @<name>.setter and @<name>.deleter
for full controlled attribute access with validation, without breaking
the API (callers still use obj.attr syntax).
"""

class Circle:
    def __init__(self, radius: float):
        self._radius = radius      # stored with underscore

    @property
    def radius(self) -> float:
        """Getter — accessed as circle.radius"""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Setter with validation — called as circle.radius = 5"""
        if value < 0:
            raise ValueError("Radius must be non-negative.")
        self._radius = value

    @radius.deleter
    def radius(self):
        """Deleter — called as del circle.radius"""
        print("Deleting radius …")
        del self._radius

    @property
    def area(self) -> float:
        """Computed (read-only) property — no setter needed."""
        return math.pi * self._radius ** 2

    @property
    def circumference(self) -> float:
        return 2 * math.pi * self._radius

c = Circle(5)
print(c.radius)          # 5   (getter)
c.radius = 7             # setter — validates input
print(c.area)            # 153.93… (computed)
print(c.circumference)   # 43.98…
# c.radius = -1          # → ValueError


# ═════════════════════════════════════════════════════════════════════════════
# 7. INHERITANCE (SINGLE)
# ═════════════════════════════════════════════════════════════════════════════
"""
Inheritance lets a CHILD class acquire attributes and methods of a
PARENT class (IS-A relationship).  The child can:
  • Use parent methods as-is.
  • Override parent methods with new behaviour.
  • Extend parent methods using super().
"""

class Animal:
    def __init__(self, name: str, sound: str):
        self.name  = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"

    def breathe(self) -> str:
        return f"{self.name} breathes air."

class Cat(Animal):
    def __init__(self, name: str, indoor: bool = True):
        super().__init__(name, "Meow")   # call parent __init__
        self.indoor = indoor             # extra attribute

    def speak(self) -> str:
        # Override + extend parent method
        base = super().speak()
        return base + " *purrs*"

    def scratch(self):
        return f"{self.name} scratches the furniture."

cat = Cat("Whiskers")
print(cat.speak())     # Whiskers says Meow! *purrs*
print(cat.breathe())   # inherited from Animal
print(cat.scratch())   # Cat-specific method
print(isinstance(cat, Animal))  # True — cat IS-A Animal
print(isinstance(cat, Cat))     # True


# ═════════════════════════════════════════════════════════════════════════════
# 8. MULTIPLE INHERITANCE & MRO
# ═════════════════════════════════════════════════════════════════════════════
"""
A class can inherit from MORE THAN ONE parent.  Python uses the
C3 Linearisation algorithm (MRO — Method Resolution Order) to decide
which parent's method is called first when names conflict.
Use ClassName.__mro__ or ClassName.mro() to inspect the order.
"""

class Flyable:
    def move(self):
        return "Flying through the air"

    def describe(self):
        return "I can fly"

class Swimmable:
    def move(self):
        return "Swimming through water"

    def describe(self):
        return "I can swim"

class Duck(Flyable, Swimmable):   # Flyable listed first → wins MRO
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.move())       # Flying … (Flyable wins — listed first)
print(duck.quack())
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)

# ── Diamond Problem ───────────────────────────────────────
class A:
    def hello(self):
        return "A.hello"

class B(A):
    def hello(self):
        return "B.hello → " + super().hello()

class C(A):
    def hello(self):
        return "C.hello → " + super().hello()

class D(B, C):   # inherits from both B and C (diamond)
    pass

d = D()
print(d.hello())   # B.hello → C.hello → A.hello  (MRO resolves cleanly)
print(D.mro())     # [D, B, C, A, object]


# ═════════════════════════════════════════════════════════════════════════════
# 9. MULTILEVEL INHERITANCE
# ═════════════════════════════════════════════════════════════════════════════
"""
Multilevel inheritance chains classes:  A → B → C.
Each level can extend the previous one.
"""

class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

    def start(self):
        return f"{self.brand} engine started."

class Car(Vehicle):
    def __init__(self, brand: str, model: str):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"Driving {self.brand} {self.model}."

class ElectricCar(Car):
    def __init__(self, brand: str, model: str, battery_kwh: float):
        super().__init__(brand, model)
        self.battery_kwh = battery_kwh

    def charge(self):
        return f"Charging {self.battery_kwh} kWh battery."

    def drive(self):
        return super().drive() + " (silent electric motor)"

tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.start())   # from Vehicle
print(tesla.drive())   # from ElectricCar (overridden)
print(tesla.charge())  # from ElectricCar


# ═════════════════════════════════════════════════════════════════════════════
# 10. POLYMORPHISM
# ═════════════════════════════════════════════════════════════════════════════
"""
Polymorphism means "many forms" — the same method name produces
different behaviour depending on the object type.
Python achieves this via duck typing: if it has the method, it works.
"""

class Shape:
    def area(self) -> float:
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Triangle(Shape):
    def __init__(self, base, height):
        self.base, self.height = base, height
    def area(self):
        return 0.5 * self.base * self.height

class CircleShape(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2

# Polymorphic function — works with ANY shape
def print_area(shape: Shape):
    print(f"{type(shape).__name__:15s} area = {shape.area():.2f}")

shapes = [Rectangle(4, 5), Triangle(6, 3), CircleShape(7)]
for s in shapes:
    print_area(s)   # same call, different result ← polymorphism


# ═════════════════════════════════════════════════════════════════════════════
# 11. METHOD OVERRIDING
# ═════════════════════════════════════════════════════════════════════════════
"""
A child class can REDEFINE a method inherited from its parent.
The child version completely replaces the parent version unless
super() is explicitly called.
"""

class Logger:
    def log(self, message: str):
        print(f"[LOG] {message}")

class FileLogger(Logger):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def log(self, message: str):
        # Override — write to file instead of console
        with open(self.filepath, "a") as f:
            f.write(f"[FILE] {message}\n")
        print(f"Written to {self.filepath}: {message}")

class TimestampLogger(Logger):
    def log(self, message: str):
        import datetime
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        # Extend parent behaviour with timestamp
        super().log(f"[{ts}] {message}")

basic  = Logger()
ts_log = TimestampLogger()
basic.log("System started")
ts_log.log("User logged in")


# ═════════════════════════════════════════════════════════════════════════════
# 12. METHOD OVERLOADING (PYTHONIC)
# ═════════════════════════════════════════════════════════════════════════════
"""
Python does NOT support traditional overloading (multiple methods with
the same name but different signatures) — the last definition wins.
Instead, use:
  • Default arguments
  • *args / **kwargs
  • functools.singledispatch for type-based dispatch
"""

from functools import singledispatch

class Calculator:
    # ── Default arguments ──────────────────────────
    def power(self, base, exp=2):
        """Square by default; custom exponent optional."""
        return base ** exp

    # ── *args for variable arguments ───────────────
    def add(self, *args):
        return sum(args)

    # ── Type checking inside one method ───────────
    def multiply(self, a, b=None):
        if isinstance(a, list):
            result = 1
            for x in a: result *= x
            return result
        return a * (b or 1)

calc = Calculator()
print(calc.power(3))       # 9  (default exp=2)
print(calc.power(3, 3))    # 27
print(calc.add(1, 2, 3, 4))  # 10
print(calc.multiply([2, 3, 4]))  # 24
print(calc.multiply(5, 6))       # 30

# ── singledispatch for true type-based dispatch ────
@singledispatch
def process(data):
    raise TypeError(f"Unsupported type: {type(data)}")

@process.register(int)
def _(data):
    return f"Integer × 2 = {data * 2}"

@process.register(str)
def _(data):
    return f"String upper = {data.upper()}"

@process.register(list)
def _(data):
    return f"List length = {len(data)}"

print(process(5))           # Integer × 2 = 10
print(process("hello"))     # String upper = HELLO
print(process([1, 2, 3]))   # List length = 3


# ═════════════════════════════════════════════════════════════════════════════
# 13. OPERATOR OVERLOADING
# ═════════════════════════════════════════════════════════════════════════════
"""
Operator overloading lets objects respond to Python's built-in operators
(+, -, *, ==, <, len(), str(), etc.) by defining DUNDER METHODS.
"""

@total_ordering   # auto-generates __le__, __gt__, __ge__ from __eq__ & __lt__
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Arithmetic operators
    def __add__(self, other):          # self + other
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):          # self - other
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):         # self * scalar
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):        # scalar * self
        return self.__mul__(scalar)

    def __neg__(self):                 # -self
        return Vector(-self.x, -self.y)

    def __abs__(self):                 # abs(self) → magnitude
        return math.sqrt(self.x**2 + self.y**2)

    # Comparison operators
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):           # compare by magnitude
        return abs(self) < abs(other)

    # String representations
    def __str__(self):                 # user-friendly: str(v), print(v)
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):                # developer: repr(v), in containers
        return f"Vector(x={self.x}, y={self.y})"

    # Boolean
    def __bool__(self):               # bool(v) — False if zero vector
        return self.x != 0 or self.y != 0

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)      # Vector(4, 6)
print(v2 - v1)      # Vector(2, 2)
print(v1 * 3)       # Vector(3, 6)
print(2 * v1)       # Vector(2, 4)
print(abs(v2))      # 5.0
print(v1 == v2)     # False
print(v1 < v2)      # True (smaller magnitude)
print(-v1)          # Vector(-1, -2)


# ═════════════════════════════════════════════════════════════════════════════
# 14. ABSTRACT CLASSES & METHODS
# ═════════════════════════════════════════════════════════════════════════════
"""
An ABSTRACT CLASS (via abc.ABC) cannot be instantiated directly.
It defines a CONTRACT — abstract methods MUST be implemented by
every concrete subclass, otherwise instantiation raises TypeError.
Use when you want to enforce a common interface across a family of classes.
"""

class PaymentProcessor(ABC):
    """Abstract base — all payment processors must implement these."""

    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process a payment. Must return True on success."""

    @abstractmethod
    def refund(self, amount: float) -> bool:
        """Issue a refund."""

    # Concrete method — shared across all subclasses
    def validate_amount(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError(f"Invalid amount: {amount}")
        return True

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        self.validate_amount(amount)
        print(f"[Stripe] Charging ${amount:.2f} …")
        return True

    def refund(self, amount: float) -> bool:
        print(f"[Stripe] Refunding ${amount:.2f} …")
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        self.validate_amount(amount)
        print(f"[PayPal] Charging ${amount:.2f} …")
        return True

    def refund(self, amount: float) -> bool:
        print(f"[PayPal] Refunding ${amount:.2f} …")
        return True

# PaymentProcessor()  → TypeError: can't instantiate abstract class
stripe = StripeProcessor()
stripe.process_payment(99.99)
stripe.refund(99.99)


# ═════════════════════════════════════════════════════════════════════════════
# 15. INTERFACES (via Protocol — structural subtyping)
# ═════════════════════════════════════════════════════════════════════════════
"""
Python's typing.Protocol defines a STRUCTURAL interface — any class
that has the required methods satisfies the protocol, WITHOUT needing
to explicitly inherit from it (duck typing + static type checking).
"""

class Drawable(Protocol):
    def draw(self) -> str: ...
    def resize(self, factor: float) -> None: ...

class Square:
    def __init__(self, side: float):
        self.side = side
    def draw(self) -> str:
        return f"□ Square(side={self.side})"
    def resize(self, factor: float):
        self.side *= factor

class Star:
    def __init__(self, points: int):
        self.points = points
    def draw(self) -> str:
        return f"★ Star(points={self.points})"
    def resize(self, factor: float):
        self.points = int(self.points * factor)

def render(drawable: Drawable):
    # Works with ANY object that has draw() + resize() — no inheritance needed
    print(drawable.draw())

render(Square(10))   # □ Square(side=10)
render(Star(5))      # ★ Star(points=5)


# ═════════════════════════════════════════════════════════════════════════════
# 16. MIXINS
# ═════════════════════════════════════════════════════════════════════════════
"""
A MIXIN is a class that provides a set of reusable methods to be
"mixed in" to other classes via multiple inheritance.  Mixins:
  • Are NOT meant to stand alone (never instantiated directly).
  • Add one focused capability (serialisation, logging, comparison …).
  • Keep classes small and composable (prefer mixins over deep inheritance).
"""

class SerializeMixin:
    """Adds JSON-like serialisation to any class."""
    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def to_json_str(self) -> str:
        import json
        return json.dumps(self.to_dict(), indent=2)

class LogMixin:
    """Adds logging capability to any class."""
    def log(self, message: str):
        print(f"[{type(self).__name__}] {message}")

class ValidateMixin:
    """Adds a basic validate hook."""
    def validate(self) -> bool:
        raise NotImplementedError("Subclass must implement validate()")

class Product(SerializeMixin, LogMixin):
    def __init__(self, name: str, price: float, stock: int):
        self.name  = name
        self.price = price
        self.stock = stock

    def sell(self, qty: int):
        self.stock -= qty
        self.log(f"Sold {qty} × {self.name}. Stock left: {self.stock}")

prod = Product("Laptop", 999.99, 10)
prod.sell(2)
print(prod.to_dict())
print(prod.to_json_str())


# ═════════════════════════════════════════════════════════════════════════════
# 17. DUNDER / MAGIC METHODS
# ═════════════════════════════════════════════════════════════════════════════
"""
Dunder (double-underscore) methods hook into Python's built-in behaviour.
Defining them makes your objects work naturally with Python's syntax.
"""

class Stack:
    """A LIFO stack demonstrating common dunder methods."""

    def __init__(self):
        self._data = []

    # ── Container protocol ─────────────────────────
    def __len__(self):           # len(stack)
        return len(self._data)

    def __contains__(self, item):  # item in stack
        return item in self._data

    def __getitem__(self, index):  # stack[0]
        return self._data[index]

    def __setitem__(self, index, value):  # stack[0] = x
        self._data[index] = value

    def __delitem__(self, index):  # del stack[0]
        del self._data[index]

    # ── Iteration protocol ─────────────────────────
    def __iter__(self):          # for item in stack
        return iter(self._data)

    def __reversed__(self):      # reversed(stack)
        return reversed(self._data)

    # ── String representations ─────────────────────
    def __str__(self):           # print(stack)
        return f"Stack({self._data})"

    def __repr__(self):          # repr(stack)
        return f"Stack(data={self._data!r})"

    # ── Boolean ────────────────────────────────────
    def __bool__(self):          # bool(stack) / if stack:
        return len(self._data) > 0

    # ── Context manager protocol ───────────────────
    def __enter__(self):         # with Stack() as s:
        print("Stack context opened")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Stack context closed — clearing stack")
        self._data.clear()
        return False             # don't suppress exceptions

    # ── Call protocol ──────────────────────────────
    def __call__(self, item):    # stack(item) → push
        self._data.append(item)
        return self

    # Stack operations
    def push(self, item): self._data.append(item)
    def pop(self): return self._data.pop()

s = Stack()
s.push(10); s.push(20); s.push(30)
print(s)              # Stack([10, 20, 30])
print(len(s))         # 3
print(20 in s)        # True
print(s[0])           # 10
for item in s: print(item, end=" ")   # 10 20 30
print()
s(99)                 # __call__ — pushes 99
print(s)              # Stack([10, 20, 30, 99])

with Stack() as ws:
    ws.push("a")
    print(ws)         # Stack(['a'])
# Stack cleared after with block


# ═════════════════════════════════════════════════════════════════════════════
# 18. DATACLASSES
# ═════════════════════════════════════════════════════════════════════════════
"""
@dataclass auto-generates __init__, __repr__, __eq__ (and optionally
__lt__, __hash__, __frozen__) from the class's annotated fields.
Eliminates boilerplate for data-holding classes.
"""

@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

@dataclass(order=True, frozen=True)   # frozen=True → immutable + hashable
class RGB:
    red:   int = 0
    green: int = 0
    blue:  int = 0

@dataclass
class Inventory:
    name:    str
    items:   list = field(default_factory=list)   # mutable default
    count:   int  = field(default=0, repr=False)  # exclude from repr
    _secret: str  = field(default="hidden", init=False, repr=False)

    def __post_init__(self):
        """Runs after __init__ — for derived or validated fields."""
        self.count = len(self.items)
        if not self.name:
            raise ValueError("Inventory name cannot be empty.")

p1 = Point(1.0, 2.0)
p2 = Point(4.0, 6.0)
print(p1)                      # Point(x=1.0, y=2.0)
print(p1.distance_to(p2))      # 5.0

colour = RGB(255, 165, 0)
print(colour)                  # RGB(red=255, green=165, blue=0)
print(colour > RGB(0, 0, 0))   # True (order=True)

inv = Inventory("Warehouse A", ["apple", "banana", "cherry"])
print(inv)
print(inv.count)   # 3 — set in __post_init__


# ═════════════════════════════════════════════════════════════════════════════
# 19. CLASS DECORATORS & METHOD DECORATORS
# ═════════════════════════════════════════════════════════════════════════════
"""
Decorators are functions that WRAP another function or class,
adding behaviour without modifying the original code.
"""

import time
import functools

# ── Method decorator: timer ────────────────────────────
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end   = time.perf_counter()
        print(f"  {func.__name__} took {(end-start)*1000:.3f} ms")
        return result
    return wrapper

# ── Method decorator: validate types ──────────────────
def validate_positive(*param_indices):
    """Ensure specified positional arguments are positive."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for idx in param_indices:
                if idx < len(args) and args[idx] <= 0:
                    raise ValueError(
                        f"Argument at position {idx} must be positive, got {args[idx]}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

# ── Class decorator: add string representation ────────
def add_repr(cls):
    """Automatically add a clean __repr__ to any class."""
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Config:
    def __init__(self, host, port, debug=False):
        self.host  = host
        self.port  = port
        self.debug = debug

class DataProcessor:
    @timer
    def process(self, data: list) -> list:
        time.sleep(0.01)   # simulate work
        return [x * 2 for x in data]

    @validate_positive(1)    # 1 → first arg after self
    def set_batch_size(self, size: int):
        self.batch_size = size
        print(f"Batch size set to {size}")

cfg = Config("localhost", 8080, debug=True)
print(cfg)     # Config(host='localhost', port=8080, debug=True)

dp = DataProcessor()
result = dp.process([1, 2, 3, 4])
dp.set_batch_size(32)
# dp.set_batch_size(-1)   → ValueError


# ═════════════════════════════════════════════════════════════════════════════
# 20. DESCRIPTORS
# ═════════════════════════════════════════════════════════════════════════════
"""
A DESCRIPTOR is a class that defines __get__, __set__, or __delete__,
and is used as a class attribute of another class.
@property is actually a built-in descriptor.
Descriptors enable reusable attribute logic (type-checking, clamping …).
"""

class PositiveNumber:
    """Descriptor: ensures the attribute is always a positive number."""

    def __set_name__(self, owner, name):
        self.public_name  = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self          # accessed on class → return descriptor itself
        return getattr(obj, self.private_name, 0)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.public_name} must be a number.")
        if value <= 0:
            raise ValueError(f"{self.public_name} must be positive.")
        setattr(obj, self.private_name, value)

    def __delete__(self, obj):
        delattr(obj, self.private_name)

class Rectangle2:
    width  = PositiveNumber()   # descriptor instances as class attributes
    height = PositiveNumber()

    def __init__(self, width, height):
        self.width  = width     # triggers PositiveNumber.__set__
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle2(4, 5)
print(r.area)       # 20
r.width = 10        # descriptor validates
# r.width = -3      # → ValueError
# r.width = "abc"   # → TypeError


# ═════════════════════════════════════════════════════════════════════════════
# 21. METACLASSES
# ═════════════════════════════════════════════════════════════════════════════
"""
A METACLASS is the class of a class — it controls how classes themselves
are created.  'type' is Python's default metaclass.
Custom metaclasses let you:
  • Auto-register subclasses.
  • Enforce naming conventions.
  • Add methods/attributes to every class automatically.
"""

# ── Example 1: Enforce method naming convention ────────
class EnforceNamingMeta(type):
    def __new__(mcs, name, bases, namespace):
        for attr_name in namespace:
            if callable(namespace[attr_name]) and not attr_name.startswith("_"):
                if not attr_name.islower():
                    raise TypeError(
                        f"Method '{attr_name}' in class '{name}' "
                        f"must be snake_case (all lowercase)."
                    )
        return super().__new__(mcs, name, bases, namespace)

class MyService(metaclass=EnforceNamingMeta):
    def process_data(self): pass    # ✓ snake_case
    def get_result(self):  pass     # ✓ snake_case
    # def ProcessData(self): pass   # ✗ → TypeError

# ── Example 2: Auto-registry metaclass ────────────────
class PluginMeta(type):
    registry = {}

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if bases:   # don't register the base class itself
            PluginMeta.registry[name] = cls

class BasePlugin(metaclass=PluginMeta):
    pass

class CSVPlugin(BasePlugin):
    def run(self): return "Processing CSV"

class JSONPlugin(BasePlugin):
    def run(self): return "Processing JSON"

print("Registered plugins:", list(PluginMeta.registry.keys()))
# ['CSVPlugin', 'JSONPlugin']

# Dynamically create and run any plugin
for name, cls in PluginMeta.registry.items():
    print(f"  {name}: {cls().run()}")


# ═════════════════════════════════════════════════════════════════════════════
# 22. COMPOSITION vs INHERITANCE
# ═════════════════════════════════════════════════════════════════════════════
"""
INHERITANCE  → IS-A relationship  (a Dog IS-A Animal)
COMPOSITION  → HAS-A relationship (a Car HAS-A Engine)

Prefer COMPOSITION when:
  • The relationship isn't truly IS-A.
  • You want to swap components at runtime.
  • Inheritance would create a deeply coupled hierarchy.
"""

# ── Composition example ───────────────────────────────
class Engine:
    def __init__(self, horsepower: int):
        self.hp = horsepower

    def start(self):
        return f"Engine ({self.hp} HP) roaring!"

    def stop(self):
        return "Engine stopped."

class GPS:
    def navigate(self, destination: str):
        return f"Navigating to {destination} …"

class Automobile:
    """Automobile HAS-A Engine and HAS-A GPS (composition)."""

    def __init__(self, brand: str, engine: Engine, gps: GPS):
        self.brand  = brand
        self.engine = engine   # composed components
        self.gps    = gps

    def start_journey(self, destination: str):
        print(self.engine.start())
        print(self.gps.navigate(destination))

    def end_journey(self):
        print(self.engine.stop())

car = Automobile(
    "BMW",
    Engine(250),
    GPS(),
)
car.start_journey("Mumbai Airport")
car.end_journey()

# You can swap the engine without changing Automobile
car.engine = Engine(400)   # upgrade engine at runtime


# ═════════════════════════════════════════════════════════════════════════════
# 23. SOLID PRINCIPLES (applied in Python)
# ═════════════════════════════════════════════════════════════════════════════

# ── S: Single Responsibility Principle ────────────────
# Each class has ONE reason to change.
class InvoiceCalculator:
    def calculate_total(self, items):
        return sum(i["price"] * i["qty"] for i in items)

class InvoicePrinter:
    def print_invoice(self, total: float):
        print(f"Total due: ${total:.2f}")

class InvoiceSaver:
    def save(self, total: float, filepath: str):
        with open(filepath, "w") as f:
            f.write(str(total))

# ── O: Open/Closed Principle ──────────────────────────
# Open for extension, CLOSED for modification.
class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: ...

class NoDiscount(Discount):
    def apply(self, price): return price

class PercentDiscount(Discount):
    def __init__(self, pct): self.pct = pct
    def apply(self, price): return price * (1 - self.pct / 100)

class FlatDiscount(Discount):
    def __init__(self, amount): self.amount = amount
    def apply(self, price): return max(0, price - self.amount)

def final_price(price: float, discount: Discount) -> float:
    return discount.apply(price)     # ← no if/elif, add discounts without changing this

print(final_price(100, PercentDiscount(20)))   # 80.0
print(final_price(100, FlatDiscount(15)))      # 85.0

# ── L: Liskov Substitution Principle ─────────────────
# Subtypes must be substitutable for their base types.
class Bird(ABC):
    @abstractmethod
    def move(self) -> str: ...

class FlyingBird(Bird):
    def move(self): return "Flying"

class RunningBird(Bird):
    def move(self): return "Running"

class Eagle(FlyingBird): pass
class Penguin(RunningBird): pass     # Penguin doesn't fly — separate hierarchy

def make_bird_move(bird: Bird):
    print(bird.move())               # works for ALL Bird subclasses

make_bird_move(Eagle())    # Flying
make_bird_move(Penguin())  # Running

# ── I: Interface Segregation Principle ────────────────
# Clients should not be forced to implement interfaces they don't use.
class Printable(ABC):
    @abstractmethod
    def print_doc(self): ...

class Scannable(ABC):
    @abstractmethod
    def scan(self): ...

class Faxable(ABC):
    @abstractmethod
    def fax(self): ...

class SimplePrinter(Printable):     # only implements what it needs
    def print_doc(self): print("Printing …")

class AllInOne(Printable, Scannable, Faxable):
    def print_doc(self): print("Printing …")
    def scan(self):      print("Scanning …")
    def fax(self):       print("Faxing …")

# ── D: Dependency Inversion Principle ────────────────
# High-level modules should depend on ABSTRACTIONS, not concrete classes.
class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str): ...

class EmailSender(MessageSender):
    def send(self, message): print(f"Email: {message}")

class SMSSender(MessageSender):
    def send(self, message): print(f"SMS: {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):   # depends on abstraction
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

NotificationService(EmailSender()).notify("Hello via email!")
NotificationService(SMSSender()).notify("Hello via SMS!")


# ═════════════════════════════════════════════════════════════════════════════
# 24. DESIGN PATTERNS
# ═════════════════════════════════════════════════════════════════════════════

# ── Singleton ─────────────────────────────────────────
# Ensures only ONE instance of a class exists.
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: int = 0):
        if not hasattr(self, "_initialised"):
            self.value = value
            self._initialised = True

s1 = Singleton(10)
s2 = Singleton(99)
print(s1 is s2)       # True — same object
print(s1.value)       # 10 — init runs only once

# ── Factory Method ────────────────────────────────────
# Delegates object creation to subclasses / factory functions.
class Notification(ABC):
    @abstractmethod
    def notify(self, message: str): ...

class PushNotification(Notification):
    def notify(self, message):
        print(f"[PUSH] {message}")

class EmailNotification(Notification):
    def notify(self, message):
        print(f"[EMAIL] {message}")

class SlackNotification(Notification):
    def notify(self, message):
        print(f"[SLACK] {message}")

def notification_factory(channel: str) -> Notification:
    channels = {
        "push":  PushNotification,
        "email": EmailNotification,
        "slack": SlackNotification,
    }
    cls = channels.get(channel.lower())
    if cls is None:
        raise ValueError(f"Unknown channel: {channel}")
    return cls()

for ch in ["push", "email", "slack"]:
    notification_factory(ch).notify("System alert!")

# ── Observer ──────────────────────────────────────────
# Objects (observers) subscribe and react to events on a subject.
class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, list] = {}

    def on(self, event: str, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event: str, *args, **kwargs):
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)

emitter = EventEmitter()
emitter.on("sale",  lambda item, price: print(f"  Logger: {item} sold for ${price}"))
emitter.on("sale",  lambda item, price: print(f"  Inventory: deducting {item}"))
emitter.on("sale",  lambda item, price: print(f"  Email: receipt for ${price}"))
emitter.emit("sale", "Laptop", 999.99)

# ── Strategy ──────────────────────────────────────────
# Define a family of algorithms, encapsulate each, make them interchangeable.
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list: ...

class BubbleSort(SortStrategy):
    def sort(self, data):
        d = data[:]
        for i in range(len(d)):
            for j in range(len(d)-i-1):
                if d[j] > d[j+1]: d[j], d[j+1] = d[j+1], d[j]
        return d

class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1: return data
        pivot = data[len(data)//2]
        left  = [x for x in data if x < pivot]
        mid   = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + mid + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, data: list) -> list:
        return self.strategy.sort(data)

data = [5, 3, 8, 1, 9, 2]
print(Sorter(BubbleSort()).sort(data))   # [1, 2, 3, 5, 8, 9]
print(Sorter(QuickSort()).sort(data))    # [1, 2, 3, 5, 8, 9]


# ═════════════════════════════════════════════════════════════════════════════
# 25. __slots__ — MEMORY OPTIMISATION
# ═════════════════════════════════════════════════════════════════════════════
"""
By default every Python instance stores attributes in a __dict__
(a dictionary), which has memory overhead.  __slots__ replaces the
dict with a fixed set of attributes stored in a compact C array.

Benefits:
  • Lower memory usage (up to 50% less per object).
  • Faster attribute access.
  • Prevents accidental creation of new attributes.

Trade-offs:
  • Cannot add new attributes dynamically.
  • More complex with multiple inheritance.
"""

class PointSlotted:
    __slots__ = ("x", "y")   # only these two attributes are allowed

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

ps = PointSlotted(3.0, 4.0)
print(ps.distance())    # 5.0
# ps.z = 1              # → AttributeError: 'PointSlotted' has no attribute 'z'
# print(ps.__dict__)    # → AttributeError: no __dict__

# Memory comparison (rough)
import sys
class PointNormal:
    def __init__(self, x, y): self.x, self.y = x, y

pn = PointNormal(3.0, 4.0)
print(f"Normal  instance size: {sys.getsizeof(pn)} bytes + {sys.getsizeof(pn.__dict__)} bytes dict")
print(f"Slotted instance size: {sys.getsizeof(ps)} bytes (no dict)")


# ═════════════════════════════════════════════════════════════════════════════
# MAIN — RUN ALL DEMONSTRATIONS
# ═════════════════════════════════════════════════════════════════════════════
def main():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║       OOP IN PYTHON — COMPLETE GUIDE DEMONSTRATION          ║")
    print("╚══════════════════════════════════════════════════════════════╝")

    sections = [
        ("1.  Classes & Objects",            lambda: print(dog1.bark())),
        ("2.  __init__ & Instance Vars",     lambda: print(p1.greet())),
        ("3.  Class Variables & @classmethod",lambda: print(BankAccount.get_bank_name())),
        ("4.  Static Methods",               lambda: print(MathUtils.is_prime(17))),
        ("5.  Encapsulation",                lambda: print(emp.get_salary())),
        ("6.  Properties",                   lambda: print(f"Area={c.area:.2f}")),
        ("7.  Single Inheritance",           lambda: print(cat.speak())),
        ("8.  Multiple Inheritance & MRO",   lambda: print(duck.move())),
        ("9.  Multilevel Inheritance",       lambda: print(tesla.drive())),
        ("10. Polymorphism",                 lambda: [print_area(s) for s in shapes]),
        ("11. Method Overriding",            lambda: ts_log.log("Demo")),
        ("12. Method Overloading",           lambda: print(calc.add(1,2,3,4,5))),
        ("13. Operator Overloading",         lambda: print(v1 + v2)),
        ("14. Abstract Classes",             lambda: stripe.process_payment(50)),
        ("15. Protocol / Interface",         lambda: [render(x) for x in [Square(4), Star(6)]]),
        ("16. Mixins",                       lambda: prod.log("demo")),
        ("17. Dunder Methods",               lambda: print(len(s), 20 in s)),
        ("18. Dataclasses",                  lambda: print(p1, colour)),
        ("19. Class Decorators",             lambda: print(cfg)),
        ("20. Descriptors",                  lambda: print(r.area)),
        ("21. Metaclasses",                  lambda: print(list(PluginMeta.registry))),
        ("22. Composition",                  lambda: car.start_journey("Airport")),
        ("23. SOLID Principles",             lambda: print(final_price(100, PercentDiscount(10)))),
        ("24. Design Patterns",              lambda: notification_factory("push").notify("Hi")),
        ("25. __slots__",                    lambda: print(ps.distance())),
    ]

    for title, demo in sections:
        print(f"\n{'─'*60}")
        print(f"  {title}")
        print(f"{'─'*60}")
        try:
            demo()
        except Exception as e:
            print(f"  (demo skipped: {e})")


if __name__ == "__main__":
    main()
