# задача 2_3_4

age_Anna = 35
age_moths = 35 * 12
print("age Anna in months: " + str(age_moths))

age_Anna_years = age_moths // 12
print("age Anna in years: " + str(age_Anna_years))

# варіант через приведення типів
age_Anna_years_2 = round(float(age_moths) / 12)
print("age Anna in years: " + str(age_Anna_years_2))

print("Му name is " + "Anna" + ". I'm " + str(age_Anna_years_2) + " years old")

# задача 2 (мій варіант)  вік людини в місяцях та роках на сьогоднішню дату

import datetime

birth_date = "1993-03-08"
current_date = datetime.date.today()

birth_date_num = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

age_in_month = (current_date.year - birth_date_num.year) * 12 + (birth_date_num.month - current_date.month)
print("age person in months: " + str(age_in_month))

age_in_years = current_date.year - birth_date_num.year
print("age person in years: " + str(age_in_years))

person = "Tom"
print("Му name is " + person+ ". I'm " + str(age_in_years) + " years old")
