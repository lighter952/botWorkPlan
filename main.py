from table_parsing import get_list_of_employees
from table_parsing import get_plan_by_employee_number
file_name = "plan.xlsx"


employees_list = get_list_of_employees(file_name)

i = 0
for employee in employees_list:
    i += 1
    print(str(i) + ' - ' + employee)
inpt = int(input()) - 1
employee_number = employees_list.get(list(employees_list.keys())[inpt])
employee_plan = get_plan_by_employee_number(employee_number, file_name)

for shift in employee_plan:
    if shift.is_weekend:
        print(str(shift.day_of_month) + ": Weekend!")
        continue
    print(str(shift.day_of_month) + ': ' + str(shift.start_time) + ' - ' + str(shift.end_time))
