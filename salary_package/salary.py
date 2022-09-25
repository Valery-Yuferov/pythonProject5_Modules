from data import register

def get_salary():
  num_shifts = input("Введите кол-во смен сотрудника: ")
  num_rate = input("Введите ставку сотрудника: ")
  for output in register:
    if output["shifts"] == num_shifts and output["pay_rate"] == num_rate:
      print (f'Зарплата сотрудника: {int(num_shifts) * int(num_rate)}')
    else:
      pass
get_salary()
