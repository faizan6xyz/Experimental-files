from abc import ABC, abstractmethod
# =========================
# ABSTRACTION
# =========================
class Person(ABC):
    def __init__(self, name, age):
        self.name = name          # Encapsulation (public)
        self._age = age           # Protected variable
    @abstractmethod
    def role(self):
        pass
    def show_details(self):
        print(f"Name: {self.name}, Age: {self._age}")
# =========================
# INHERITANCE + POLYMORPHISM
# =========================
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)   # Calling parent constructor
        self.marks = marks
    def role(self):   # Method overriding (polymorphism)
        print("I am a Student")
    def show_marks(self):
        print(f"Marks: {self.marks}")
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def role(self):   # Method overriding
        print("I am a Teacher")
    def show_subject(self):
        print(f"Subject: {self.subject}")
# =========================
# ENCAPSULATION (PRIVATE)
# =========================
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
# =========================
# METHOD TYPES
# =========================
class Demo:
    class_var = "I am class variable"
    def __init__(self):
        self.instance_var = "I am instance variable"
    def instance_method(self):
        print("Instance Method")
    @classmethod
    def class_method(cls):
        print("Class Method:", cls.class_var)
    @staticmethod
    def static_method():
        print("Static Method")
# =========================
# MAIN PROGRAM
# =========================
if __name__ == "__main__":
    print("=== Student ===")
    s = Student("Faizan", 20, 90)
    s.role()
    s.show_details()
    s.show_marks()
    print("\n=== Teacher ===")
    t = Teacher("Ali", 35, "Math")
    t.role()
    t.show_details()
    t.show_subject()
    print("\n=== Bank Account ===")
    acc = BankAccount(1000)
    acc.deposit(500)
    print("Balance:", acc.get_balance())
    print("\n=== Method Types ===")
    d = Demo()
    d.instance_method()
    Demo.class_method()
    Demo.static_method()