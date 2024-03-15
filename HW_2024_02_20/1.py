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