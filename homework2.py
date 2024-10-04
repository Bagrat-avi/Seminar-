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
