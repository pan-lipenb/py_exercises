from datetime import datetime, timedelta
# from dateutil import relativedelta
name = input("Имя: ")
surname = input("Фамилия: ")
date_of_birth = input("Дата рождения в формате дд.мм.гггг: ")
height = int(input("Введите свой рост в см: "))

dt = datetime.today()
db = datetime.strptime(date_of_birth, '%d.%m.%Y') 
days_in_year = timedelta(days=365.25)
name = name.title()
surname = surname.title()
age = int((dt - db)/days_in_year)
delta_H = height - 178 

print(f"Пользователь {name} {surname}, {age} лет. Ваш рост выше среднего на {delta_H} см.")