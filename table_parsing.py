import pylightxl as xl
from models import Shift
from datetime import datetime


def get_list_of_employees(file_name) -> dict:
    """Возвращает лист работников из файла в виде словаря(имя, номер строки в таблице"""
    db = xl.readxl(file_name)
    employee_list = dict()
    i = 7
    while i < 65:
        i += 1
        table_cell = db.ws(ws='04.2023 ').index(row=i, col=3)
        if len(table_cell) > 10 and table_cell != 'godziny':
            employee_list[str(table_cell)] = [i, i + 62]
    return employee_list


def get_plan_by_employee_number(number: list, file_name: str) -> list:
    """ По заданному номеру работника возвращает лист обьектов его смен """

    db = xl.readxl(file_name)
    list_of_days = list()
    i = 3

    while i < 33:  # 33 is summary longitude of table
        i += 1
        cell = db.ws(ws='04.2023 ').index(row=number[0], col=i)

        if i % 2 == 0:
            day_of_month = int(db.ws(ws='04.2023 ').index(row=5, col=i))

        if len(str(cell)) > 1:
            is_weekend = False
            datetime_object = datetime.strptime(cell, '%H:%M:%S')
            if i % 2 == 0:
                shift_start_time = datetime_object.time()
            else:
                shift_end_time = datetime_object.time()
                list_of_days.append(Shift(day_of_month, shift_start_time, shift_end_time, is_weekend))
        else:
            if i % 2 == 0:
                shift_start_time = shift_end_time = datetime.strptime("00:00:00", '%H:%M:%S')
                is_weekend = True
                list_of_days.append(Shift(day_of_month, shift_start_time, shift_end_time, is_weekend))

    i = 3
    while i < 33:  # 33 is summary longitude of table
        i += 1
        cell = db.ws(ws='04.2023 ').index(row=number[1], col=i)

        if i % 2 == 0:
            day_of_month = int(db.ws(ws='04.2023 ').index(row=68, col=i))

        if len(str(cell)) > 1:
            is_weekend = False
            datetime_object = datetime.strptime(cell, '%H:%M:%S')
            if i % 2 == 0:
                shift_start_time = datetime_object.time()
            else:
                shift_end_time = datetime_object.time()
                list_of_days.append(Shift(day_of_month, shift_start_time, shift_end_time, is_weekend))
        else:
            if i % 2 == 0:
                shift_start_time = shift_end_time = datetime.strptime("00:00:00", '%H:%M:%S')
                is_weekend = True
                list_of_days.append(Shift(day_of_month, shift_start_time, shift_end_time, is_weekend))
    return list_of_days
