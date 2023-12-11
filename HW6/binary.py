def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Найден искомый элемент, возвращаем его индекс
        elif mid_value < target:
            low = mid + 1  # Искомый элемент находится справа от середины
        else:
            high = mid - 1  # Искомый элемент находится слева от середины

    return -1  # Элемент не найден

# Пример использования:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = binary_search(sorted_array, target_element)

if result != -1:
    print(f"Искомый элемент {target_element} найден по индексу {result}.")
else:
    print(f"Искомый элемент {target_element} не найден в массиве.")
