from data import register

def get_employees():
  num_empl = input("Введите номер сотрудника: ")
  for output in register:
    if output["number"] == num_empl:
      print (f'Сотрудник: {output["name"]}')
    else:
      pass
get_employees()
