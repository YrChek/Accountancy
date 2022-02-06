from main import *

if __name__ == '__main__':
    service_number = input('Введите табельный номер' + "\n")
    print(date.today())
    get_employees(service_number)
    calculate_salary(service_number)
