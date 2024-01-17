import numpy as np
s = input()
n = int(input())
a = []
start = 0
end = n-1
ran = end+1
while(True):
    if start>=len(s) and end>=len(s):
        break
    q = s[start:end+1]
    a.append([i for i in q])
    if ran>=len(s):
        break
    for j in range(n-2):
        l = []
        for k in range(n-1):
            l.append("")
        l.insert(j+1,s[ran])
        ran+=1
        l.reverse()
        a.append(l)
    start = (ran)
    end = (start+n-1)
    ran = (end+1)
if len(a[len(a)-1]) != len(a[0]):
    for f in range(len(a[0]) - len(a[len(a)-1])):
        a[len(a)-1].append("")
print(a)
a = np.array(a,dtype = str)
a = np.transpose(a)
ss = ""
for i in a:
    ss+= "".join(i)
print(ss)
