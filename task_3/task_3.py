import json


def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def populate_report(tests, values):
    id_to_value = {item['id']: item['value'] for item in values['values']}

    def populate_tests(tests):
        for test in tests:
            test_id = test['id']
            if test_id in id_to_value:
                test['value'] = id_to_value[test_id]
            if 'values' in test:
                populate_tests(test['values'])

    populate_tests(tests['tests'])
    return tests


def write_json_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def main(values_file, tests_file, report_file):
    values_data = load_json_file(values_file)
    tests_data = load_json_file(tests_file)

    report_data = populate_report(tests_data, values_data)

    write_json_file(report_data, report_file)
    print(f"Generated report.json based on {tests_file} and {values_file}.")


if __name__ == '__main__':
    values_file = 'values.json'
    tests_file = 'tests.json'
    report_file = 'report.json'

    main(values_file, tests_file, report_file)
