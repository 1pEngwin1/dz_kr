print('Введите четыре числа')
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < d:
    






kol = 0

for i in range(a,b+1):
    for j in range(c,d+1):
        if i == j:
            kol += 1
print(kol)
