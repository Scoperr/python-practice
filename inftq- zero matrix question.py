import numpy as np
m = int(input())
matrix = [list(map(int,input().split())) for i in range(m)]
a = np.array(matrix)
a = list(np.transpose(a))
print(a)
print(matrix)
a = []
for i in range(1,len(matrix)+1):
    if 0 in matrix[i-1]:
        row = i-1
        matrix[i-1] = [0 for j in range(len(matrix[i-1]))]
for i in range(1,len(a)+1):
    if 0 in a[i-1]:
        row = i-1
        a[i-1] = [0 for j in range(len(a[i-1]))]
print(matrix)
print(a)
