# ==========  3  ==========

num = int(input())
sum = num
for i in range(1, num // 2 + 1):
    if num % i == 0:
        sum += i
                
print(sum)

# ВЫВОД В ТЕРМИНАЛЕ:     

# 15
# 24