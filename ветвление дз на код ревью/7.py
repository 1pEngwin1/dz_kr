print('Введите четыре числа')
a = int(input())
b = int(input())
c = int(input())
d = int(input())

dlina = 0

if a < d:
    x = b - a + 1
    y = d - c + 1
    if c > a and b < d:
        dlina = max(x,y) - abs(a - c)
    elif c > a and b > d:
        dlina = max(x, y) - abs(a - c) - abs(b - d)
    elif a > c and b < d:
        dlina = max(x, y) - abs(a - c) - abs(b - d)
    elif a > c and b > d:
        dlina = max(x, y) - abs(a - c)
elif a == d or c == b:
    dlina = 1

print(dlina)
