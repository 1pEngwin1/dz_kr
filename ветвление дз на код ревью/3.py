print('Введите четыре числа с клавиатуры')
x = int(input())
y = int(input())
z = int(input())
e = int(input())

print('Минимальное число = ', min(x,y,z,e)) #не особо видел смысл делать ифами, но на всякий случай написал

if (x < y) and (x < z) and (x < e):
    print('Минимально число = ', x)
elif (y < x) and (y < z) and (y < e):
    print('Минимально число = ', y)
elif (z < x) and (z < y) and (z < e):
    print('Минимально число = ', z)
else:
    print('Минимально число = ', e)
