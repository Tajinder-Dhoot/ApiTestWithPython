import json


def compare_schema():
    with open('../files/employee.json') as file_1:
        data_1 = json.load(file_1)

    with open('../files/employee2.json') as file_2:
        data_2 = json.load(file_2)

    assert data_1 == data_2


compare_schema()

