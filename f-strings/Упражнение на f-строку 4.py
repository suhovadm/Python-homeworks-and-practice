# python -m timeit -s 'x, y = "Hello", "World"' 'f"{x} {y}"'
from string import Template

x, y = "Hello", "World"

# Из всех методов форматирования строк, f-строки самые быстрые.
print(f"{x} {y}")  # 39.6 nsec per loop - Быстро!
print(x + " " + y)  # 43.5 nsec per loop
print(" ".join((x, y)))  # 58.1 nsec per loop
print("%s %s" % (x, y))  # 103 nsec per loop, через спецификаторы тоже довольно медленно.
print("{} {}".format(x, y))  # 141 nsec per loop
print(Template("$x $y").substitute(x=x, y=y))  # 1.24 usec per loop - медленно!