# ==========  7  ==========

text = input()
marks = '''\.,:;!?--'/"()*'''

for symbol in text:
    if symbol in marks:
        text = text.replace(symbol, '') 
    
print(text)

# ВЫВОД В ТЕРМИНАЛЕ:

# Точка. Запятая, Тире- и много других знаков препинания:;!?\'\" используются в русском (нашем) языке*/

# Точка Запятая Тире и много других знаков препинания используются в русском нашем языке


# Комментарий преподавателя:
# отличная работа! =)
