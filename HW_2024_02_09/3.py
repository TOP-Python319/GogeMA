# === 3 ===

year = int(input('Введите год: '))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print('да')
else: 
    print('нет')

# ВЫВОД В ТЕРМИНАЛЕ:

# Пример 1:
# Введите год: 2024
# да

# Пример 2:
# Введите год: 2023
# нет

# комментарий преподавателя:
# всё чисто, вопросов нет. =)