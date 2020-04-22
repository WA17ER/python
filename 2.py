time = int(input("Ведите время в секундах"))
sec = time % 60
min = time // 60
hour = time // 360
# 1й вариант
print(f'{hour}:{min}:{sec}')
# 2й с  переменной
full_time = f'{hour}:{min}:{sec}'
print(full_time)
