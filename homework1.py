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
