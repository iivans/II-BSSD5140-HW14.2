class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '/': self.divide,
            'number_42': self.multiply,  
        }

    def menu(self):
        print("Available operations:")
        print(" + : Add")
        print(" - : Subtract")
        print(" / : Divide")
        print(" * : Multiply")
        print(" pow : Raise to a power")
        print(" q : Quit")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def multiply(self, a, b):
        return a * b

    def sqr(self, a, b):
        return a ** b  

    def perform_operation(self, op, a, b):
        if op == '*':
            method_name = 'number_42'  
            method = self.operations.get(method_name)
            if method:
                return method(a, b)
        method = self.operations.get(op)
        if method:
            return method(a, b)
        elif op == 'pow':  
            return self.sqr(a, b)
        else:
            return "Invalid operation"

def main():
    calc = Calculator()
    while True:
        calc.menu()
        op = input("Enter operation (or 'q' to quit): ").strip()
        if op == 'q':
            print("Exiting")
            break
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = calc.perform_operation(op, a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
