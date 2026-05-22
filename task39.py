def calculate(a, b, operation):
    if operation == "+":
        return a + b;
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return None
    
print(calculate(10,3, "/"))