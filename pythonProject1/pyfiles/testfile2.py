f = open('text', 'r')

c = f.readlines()
print(c[0].split())
a = list(map(int, c[0].split()))