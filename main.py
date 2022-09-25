import datetime
today = datetime.date.today()
print(today)
print()

import emoji

from data import register
print(register)
print()

result = emoji.emojize('I :orange_heart: Python')
print(result)
print()


from people_package.people import get_employees
from salary_package.salary import get_salary

if __name__ == '__main__':
  get_employees()
  get_salary()
