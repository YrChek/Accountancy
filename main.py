from application.people import get_employees
from application.salary import calculate_salary
from datetime import date


if __name__ == '__main__':
    service_number = input('Введите табельный номер' + "\n")
    print('Сегодня:', date.today())
    get_employees(service_number)
    calculate_salary(service_number)
