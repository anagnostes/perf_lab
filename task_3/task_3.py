import json


def load_json_file(file_path):
    # Открываем файл и загружаем JSON данные из указанного пути
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def populate_report(tests, values):
    # Создаем словарь для быстрого поиска значений по id
    id_to_value = {item['id']: item['value'] for item in values['values']}

    # Рекурсивная функция для заполнения поля "value" в tests.json
    def populate_tests(tests):
        for test in tests:
            test_id = test['id']
            # Если id тест найден в словаре, заполняем поле "value"
            if test_id in id_to_value:
                test['value'] = id_to_value[test_id]
            # Если есть вложенные тесты, вызываем функцию рекурсивно
            if 'values' in test:
                populate_tests(test['values'])

    # Запускаем рекурсивную функцию для корневого списка тестов
    populate_tests(tests['tests'])
    return tests


def write_json_file(data, file_path):
    # Открываем файл и записываем данные в формате JSON с отступами
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def main(values_file, tests_file, report_file):
    # Загружаем данные из values.json и tests.json
    values_data = load_json_file(values_file)
    tests_data = load_json_file(tests_file)

    # Заполняем данные отчета на основе values_data
    report_data = populate_report(tests_data, values_data)

    # Записываем результат в report.json
    write_json_file(report_data, report_file)
    print(f"Generated report.json based on {tests_file} and {values_file}.")


if __name__ == '__main__':
    # Пути к файлам JSON
    values_file = 'values.json'
    tests_file = 'tests.json'
    report_file = 'report.json'

    # Запуск основной функции
    main(values_file, tests_file, report_file)

