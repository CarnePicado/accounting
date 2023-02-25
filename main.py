from application.salary import calculate_salary
from application.db.people import get_employee
from datetime import datetime
import accounting

if __name__ == '__main__':
    print(datetime.now().date())
    print(calculate_salary())
    print(get_employee())