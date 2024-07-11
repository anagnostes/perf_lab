import sys  # Импорт модуля sys для работы с аргументами командной строки
import math  # Импорт модуля math для математических вычислений

# Функция для чтения данных о центре окружности и радиусе из файла
def read_circle_data(circle_file):
    with open(circle_file, 'r') as f:  # Открытие файла circle_file для чтения
        center = list(map(float, f.readline().strip().split()))  # Чтение координат центра и преобразование в числа с плавающей точкой
        radius = float(f.readline().strip())  # Чтение радиуса и преобразование в число с плавающей точкой
    return center, radius  # Возвращение кортежа с координатами центра и радиусом окружности

# Функция для чтения координат точек из файла
def read_points_data(points_file):
    points = []  # Пустой список для хранения координат точек
    with open(points_file, 'r') as f:  # Открытие файла points_file для чтения
        for line in f:  # Чтение файла построчно
            points.append(list(map(float, line.strip().split())))  # Преобразование строки в список чисел с плавающей точкой и добавление в список points
    return points  # Возвращение списка координат точек

# Функция для определения положения точки относительно окружности
def determine_point_position(center, radius, point):
    distance = math.sqrt((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2)  # Вычисление расстояния от точки до центра окружности
    if distance == radius:  # Если расстояние равно радиусу
        return 0  # Точка лежит на окружности
    elif distance < radius:  # Если расстояние меньше радиуса
        return 1  # Точка внутри окружности
    else:  # Если расстояние больше радиуса
        return 2  # Точка снаружи окружности

# Основная функция программы
def main():
    if len(sys.argv) != 3:  # Проверка, что количество аргументов командной строки равно 3 (имя скрипта + два файла)
        print("Usage: python script.py <circle_file> <points_file>")  # Вывод сообщения об использовании, если количество аргументов неверное
        return  # Завершение работы программы

    circle_file = sys.argv[1]  # Получение имени файла с данными окружности из аргумента командной строки
    points_file = sys.argv[2]  # Получение имени файла с данными точек из аргумента командной строки

    center, radius = read_circle_data(circle_file)  # Чтение данных об окружности из файла
    points = read_points_data(points_file)  # Чтение координат точек из файла

    for point in points:  # Для каждой точки из списка точек
        position = determine_point_position(center, radius, point)  # Определение её положения относительно окружности
        print(position)  # Вывод результата (0 - на окружности, 1 - внутри, 2 - снаружи)

if __name__ == "__main__":  # Если скрипт запущен напрямую, а не импортирован как модуль
    main()  # Вызов основной функции программы
