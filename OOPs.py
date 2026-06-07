from abc import ABC, abstractmethod
# 🔹 Base Class (Encapsulation + Abstraction)
class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name        # private variable (encapsulation)
        self._age = age           # protected variable 
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    @abstractmethod
    def sound(self):
        pass
# 🔹 Derived Class (Inheritance)
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    # 🔹 Polymorphism (method overriding)
    def sound(self):
        return "Bark"
    def display(self):
        print(f"Dog Name: {self.get_name()}, Age: {self._age}, Breed: {self.breed}")
# 🔹 Another Derived Class
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def sound(self):
        return "Meow"
    def display(self):
        print(f"Cat Name: {self.get_name()}, Age: {self._age}, Color: {self.color}")
# 🔹 Polymorphism in action
def animal_sound(animal):
    print(f"{animal.get_name()} says {animal.sound()}")
# 🔹 Main Program
if __name__ == "__main__":
    dog = Dog("Buddy", 3, "Labrador")
    cat = Cat("Kitty", 2, "White")
    dog.display()
    cat.display()
    animal_sound(dog)
    animal_sound(cat)