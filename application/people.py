from application.database.data import list_of_employees


def get_employees(service_number, employees_list=list_of_employees):
    res_str = 'Такого табельного номера не существует'
    for dictionary in employees_list:
        for number in dictionary.values():
            if service_number == number:
                res_str = dictionary['name']
    print(res_str)
