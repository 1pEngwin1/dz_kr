print('Введите четыре числа с клавиатуры')
x = int(input())
y = int(input())
z = int(input())
e = int(input())

print('Максимальное число = ', max(x,y,z,e)) #не особо видел смысл делать ифами, но на всякий случай написал

if (x > y) and (x > z) and (x > e):
    print('Максимальное число = ', x)
elif (y > x) and (y > z) and (y > e):
    print('Максимальное число = ', y)
elif (z > x) and (z > y) and (z > e):
    print('Максимальное число = ', z)
else:
    print('Максимальное число = ', e)