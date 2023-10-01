from employees.models import Subsidiary, Department, Employee
import random

import random
from datetime import datetime, timedelta

# Генерация случайного дня, месяца и года для даты рождения
def generate_random_birthdate(start_date, end_date):
    days_difference = (end_date - start_date).days
    random_days = random.randint(0, days_difference)
    random_birthdate = start_date + timedelta(days=random_days)
    return random_birthdate

# Установите начальную и конечную даты для генерации
start_date = datetime(1950, 1, 1)
end_date = datetime(2005, 12, 31)

# Генерация случайной даты рождения


def run():
    # Вставляем данные в таблицы
    branch = [("Moscow", 'Филиал 1'), ("SPB",
                                       'Филиал 2'), ("Voronej", 'Филиал 3')]

    for branch in branch:
        subsidiary = Subsidiary(address=branch[0],
                                short_name=branch[1])
        subsidiary.save()

        num_departments = random.randint(2, 5)

        for i in range(num_departments):
            department_name = f'Отдел {random.randint(1, 30)}-{random.randint(1, 30)}'
            department = Department(
                name=department_name, 
                floor=i,
                subsidiary=subsidiary)
            num_employees = random.randint(1, 30)
            positions = ["Devops", "Developer", "Manager"]
            numbers = ["355.243.6022", "932-986-4653", "1-404-735-1588"]
            email = ["fugit@gmail.com", "ut@gmail.com", "debitis@gmail.com"]
            department.save()
            for _ in range(num_employees):
                employee_name = f'Сотрудник {random.randint(1, 30)}'
                employee = Employee(full_name=employee_name,
                                    position=random.choice(positions),
                                    phone_number=random.choice(numbers),
                                    birth_date= generate_random_birthdate(start_date, end_date),
                                    email=random.choice(email),
                                    department=department)
                employee.save()


