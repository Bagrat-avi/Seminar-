#3 Со времен Евклида известно, что для любых положительных a и b существуют такие целые x и y, что ax + by = d, где d – наибольший общий делитель a и b. По заданным a и b найти x, y, d.
def evklid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = evklid(b, a % b)
        return d, y, x - y * (a // b)
m, n = map(int, input().split())
print(evklid(m, n))
