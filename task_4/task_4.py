import sys


# Функция для вычисления минимального количества ходов
def min_moves_to_same_number(nums):
    # Сортируем массив чисел
    nums.sort()
    # Находим медиану массива (серединный элемент после сортировки)
    median = nums[len(nums) // 2]
    # Инициализируем переменную для хранения суммы ходов
    moves = 0
    # Проходим по каждому числу в массиве
    for num in nums:
        # Добавляем значение разности между текущим числом и медианой к общему количеству ходов
        moves += abs(num - median)
    # Возвращаем общее количество ходов
    return moves


if __name__ == "__main__":
    # Проверяем, был ли передан аргумент командной строки
    if len(sys.argv) < 2:
        print("Usage: python program.py <input_file>")
        sys.exit(1)

    # Получаем имя файла из аргументов командной строки
    input_file = sys.argv[1]

    # Открываем файл и считываем числа в массив
    with open(input_file, 'r') as f:
        nums = [int(line.strip()) for line in f]

    # Вызываем функцию для нахождения минимального количества ходов
    result = min_moves_to_same_number(nums)

    # Выводим результат на экран
    print(result)
