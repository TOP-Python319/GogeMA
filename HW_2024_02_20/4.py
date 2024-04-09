# ==========  4  ==========

def is_prime(x):
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
counter = 0

for i in range(10 ** (n - 1), 10 ** n):
    if is_prime(i):
        counter += 1
        
print(counter)

# ВЫВОД В ТЕРМИНАЛЕ:

# 2
# 21


# комментарий преподавателя:
# вопросов нет. =)