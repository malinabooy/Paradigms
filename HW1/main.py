#Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
#сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
def bubble_sort_desc(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Пример использования
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_desc(numbers)
print("Отсортированный в порядке убывания список:", numbers)

#Написать точно такую же процедуру, но в декларативном стиле
def sort_desc(numbers):
    return sorted(numbers, reverse=True)

# Пример использования
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sort_desc(numbers)
print("Отсортированный в порядке убывания список:", sorted_numbers)
