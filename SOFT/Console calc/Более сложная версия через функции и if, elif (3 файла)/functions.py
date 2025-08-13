# Сложение.
def add(a, b):
    return a + b

# Вычитание.
def subtract(a, b):
    return a - b

# Умножение.
def multiply(a, b):
    return a * b

# Возведение в степень.
def power(a, b):
    return a ** b

# Деление.
def divide(a, b):
    # Обработчик ошибок, что на ноль делить нельзя.
    if b != 0:
        return a / b
    else:
        return 'Ошибка! На ноль делить нельзя.'

# Целочисленное деление.
def integer_divide(a, b):
    # Аналогичный обработчик ошибок, что на ноль делить нельзя.
    if b != 0:
        return a // b
    else:
        return 'Ошибка! На ноль делить нельзя.'
