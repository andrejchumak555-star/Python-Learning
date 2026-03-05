a = float(input("Введи число! "))
b = float(input("Введи 2 число! "))
op = input("Введи операцию! ")

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "На ноль делить нельзя!"
    else:
        return "Неизвестная операция"

result = calculate(a, b, op)
print("Результат:", result)
