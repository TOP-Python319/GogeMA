# ==========  8  ==========

n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print('1 1')
elif n > 2:
    fib_1 = fib_2 = 1
    print (fib_1, fib_2, end=' ')
    for i in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(fib_2, end=' ')
        
# ВЫВОД В ТЕРМИНАЛЕ:

# 1
# 1

# 2
# 1 1

# 10
# 1 1 2 3 5 8 13 21 34 55 

# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 


# Комментарий преподавателя:
# Улучшение: использовать генератор для вывода последовательности Фибоначчи