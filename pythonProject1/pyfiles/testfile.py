import time

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(matrix1)):
         print(f'i = {i}')
         time.sleep(0.5)
         for j in range(len(matrix1[0])):
                  time.sleep(0.5)
                  print(j)
                  result[i][j] = matrix1[i][j] + matrix2[i][j]
                  print(result)
                  time.sleep(0.5)

print(result)
