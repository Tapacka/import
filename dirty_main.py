from application.salary import *
from application.db.people import *
print(f'{calculate_salary(30,400)} {datetime.today().date()}')
print(f"{get_employees('Ivan ', 'ivanov')} {datetime.today().date()}")