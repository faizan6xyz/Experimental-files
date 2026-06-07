class Demo:
    class_var = "Shared by all objects"  
    # USE: Class variable (common for all objects)

    def __init__(self, name):
        self.name = name  
        # FUNCTION: Initializes object
        # USE: Assign values when object is created

    def __str__(self):
        return f"Name is {self.name}"
        # FUNCTION: Defines print() output
        # USE: User-friendly display

    def __repr__(self):
        return f"Demo({self.name})"
        # FUNCTION: Official representation
        # USE: Debugging

    def __len__(self):
        return len(self.name)
        # FUNCTION: Called by len()
        # USE: Returns length of object

    def __add__(self, other):
        return self.name + other.name
        # FUNCTION: Defines + operator
        # USE: Combine two objects

    def __eq__(self, other):
        return self.name == other.name
        # FUNCTION: Defines == operator
        # USE: Compare objects

    def __lt__(self, other):
        return self.name < other.name
        # FUNCTION: Defines < operator
        # USE: Sorting/comparison

    def __getitem__(self, index):
        return self.name[index]
        # FUNCTION: Enables indexing obj[0]
        # USE: Access data like list

    def __setattr__(self, key, value):
        print(f"Setting {key} = {value}")
        super().__setattr__(key, value)
        # FUNCTION: Controls attribute assignment
        # USE: Validation/logging

    def __call__(self):
        print(f"Hello {self.name}")
        # FUNCTION: Makes object callable
        # USE: obj() like function

    def __bool__(self):
        return len(self.name) > 0
        # FUNCTION: Defines truth value
        # USE: Used in if conditions

    def __iter__(self):
        return iter(self.name)
        # FUNCTION: Makes object iterable
        # USE: for loop support

    def __enter__(self):
        print("Start")
        return self
        # FUNCTION: Start of with block
        # USE: Resource handling

    def __exit__(self, a, b, c):
        print("End")
        # FUNCTION: End of with block
        # USE: Cleanup

    def show(self):
        """This is a demo method"""
        pass
        # FUNCTION: Example docstring
        # USE: Documentation


# ---------------- MAIN ----------------

if __name__ == "__main__":
    # FUNCTION: Checks if file is main program
    # USE: Prevents auto execution when imported

    obj1 = Demo("Ali")
    obj2 = Demo("Sara")

    print(obj1)                  # __str__
    print(repr(obj1))            # __repr__
    print(len(obj1))             # __len__
    print(obj1 + obj2)           # __add__
    print(obj1 == obj2)          # __eq__
    print(obj1 < obj2)           # __lt__
    print(obj1[1])               # __getitem__

    obj1()                       # __call__
    print(bool(obj1))            # __bool__

    for ch in obj1:              # __iter__
        print(ch)

    print(obj1.__dict__)         # FUNCTION: Object data
    print(obj1.__class__)        # FUNCTION: Class info
    print(obj1.show.__doc__)     # FUNCTION: Docstring
    print(obj1.__module__)       # FUNCTION: Module name

    import os
    print(os.path.abspath(__file__))  
    # FUNCTION: File path
    # USE: Locate script
    with Demo("Test") as d:      # __enter__, __exit__
        print("Inside block")