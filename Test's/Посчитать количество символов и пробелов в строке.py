# Дана строка. Посчитать количество символов и пробелов.

text = str('20th Century Fox')

total_chars = len(text)
spaces = text.count(" ")

print('Количество символов:', total_chars)
print('Количество пробелов:', spaces)