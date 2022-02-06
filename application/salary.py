from application.database.data import list_of_employees, time_worked, tariff_by_profession


def calculate_salary(service_number, employees_list=list_of_employees, time_list=time_worked,
                     tariff_list=tariff_by_profession):
    res_str = 'Такого табельного номера не существует'
    hours_worked = time_list.get(service_number)
    if hours_worked is None:
        print(res_str)
        return
    for dictionary in employees_list:
        for number in dictionary.values():
            if service_number == number:
                profession = dictionary['profession']
    rate = tariff_list.get(profession)
    salary = rate * hours_worked
    res_str = salary
    print(res_str)
