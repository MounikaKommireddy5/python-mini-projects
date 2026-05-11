def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Calculator")
print("Add:", add(5, 3))
print("Sub:", sub(5, 3))
print("Mul:", mul(5, 3))
print("Div:", div(5, 3))
