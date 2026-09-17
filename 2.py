print('Эта программа переводит значение расстояния из одной единицы в другую.')
print('Используемые единицы: километры (1), метры (2), сантиметры (3), миллиметры (4), мили (5) и ярды (6).')
while True:
    before = int(input('Выберите единицу исходную единицу измерения по её номеру в списке: '))
    if before not in (1,2,3,4,5,6):
        print('Ошибка: такой единицы измерения нет в списке. Попробуйте снова.')
    else:
        break
while True:
    after = int(input('Выберите желаемую единицу измерения по её номеру в списке: '))
    if after not in (1,2,3,4,5,6):
        print('Ошибка: такой единицы измерения нет в списке. Попробуйте снова.')
    else:
        break
number = float(input('Введите значение расстояния в исходных единицах измерения: '))

meter = 1
kilometer = 1000
centimeter = 0.01
millimeter = 0.001
mil = 1609.34
yard = 0.9144

if before==1:
    number = number*kilometer
elif before==2:
    number = number*meter
elif before==3:
    number = number * centimeter
elif before==4:
    number = number*millimeter
elif before==5:
    number = number*mil
elif before==6:
    number = number*yard

if after==1:
    number = number/kilometer
    number = round(number, 2)
    print('Полученный результат в километрах:', number)
elif after==2:
    number = number/meter
    number = round(number, 2)
    print('Полученный результат в метрах:', number)
elif after==3:
    number = number / centimeter
    number = round(number, 2)
    print('Полученный результат в сантиметрах:', number)
elif after==4:
    number = number/millimeter
    number = round(number, 2)
    print('Полученный результат в милиметрах:', number)
elif after==5:
    number = number/mil
    number = round(number, 2)
    print('Полученный результат в милях:', number)
elif after==6:
    number = number/yard
    number = round(number, 2)
    print('Полученный результат в ярдах:', number)