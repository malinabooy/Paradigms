import numpy as np

def pearson_correlation(x, y):
    # Проверяем, что массивы имеют одинаковую длину
    if len(x) != len(y):
        raise ValueError("Массивы должны иметь одинаковую длину")

    # Функция для вычисления среднего значения
    mean = lambda arr: sum(arr) / len(arr)

    # Вычисляем средние значения
    mean_x, mean_y = mean(x), mean(y)

    # Вычисляем корреляцию Пирсона
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    denominator_x = sum((x[i] - mean_x)**2 for i in range(len(x)))
    denominator_y = sum((y[i] - mean_y)**2 for i in range(len(y)))

    correlation = numerator / np.sqrt(denominator_x * denominator_y)

    return correlation

if __name__ == "__main__":
    # Пример использования
    array1 = [1, 2, 3, 4, 5]
    array2 = [2, 3, 4, 5, 6]

    correlation = pearson_correlation(array1, array2)
    print(f"Корреляция Пирсона между массивами: {correlation}")
