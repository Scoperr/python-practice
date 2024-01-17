m = [int(x) for x in input()]
n = [int(y) for y in input()]
print(sum(set(list(set(m)-set(n))+list(set(n)-set(m)))))
