from table_parsing import *

def print_list_employess(employees_list: list) -> None:
    i = 0
    for employee in employees_list:
        i += 1
        print(str(i) + ' - ' + employee)

def get_mounth_by_number(number: int) -> str:
    if 0 < number < 18:
        file_name = "plan.xlsx"
        employees_list = get_list_of_employees(file_name)
        employee_number: list = employees_list.get(list(employees_list.keys())[number])
        employee_plan = get_plan_by_employee_number(employee_number, file_name)
        repl = ''
        repl += f"{list(employees_list.keys())[number]}\n"
        for shift in employee_plan:
            if shift.is_weekend == False:
                repl += f"{shift.day_of_month}.04: Start: {shift.start_time}, end: {shift.end_time}\n"
            else:
                repl += f"{shift.day_of_month}.04: Is weekend\n"
        return repl
    else:
        return "Error: number not in range"
