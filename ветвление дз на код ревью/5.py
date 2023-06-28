print('Введите стороны треугольника')
x = int(input())
y = int(input())
z = int(input())

if (x + y > z) and (x + z > y) and (y + z > x):
    print('True')
else:
    print('False')