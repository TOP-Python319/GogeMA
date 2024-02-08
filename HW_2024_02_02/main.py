# === 1 ===
print('ЗАДАЧА №1')

name = input('Введите ваше имя: ')
name = name + ","
surname = input('Введите вашу фамилию: ')
year_of_birth = int(input('Ведите год вашего рождения: '))
print(surname, name, 2024 - year_of_birth)
print()

# ВЫВОД В ТЕРМИНАЛЕ:
# PS C:\Users\Lenovo> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python312/python.exe c:/Users/Lenovo/Desktop/обучение/PYTHON/3.Python/les_3-4/main.py
# Введите ваше имя: Мария
# Введите вашу фамилию: Гоге
# Ведите год вашего рождения: 1986
# Гоге Мария, 38      
# PS C:\Users\Lenovo>


# === 2 ===
print('ЗАДАЧА №2')

number = int(input('Введите число: '))
print(f'Следующее за числом {number} число: {number + 1}')
print(f'Для числа {number} предыдущее число: {number - 1}')
print()

# ВЫВОД В ТЕРМИНАЛЕ:
# PS C:\Users\Lenovo> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python312/python.exe c:/Users/Lenovo/Desktop/обучение/PYTHON/3.Python/les_3-4/main.py
# Введите число: 999
# Следующее за числом 999 число: 1000
# Для числа 999 предыдущее число: 998
# PS C:\Users\Lenovo>


# === 3 ===
print('ЗАДАЧА №3')

time = int(input('Введите количество минут: '))
print(f'{time} мин - это {time // 60} час {time % 60} мин')
print()

# ВЫВОД В ТЕРМИНАЛЕ:
# PS C:\Users\Lenovo> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python312/python.exe c:/Users/Lenovo/Desktop/обучение/PYTHON/3.Python/les_3-4/main.py
# Введите количество минут: 500
# 500 мин - это 8 час 20 мин
# PS C:\Users\Lenovo>


# === 4 ===
print('ЗАДАЧА №4')

number = int(input('Введите положительное трехзначное число: '))
digit_1 = number // 100
digit_2 = number // 10 - digit_1 * 10
digit_3 = number % 10
print(f'Сумма цифр = {digit_1 + digit_2 + digit_3}')
print(f'Произведение цифр = {digit_1 * digit_2 * digit_3}')
print()

# ВЫВОД В ТЕРМИНАЛЕ:
# PS C:\Users\Lenovo> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python312/python.exe c:/Users/Lenovo/Desktop/обучение/PYTHON/3.Python/les_3-4/main.py
# Введите положительное трехзначное число: 555
# Сумма цифр = 15        
# Произведение цифр = 125
# PS C:\Users\Lenovo>  


# === 5 ===
print('ЗАДАЧА №5')

num1 = input('Введите целую часть числа миль: ')
num2 = input('Введите дробную часть числа миль: ')
miles = float(num1 + '.' + num2)
km = miles * 1.61
print(f'{miles} миль = {km:.1f} км')
print()

# ВЫВОД В ТЕРМИНАЛЕ:
# PS C:\Users\Lenovo> & C:/Users/Lenovo/AppData/Local/Programs/Python/Python312/python.exe c:/# Users/Lenovo/Desktop/обучение/PYTHON/3.Python/les_3-4/main.py
# Введите целую часть числа миль: 62
# Введите дробную часть числа миль: 05
# 62.05 миль = 99.9 км 
# PS C:\Users\Lenovo> 

#Комментарий от преподавателя: 12/12, но в следующий раз, пожалуйста, делите на отдельные файлы
