from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(f'{calculate_salary(30,400)} {datetime.today().date()}')
    print(f"{get_employees('Ivan ', 'ivanov')} {datetime.today().date()}")