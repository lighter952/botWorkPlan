from bot import bot_run
from table_parsing import *
from print import print_list_employess
from datetime import datetime

bot_run()

# timenow = datetime.now()
# print(timenow.day)
#
#
# file_name = "plan.xlsx"
#
# employees_list = get_list_of_employees(file_name)
# print_list_employess(employees_list)
#
# print("Choose your name: ", end="")
# inpt = int(input()) - 1
#
#
# employee_number: list = employees_list.get(list(employees_list.keys())[inpt])
# employee_plan = get_plan_by_employee_number(employee_number, file_name)
#

# for shift in employee_plan:
#     if shift.is_weekend:
#         print(str(shift.day_of_month) + ": Weekend!")
#         continue
#     print(str(shift.day_of_month) + ': ' + str(shift.start_time) + ' - ' + str(shift.end_time))


