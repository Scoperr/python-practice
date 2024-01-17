import numpy as np
def find_col(arr):
    for i in range(len(arr[0])):
        j = 0
        s = ""
        d_col = dict()
        while(j<len(arr)):
            if arr[j][i] not in d_col:
                d_col[arr[j][i]] = 1
            else:
                d_col[arr[j][i]] += 1
            s += str(arr[j][i])
            j += 1
        for i in d_col.keys():
            if str(i)*4 in s:
                d.append(i)
        col.append(s)

def find_row(arr):
    for i in range(len(arr)):
        j = 0
        s = ""
        d_row = dict()
        while(j<len(arr[0])):
            if arr[i][j] not in d_row:
                d_row[arr[i][j]] = 1
            else:
                d_row[arr[i][j]] += 1
            s += str(arr[i][j])
            j += 1
        for i in d_row.keys():
            if str(i)*4 in s:
                d.append(i)
        row.append(s)

def dia(a,b):
    for i in range(len(a)):
        j = len(a)-i-1
        k = i
        while j!=0:
            a[i].insert(0,-1)
            b[i].insert(len(b[i]),-1)
            j-=1
        for k in range(i):
            a[i].insert(len(a[i]),-1)
            b[i].insert(0,-1)
        dia3.append(b[i])
        dia1.append(a[i])
 
    n_dia = np.array(dia1)
    n_dia = np.transpose(n_dia)
    n_d = np.array(dia3)
    n_d = np.transpose(n_d)
    for i in n_dia:
        s = ""
        di = dict()
        for j in i:
            if j>-1 and j not in di:
                s+=str(j)
                di[j] = 1
            elif j>-1:
                s+=str(j)
                di[j] += 1
        dia2.append(s)
        for i in di.keys():
            if str(i)*4 in s:
                d.append(i)

    for i in n_d:
        s = ""
        di = dict()
        for j in i:
            if j>-1 and j not in di:
                s+=str(j)
                di[j] = 1
            elif j>-1:
                s+=str(j)
                di[j] += 1
        dia4.append(s)
        for i in di.keys():
            if str(i)*4 in s:
                d.append(i)
dia1 = []
dia2 = []
dia3 = []
dia4 = []
m = int(input())
d = []
col = []
row = []
if m>3:
    arr = []
    for i in range(m):
        l = list(map(int,input().split()))
        arr.append(l)
    b = []
    for i in arr:
        f = []
        for j in i:
            f.append(j)
        b.append(f)
    find_col(arr)
    find_row(arr)
    dia(arr,b)
    print(row)
    print(col)
    print(np.array(dia2))
    print(np.array(dia4))
    if not d:
        print("-1")
    else:
        print(d)
        print(min(d))
else:
    print("M value should be greater than 3 :)")
