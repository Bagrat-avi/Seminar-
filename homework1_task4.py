#4 Напишите функцию для вывода треугольника. Функция принимает два аргумента – size (количество строк, на которых будет строиться треугольник) и symb (символ, используемый для заполнения треугольника).
def triangle(size, symb):
    for i in range(1, size + 1):
        print(symb * min(i, size - i + 1))
size, symb = input().split()
size = int(size)
triangle(size, str(symb))
