# Обоснование выбора парадигмы:
# Декларативный стиль выбран для улучшения читаемости и поддерживаемости кода.
# Мы используем генераторы списков для создания таблицы умножения без явного управления состоянием вывода.
# Функции generate_multiplication_table и display_table разделяют логику генерации и отображения таблицы,
# делая код более структурированным.

def generate_multiplication_table(n):
    return [[f"{i} * {j} = {i * j}" for j in range(1, n + 1)] for i in range(1, n + 1)]

def display_table(table):
    for row in table:
        print("\t".join(row))

# Пример использования
n = int(input("Введите число n: "))
table = generate_multiplication_table(n)
display_table(table)
