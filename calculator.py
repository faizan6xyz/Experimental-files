def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    print("=" * 30)
    print("   SIMPLE CALCULATOR")
    print("=" * 30)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue
        
        if choice == '1':
            result = add(num1, num2)
            symbol = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            symbol = "*"
        elif choice == '4':
            result = divide(num1, num2)
            symbol = "/"
        
        print(f"\n{num1} {symbol} {num2} = {result}")

if __name__ == "__main__":
    calculator()
