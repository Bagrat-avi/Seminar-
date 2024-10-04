#1 Написать функцию, считающую N-ое число Фибоначчи (N вводится с клавиатуры).
def fib(n):
    if n <= 0:
        return "Ошибка"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
N = int(input())
print(fib(N))


#6 Напишите функцию, считающую коэффициенты МНК для набора измерений x и y.
import numpy as np
x = np.array([3,6,7,8,5,6,4])
y = np.array([7,3,9,2,6,4,7])
a = (np.mean(x*y) - np.mean(x)*np.mean(y)) / (np.mean(x**2) * np.mean(x)**2)
b = np.mean(y) - a*np.mean(x)
std_a = 1/np.sqrt(len(x)) * np.sqrt((np.mean(y**2)-np.mean(y)**2)/((np.mean(x**2)-np.mean(x)**2))-a**2)
str_b = std_a* np.sqrt(np.mean(x**2)-np.mean(x)**2)
print(std_a, str_b)

#2. Написать функцию, раскладывающую число на простые множители (число вводится с клавиатуры).
def simple(n):
    if n <= 1:
        return []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + simple(n // i)
    return [n]
n = int(input())
print(simple(n), " ")



#4 Напишите функцию для вывода треугольника. Функция принимает два аргумента – size (количество строк, на которых будет строиться треугольник) и symb (символ, используемый для заполнения треугольника).
def triangle(size, symb):
    for i in range(1, size + 1):
        print(symb * min(i, size - i + 1))
size, symb = input().split()
size = int(size)
triangle(size, str(symb))

#3 Со времен Евклида известно, что для любых положительных a и b существуют такие целые x и y, что ax + by = d, где d – наибольший общий делитель a и b. По заданным a и b найти x, y, d.
def evklid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = evklid(b, a % b)
        return d, y, x - y * (a // b)
m, n = map(int, input().split())
print(evklid(m, n))

#5
n, m = [int(i) for i in input().split()]
matrix = []
for i in range(n):
    temp = [0 for num in range(m)]
    matrix.append(temp)
x,y,= 0, 0
k = int(1)
matrix[0][0]=1
while k < m*n:
    if x + 1 < m:
        if matrix[y][x+1] == 0:
            x+=1
            k+=1
            matrix[y][x] = k
            continue
    if y+1< n:
        if matrix[y+1][x] == 0:
            y+=1
            k+=1
            matrix[y][x] = k
            continue
    if matrix[y][x-1] == 0 and x-1>=0:
        x-=1
        k+=1
        matrix[y][x] = k
        continue
    while matrix[y-1][x] == 0:
        y-=1
        k+=1
        matrix[y][x] = k
for row in matrix:
    print(*row)
