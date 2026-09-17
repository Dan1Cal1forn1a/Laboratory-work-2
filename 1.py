print('Эта программа вычисляет площадь треугольника по его сторонам')
while True:
    first = float(input('Введите первую сторону треугольника: '))
    second = float((input('Введите вторую сторону треугольника: ')))
    third = float((input('Введите третью сторону треугольника: ')))
    if first > (second + third) or second > (first + third) or third > (second + first) or first<=0 or second<=0 or third<=0:
        print('Такой треугольник не существует. Попробуйте снова.')
        continue
    half_perimeter = (first + second + third)/2
    S=(half_perimeter * (half_perimeter - first) * (half_perimeter - second) * (half_perimeter - third))**0.5
    S = round(S, 2)
    print('Площадь введённого треугольника:', S)
