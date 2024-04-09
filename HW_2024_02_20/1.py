# ==========  1  ==========

i = int(input())
numbers = []
while i % 7 == 0:
    numbers.insert(0, i)
    i = int(input())

print(*numbers, sep=' ')

# ВЫВОД В ТЕРМИНАЛЕ:

# 28
# 21
# 14
# 7
# 0
# 1

# 0 7 14 21 28


# Комментарий преподавателя:
# можно использовать while True и break вместо while i % 7 == 0 и else
