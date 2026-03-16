def calculator():
    # Simple CLI calculator to perform +, -, *, /
    try:
        n1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        n2 = float(input("Enter second number: "))
        
        if op == '+': print(n1 + n2)
        elif op == '-': print(n1 - n2)
        elif op == '*': print(n1 * n2)
        elif op == '/':
            print(n1 / n2 if n2 != 0 else "Error: Division by zero")
        else: print("Invalid operator")
    except ValueError:
        print("Invalid number input")

if __name__ == "__main__":
    print("-------Calculator--------")
    calculator()
