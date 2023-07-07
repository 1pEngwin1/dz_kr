print('Введите стороны треугольника')
x = int(input())
y = int(input())
z = int(input())

if (x + y > z) and (x + z > y) and (y + z > x):
    if x == y and z == y and x == z:
        print('Равносторонний треугольник')
    elif x == y or y == z or x == z:
        print('Равнобедренный треугольник')
    else:
        print('Разносторонний треугольник')
else:
    if max(x,y,z) == ((x + y + z)/2):
        print('Вырожденный треугольник')
    else:
        print('Не является треугольником')

